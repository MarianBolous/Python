import pandas as pd
df = pd.read_csv('pokemondata.csv')
# print (df)

# print(df.head(3))
# print(df.tail(3))

#df_xlsx =  pd.read_excel('pokemondata.xlsx')
#print(df_xlsx.head(3))

#df = pd.read_csv('pokemondata.txt', delimiter='\t')
#print (df)

#read headers
#df.columns
#print (df.columns)

#read column
#print (df[['Name', 'Type 1','HP']][0:5])
#print (df.Name)
#print (df['Name'][0:5])

#read each row
#print (df.head(4))
#print (df.iloc[0:4])
#for index, row in df.iterrows():
 #print (index, row)
 #print (index, row['Name'])
#print(df.iloc[0,1])
#print (df.loc[df['Type 1'] == "Fire"])


#print(df.describe())
#print(df.sort_values('Name', ascending=False))
#print(df.sort_values(['Type 1', 'HP'], ascending=True))
#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

#df.head(5)
#df['Total'] = df['HP'] + df['Attack']+df['Defense']+df['Sp. Atk']+ df['Sp. Def']+df['Speed']
#print (df)

#df = df.drop(columns=['Total'])
#print (df.columns)

#df['Total']= df.iloc[:,4:10].sum(axis=1)
#cols = list(df.columns)
#print (df)
#df = df[cols[0:4] +cols[4:13]]

#print (df)

#df.to_csv('modified.csv', index=False)
#df.to_csv('modified.txt', index=False, sep='\t')

#df.loc[(df['Type 1']=='Grass') & (df['Type 2'] == 'Poison'& (df['HP'] > 7)

import re

#df.loc[~df['Name'].str.contains('Mega', regex=True)]
#df.loc[~df['Name'].str.contains('Fire|Grass', flags=re.I , regex=True)]
df.loc[~df['Name'].str.contains('^pi[a-z]*', regex=True)]
print(df)
