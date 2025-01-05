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

3. **Run the Streamlit app**:
Using following:
   ```bash

   streamlit run streamlit_mordred_sdf_pdb_smiles.py


