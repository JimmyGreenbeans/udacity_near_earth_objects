import pandas as pd
import csv
import json

# read near earth objects database
neos = pd.read_csv('data\\neos.csv')
# print(neos.head())

# liste = []
# with open('data\\neos.csv') as in_file:
#     csv_reader = csv.DictReader(in_file, delimiter=";")
#     for row in csv_reader:
#         lex = {}
#         for key, value in row.items():
#             lex[key] = value
#             liste.append(lex)

# read
with open('data\\cad.json', 'r') as file:
    cad = json.load(file)
    cad_dict = dict(zip(cad['fields'], cad['data']))
print('done')


# How many NEOs are in the neos.csv data set?
# Hint: Count the number of rows in the neos.csv file.
# Answer: 23967
# What is the primary designation of the first Near Earth Object in the neos.csv data set?
# Hint: Look at the first row of the CSV, under the header "pdes"
# Answer: 433
# What is the diameter of the NEO whose name is "Apollo"?
# Hint: Look for the row of the CSV containing the name "Apollo" in the "name" column, and find the entry under the "diameter" column.
# Answer: 1.5 kilometers
# How many NEOs have IAU names in the data set?
# Hint: Count the number of rows that have nonempty entries in the "name" column.
# Answer: 343
# How many NEOs have diameters in the data set?
# Hint: Count the number of rows that have nonempty entries in the "diameter" column.
# Answer: 1268
# How many close approaches are in the cad.json data set?
# Hint: Instead of manually counting the entries, you can use the value of the "count" key.
# Answer: 406785
# On January 1st, 2000, how close did the NEO whose primary designation is "2015 CL" pass by Earth?
# Find entries whose date starts with '2000-Jan-01'. One of the lists represents the close approach of the NEO "2015 CL". What is the value corresponding to the distance from Earth?
# Answer: About 0.145 au
# On January 1st, 2000, how fast did the NEO whose primary designation is "2002 PB" pass by Earth?
# Hint: Find entries whose date starts with '2000-Jan-01'. One of the lists represents the close approach of the NEO "2002 PB". What is the value corresponding to the velocity relative to Earth?
# Answer: About 29.39 km/s