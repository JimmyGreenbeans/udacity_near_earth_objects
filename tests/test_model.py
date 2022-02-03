"""

"""
from lib2to3.pgen2.token import EQUAL
import pathlib
import unittest
import sys
import os
from numpy import equal
import pandas as pd
import json
import datetime
sys.path.append(r'..\udacity_near_earth_objects')
from models import NearEarthObject, CloseApproach

class TestModels(unittest.TestCase):

    #def set_up(self):
        # read near earth objects database
        # neos = pd.read_csv('data\\neos.csv')
        # self.neo_dict_1 = neos.loc[0, :].to_dict()
        # self.neo_dict_2 = neos.loc[23780, :].to_dict()

    def test_model_neos(self):
        neos = pd.read_csv('data\\neos.csv')
        neo_1_dict = neos.loc[0, :].to_dict()
        neo_2_dict = neos.loc[23780, :].to_dict()
        neo_1 = NearEarthObject(**neo_1_dict)
        neo_2 = NearEarthObject(**neo_2_dict)

        self.assertEqual(neo_1.name, 'Eros')
        self.assertAlmostEqual(neo_1.diameter, 16.84, 2)
        self.assertEqual(neo_1.hazardous, False)
        self.assertEqual(neo_2.name, None)
        self.assertEqual(neo_2.hazardous, False)
    
    def test_model_close_approaches(self):
        with open('data\\cad.json', 'r') as file:
            cad = json.load(file)
        ca_df = pd.DataFrame(cad['data'], columns=cad['fields'])
        ca_1_dict = ca_df.loc[0, :].to_dict()
        ca_1 = CloseApproach(**ca_1_dict)

        self.assertIsInstance(ca_1.time, datetime.datetime)
        self.assertEqual(ca_1.time_str, '1900-01-01 00:11')
        self.assertAlmostEqual(ca_1.distance, 0.09217, 2)
        self.assertAlmostEqual(ca_1.velocity, 16.7523, 2)
            
if __name__ == '__main__':
    unittest.main()