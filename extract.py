"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path): # path = 'data\\neos.csv'
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    
    with open(neo_csv_path, "r") as infile:
        reader = csv.DictReader(infile)
        neos_list = []
        for neo in reader:        
            # get list of neos (dictionaries)
            neos_list.append(neo)

    # create list of NEO Objects
    neos = []
    for neo in neos_list:
        neos.append(NearEarthObject(**neo))
    return neos


def load_approaches(cad_json_path): # path = 'data\\cad.json'
    
    # """Read close approach data from a JSON file.

    # :param cad_json_path: A path to a JSON file containing data about close approaches.
    # :return: A collection of `CloseApproach`es.
    # """

    with open(cad_json_path, 'r') as file:
        cad = json.load(file)

    ca_list = []
    for ca in cad['data']:
        ca_list.append(dict(zip(cad['fields'], ca)))
    # create a list of CloseApproach Objects
    cas = []
    for ca in ca_list:
        cas.append(CloseApproach(**ca))
    return cas
