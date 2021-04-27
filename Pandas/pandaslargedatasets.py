import pandas as pd
df = pd.read_csv('modified.csv')
for df in pd.read_csv('modified.csv',chunksize=5):
 print('CHUNK DF')
 print (df)
