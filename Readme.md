# Description for uploaded data

This repository provides additional data associated with the manuscript **"Data-Driven Analysis of Lithium-ion Transport in Covalent-Organic Frameworks (Lim et al., 2026)"**. </br>

This repository contains three main components:</br>

1. `all_data.csv`
2. `screening/`
3. `training/`

---



## 1. `all_data.csv`

- This file contains the complete dataset for 362 filtered COF frameworks derived from the Curated COF database after molecular dynamics (MD) simulations.
- Each row corresponds to a single COF structure. The columns include:
  - Lithium-ion diffusion coefficient
  - R2 score from linear regression of the MSD curve (used to assess reliability)
  - Geometric descriptros calculated using Zeo++:
    - Largest cavity diameter (LCD)
    - Pore limiting diameter (PLD)
    - Accessible surface area (ASA)
    - Accessible surface volume
    - Accessible void fraction


---



## 2. `screening/` directory

- This directory contains example input files for molecular dynamics (MD) simulations. Four representative COFs with different topologies are provided: `05001N2_ddec, 16170N2_ddec, 16510N2_ddec, 20470N2_ddec`.

- Each example directory includes:

  (a) `PACKMOL/` subdirectory

  - Input files for Packmol software to generate initial configurations of framework + LiClO4 systems.
  - `.inp` files with associated framework and ion salt structure files.

  (b) Moltempate files

  - `ddec-LiClO4.lt`, `Rev-{name}-0.75.lt`, `system.lt`
  - These files are used with Moltemplate software to generate LAMMPS input files.

  (c) LAMMPS input files

  - `lmp.in.run`, `system.data`, `system.in`, `system.in.init`, `system.in.settings`
  - These files allow reproduction of the MD simulations described in the manuscript.

---



## 3. `training/` directory

- This directory contains scritps and metadata required to reproduce machine learning training using PMTransformer.

  (a) `folds.csv`

  - Specifies fold assignments for 5-fold cross-validation.
  - COFs labeled with `fold = k` were used as validation data in fold *k* and as training data in all other folds.

  (b) `prepare_data.py`

  - Script used to construct the dataset for PMTransformer training.
    - Target properties must be prepared in `.json` format.
    - The `max_length` parameter was set to 1000 (default: 60) to accomodate large COF structures.

  (c) Jupyter Notebooks

  - `fromscratch_training.ipynb`, `pmtransformer_training.ipynb`
  - These notebooks perform model training using 5 learning rates and 5 weight decay values.

- Details of files as follows:

  1. folds.csv
     - Designate each COF were belongs to validation of which fold. For example, COFs tagged with fold 0 was used as validation set during training with fold 0 and other COFs were used as training set.
  2. prepare_data.py
     - Construct dataset for PMTransformer. .json files with target properties should be prepared.
     - max_length was changed as 1000 (default: 60) to deal with COFs with large size.
  3. .ipynb files (from scratch_training.ipynb and pmtransformer_training.ipynb)
     - Jupyter notebook files to run training with constructed dataset.
     - Combinations of 5 learning rates and 5 weight decays were tested.

---



## 3. Citations :page_with_curl:

Citation information will be uploaded after publication.

---



## 4. Acknolwedgements :muscle:

Acknowledgements will be added after publication.