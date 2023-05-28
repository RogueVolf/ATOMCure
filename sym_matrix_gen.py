import pandas as pd

df = pd.read_csv("Symptoms/dataset.csv")

df.head()
symptoms = []
for i in range(1,11):
    symptoms.append(list(df[f'Symptom_{i}'].values))
uni_sym = []
for sym in symptoms:
    for val in sym:
        if val not in uni_sym:
            uni_sym.append(val)
uni_sym.remove(0)
df.fillna(0,inplace=True)
df.drop(['Symptom_17','Symptom_16','Symptom_15','Symptom_14','Symptom_13','Symptom_12','Symptom_11'],axis=1,inplace=True)
df['Disease'].values
symp_dict = {}
for vals in df['Disease'].values:
    symp_dict[vals] = []
import numpy as np
for index,row in df.iterrows():
    symp_dict[row[0]].append(list(row[1:]))
import pickle as pkl
with open('symptoms.pkl', 'wb') as file:
    pkl.dump(symp_dict, file)