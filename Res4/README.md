 This folder contains the scripts and files for conducting the calculations
 needed for the FSSH3 project


# 1. Methodologies 

In this folder, I only test the FSSH-3 method, but using several of its variations

Here, I test the case of J mapping the populations, not population to population time-derivative as before


# 2. Run TSH calculations

## 2a. Run individual TSH calculations

To run the TSH calculation, use the `tsh.py` file with the suitable arguments.
Run it e.g. like:

    python tsh.py --model_indx=0 --method_indx=0 --dt=4.0


## 2b. Run all TSH calculation

Edit the `run_all.py` script as needed, then:

    python run_all.py


# 3. Plot the population dynamics for all methods and models

Use Jupyter notebook: `plot-all.ipynb`
