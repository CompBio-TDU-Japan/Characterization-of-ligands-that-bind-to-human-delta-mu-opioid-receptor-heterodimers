import numpy as np
import pandas as pd
import time
from rdkit import Chem
from mordred import Calculator , descriptors


t1 = time.time()

print('start')
calc = Calculator(descriptors, ignore_3D = True)
sdf = [mol for mol in Chem.SDMolSupplier('10396full_ligand.sdf')]
df = calc.pandas(sdf).astype('float').dropna(axis = 1)
print(df)
df.to_csv('dataset_no3ded.csv')

t2 = time.time()
fullcalc_time = t2 - t1

print(f'finish : {fullcalc_time} s')
