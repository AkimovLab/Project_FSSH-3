 This folder contains the scripts and files for conducting the calculations
 needed for the FSSH3 project


# 1. Methodologies 

The methodologies are defined in the `recipes` folder. Here, I consider:

  - FSSH
  - FSSH-2
  - FSSH-3
  - GFSH

# 2. Running TSH calculations:

Here, the integrator is reset to use the NAC-based approach + phase correction and state tracking are turned on

This is all done in the tsh.py script


## 2a. Run individual TSH calculations

To run the TSH calculation, use the `tsh.py` file with the suitable arguments.
Run it e.g. like:

    python tsh.py --model_indx=0 --method_indx=0 --dt=4.0


## 2b. Run all TSH calculation

Edit the `run_all.py` script as needed, then:

    python run_all.py


# 3. Plot the population dynamics for all methods and models

Use Jupyter notebook: `plot-all.ipynb`
