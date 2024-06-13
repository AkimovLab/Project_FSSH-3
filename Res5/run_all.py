import os, sys

#============= TSH ============================

for model_indx in [0, 1, 3]:
    for method_indx in [10, 20]:
        for dt in [4.0]:
            os.system(F"python tsh.py --model_indx={model_indx} --method_indx={method_indx} --dt={dt}")


