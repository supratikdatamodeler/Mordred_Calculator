import streamlit as st
import pandas as pd
from rdkit import Chem
from mordred import Calculator, descriptors
import tempfile

# Function to calculate descriptors
def calculate_descriptors(input_file, file_format):
    """
    Calculate Mordred descriptors for molecules from different file formats.

    Args:
        input_file: Uploaded file object.
        file_format: Format of the uploaded file (e.g., 'sdf', 'pdb').
    """
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_format}") as temp_file:
        temp_file.write(input_file.read())
        temp_file_path = temp_file.name

    # Read molecules based on file format
    if file_format == "sdf":
        suppl = Chem.SDMolSupplier(temp_file_path)
    elif file_format == "pdb":
        suppl = [Chem.MolFromPDBFile(temp_file_path, sanitize=False)]
    else:
        st.error("Unsupported file format")
        return pd.DataFrame()

    calc = Calculator(descriptors, ignore_3D=False)

    descriptor_data = []
    for idx, mol in enumerate(suppl):
        if mol is None:
            st.warning(f"Error reading molecule at index {idx}")
            continue

        molecule_id = f"Molecule_{idx}"
        try:
            desc_values = calc(mol)
            desc_dict = desc_values.asdict()
            desc_dict['ID'] = molecule_id
            descriptor_data.append(desc_dict)
        except Exception as e:
            st.warning(f"Error processing molecule ID {molecule_id}: {e}")

    descriptor_df = pd.DataFrame(descriptor_data)

    # Filter out non-numeric or boolean columns (except 'ID')
    numeric_columns = ['ID'] + [
        col for col in descriptor_df.columns
        if col == 'ID' or (pd.api.types.is_numeric_dtype(descriptor_df[col]) and not pd.api.types.is_bool_dtype(descriptor_df[col]))
    ]
    descriptor_df = descriptor_df[numeric_columns]

    # Remove or rename duplicate columns
    descriptor_df = descriptor_df.loc[:, ~descriptor_df.columns.duplicated()].copy()

    return descriptor_df

# Streamlit UI
st.title("Mordred Descriptor Calculator")
st.write("Upload a file in SDF (.sdf) or PDB (.pdb) format.")

uploaded_file = st.file_uploader("Upload a file", type=["sdf", "pdb"])

if uploaded_file:
    file_format = uploaded_file.name.split(".")[-1].lower()

    # Display "Processing file..." while calculations are ongoing
    with st.spinner("Processing file..."):
        output_df = calculate_descriptors(uploaded_file, file_format)

    if not output_df.empty:
        st.success("Descriptors calculated successfully!")
        st.dataframe(output_df)

        # Provide download link for CSV
        csv = output_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=csv, file_name="output_descriptors.csv", mime="text/csv")
    else:
        st.error("No descriptors could be calculated. Please check the input file.")
