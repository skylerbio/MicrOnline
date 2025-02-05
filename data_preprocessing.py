import pandas as pd
import numpy as np

abundance_table = pd.read_excel("/Users/julietmalkowski/Desktop/Research/Kinetic_Model/abundance_table.xlsx")
#remove first 4 characters in every column name
abundance_table.columns = abundance_table.columns.str[4:] 
#split string in column to get date and process
abundance_table[['Process','Date']] = abundance_table['le'].str.split('_',expand=True)
abundance_table = abundance_table.drop(columns=['le'])
processes = ['AS-1', 'AS-2']
as_abundance_table = abundance_table[abundance_table['Process'].isin(processes)]
as_abundance_table = as_abundance_table.drop(columns=['Process'])
#group by date and find the mean of all values
as_abundance_table = as_abundance_table.groupby(['Date']).mean()
#remove last two rows of as_abundance_table
a = as_abundance_table.iloc[:,:-2]
a = a.reset_index()
#remove first column in a
a = a.iloc[:,1:]
a = a.to_numpy()


r = pd.read_csv('/Users/julietmalkowski/Desktop/Research/Kinetic_Model/reads.sintax.csv', sep = ",", skiprows=0, header=0, engine = 'python').reset_index()
r.drop(r.columns[[2, 3]], axis=1, inplace=True)
r.columns = ['OTU','Classification']
r[['domain','phylum','class','order','family','genus','species']] = r['Classification'].str.split(',', expand=True)
r.drop(r.columns[[1]], axis=1, inplace=True)
r = r.applymap(lambda x: x.split('(')[0])
r = r.applymap(lambda x: x[x.find(':')+1:] if ':' in x else x)
r.to_excel('tax.xlsx')