# Mordred_Calculator

Mordred_Calculator is a web application designed to calculate Mordred descriptors for chemical structures provided in SDF (.sdf) or PDB (.pdb) file formats. The descriptors are generated using the Mordred library developed by Moriwaki et al. (2018).

## Description

This application provides an intuitive interface powered by **Streamlit** to calculate molecular descriptors commonly used in cheminformatics, machine learning, QSAR modeling, and other computational chemistry workflows. The goal is to facilitate education and research by enabling students and researchers to compute Mordred descriptors effortlessly from chemical structure files.

### Citation for Mordred Descriptors

If you use this calculator or the Mordred descriptors in your research, please cite the following paper:

**Moriwaki H, Tian Y-S, Kawashita N, Takagi T (2018).**  
Mordred: A Molecular Descriptor Calculator.  
*Journal of Cheminformatics*, 10:4.  
[https://doi.org/10.1186/s13321-018-0258-y](https://doi.org/10.1186/s13321-018-0258-y)

### Citation for This Application

If you use this application in your research or teaching, kindly include a citation to the app:  
[https://mordred-calculator.streamlit.app/](https://mordred-calculator.streamlit.app/)

---

## Features

- **File Support**: Accepts chemical structure files in `.sdf` or `.pdb` formats.
- **Descriptor Calculation**: Uses the Mordred library to compute over 1800 molecular descriptors, including both 2D and 3D descriptors.
- **Interactive Web Interface**: Built with **Streamlit** to provide an easy-to-use and visually appealing interface.
- **CSV Export**: Download the computed descriptors as a CSV file for further analysis.

---

## Installation

To run this application locally, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/supratikdatamodeler/Mordred_Calculator.git
   cd Mordred_Calculator

2. **Set up the environment**: Install the required dependencies using Conda:
   ```bash
   conda env create -f environment.yml
   conda activate mordred_calculator

3. **Run the Streamlit app**: Using the following command:
   ```bash
   streamlit run streamlit_mordred_sdf_pdb_smiles.py

4. **Access the app**:
Open your browser and navigate to: [https://mordred-calculator.streamlit.app/]



**Dependencies**
The following major dependencies are required for this application:

Python 3.9
RDKit
Pandas
Mordred
Streamlit
NumPy
Please see the environment.yml or requirements.txt file for the full list of dependencies.

**Usage**
1. Upload an SDF or PDB file containing the chemical structures.
2. Click on the "Upload" button to process the file.
3. View the calculated descriptors in the app interface.
4. Download the results as a CSV file for further analysis.

**Legal Disclaimer**
This tool is intended for educational and research purposes only. The authors and contributors are not liable for any use of this tool beyond its intended scope. By using this application, you agree to cite the original Mordred publication and acknowledge the application in your work.

The application includes the Mordred library under its respective license. Refer to the Mordred GitHub repository for licensing details.

**Acknowledgments**
Mordred Library: Special thanks to Moriwaki et al. (2018) for developing the Mordred descriptor calculator.
Streamlit: For enabling the creation of this interactive web app.

**License**
This repository is distributed under the MIT License. See the LICENSE file for more information.



