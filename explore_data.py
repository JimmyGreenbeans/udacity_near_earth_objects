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