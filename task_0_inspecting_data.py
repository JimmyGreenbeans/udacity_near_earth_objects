from cmath import nan
import pandas as pd
import numpy as np
import csv
import json
from models import CloseApproach, NearEarthObject

# read near earth objects database
with open('data\\neos.csv', "r") as infile:
    reader = csv.DictReader(infile)
    neos_list = []
    for neo in reader:        
        # get list of neos (dictionaries)
        neos_list.append(neo)

# create list of NEO Objects
neos = []
for neo in neos_list:
    neos.append(NearEarthObject(**neo))

# alternative: Work with Pandas
# neos = pd.read_csv('data\\neos.csv')

# read
# returns a dictionary
# under cad['fields'] you get the keys
# under cad['data']
# we want a list of dictionaries with cad.['fields'] as keys
with open('data\\cad.json', 'r') as file:
    cad = json.load(file)

ca_list = []
for ca in cad['data']:
    ca_list.append(dict(zip(cad['fields'], ca)))
# create a list of CloseApproach Objects
cas = []
for ca in ca_list:
    cas.append(CloseApproach(**ca))



# alternative: Work with Pandas
# cad_df = pd.DataFrame(cad['data'], columns=cad['fields'])


#print(neos.tail())
print(type(neos.loc[:-3, 'name']))
print(type(neos.loc[0, 'name']))
x = neos.iloc[0, :].to_dict()
print(x)
y = neos.iloc[23964, :].to_dict()
print(y)
print(x['K1'])
print(type(x['K1']))
print(np.isnan(x['K1']))
x 

# How many NEOs are in the neos.csv data set?
print(len(neos))
# Hint: Count the number of rows in the neos.csv file.
# Answer: 23967

# What is the primary designation of the first Near Earth Object in the neos.csv data set?
print(neos.loc[0,'pdes'])
# Hint: Look at the first row of the CSV, under the header "pdes"
# Answer: 433

# What is the diameter of the NEO whose name is "Apollo"?
diameter = neos.loc[:, 'diameter'][neos['name'] == 'Apollo']  
print(diameter)
# Hint: Look for the row of the CSV containing the name "Apollo" in the "name" column, and find the entry under the "diameter" column.
# Answer: 1.5 kilometers

# How many NEOs have IAU names in the data set?
print(neos['name'].notnull().sum())
# Hint: Count the number of rows that have nonempty entries in the "name" column.
# Answer: 343

# How many NEOs have diameters in the data set?
print(neos['diameter'].notnull().sum())
# Hint: Count the number of rows that have nonempty entries in the "diameter" column.
# Answer: 1268

# How many close approaches are in the cad.json data set?
print(len(cad['data']))
# Hint: Instead of manually counting the entries, you can use the value of the "count" key.
# Answer: 406785

# On January 1st, 2000, how close did the NEO whose primary designation is "2015 CL" pass by Earth?
print(cad_df.loc[:, 'dist'][(cad_df['des'] == '2015 CL') & (cad_df['cd'].str.startswith('2000-Jan-01'))])
# Find entries whose date starts with '2000-Jan-01'. One of the lists represents the close approach of the NEO "2015 CL". What is the value corresponding to the distance from Earth?
# Answer: About 0.145 au

# On January 1st, 2000, how fast did the NEO whose primary designation is "2002 PB" pass by Earth?
print(cad_df.loc[:, 'v_rel'][(cad_df['des'] == '2002 PB') & (cad_df['cd'].str.startswith('2000-Jan-01'))])
# Hint: Find entries whose date starts with '2000-Jan-01'. One of the lists represents the close approach of the NEO "2002 PB". What is the value corresponding to the velocity relative to Earth?
# Answer: About 29.39 km/s