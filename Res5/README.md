 This folder contains the scripts and files for conducting the calculations
 needed for the FSSH3 project


Calculations with other schemes for velocity treatment upon the frustrated hops.
To address the Reviewer's 1 concern.

# 1. Models

To plot the PES (diabatic and adiabatic) for all the models, run:

    python plot_models.py

This will generate folders  model_0,  model_1, etc. with the figures

# 2. Methodologies 

The methodologies are defined in the `recipes` folder. Here, I consider:
  - FSSH
  - FSSH-2
  - FSSH-3
  - GFSH

# 3a. Run individual TSH calculations

To run the TSH calculation, use the `tsh.py` file with the suitable arguments.
Run it e.g. like:

    python tsh.py --model_indx=0 --method_indx=0 --dt=4.0


# 3b. Run all TSH calculation

Edit the `run_all.py` script as needed, then:

    python run_all.py


# 4. Plot the population dynamics for all methods and models

Use Jupyter notebook: `plot-all.ipynb`
