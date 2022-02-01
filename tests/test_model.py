"""

"""
from lib2to3.pgen2.token import EQUAL
import pathlib
import unittest
import sys
import os
from numpy import equal
import pandas as pd
sys.path.append(r'..\udacity_near_earth_objects')
from models import NearEarthObject, CloseApproach

class TestModels(unittest.TestCase):

    #def set_up(self):
        # read near earth objects database
        # neos = pd.read_csv('data\\neos.csv')
        # self.neo_dict_1 = neos.loc[0, :].to_dict()
        # self.neo_dict_2 = neos.loc[23780, :].to_dict()

    def test_models(self):
        neos = pd.read_csv('data\\neos.csv')
        neo_dict_1 = neos.loc[0, :].to_dict()
        neo_dict_2 = neos.loc[23780, :].to_dict()
        neo_1 = NearEarthObject(**neo_dict_1)
        neo_2 = NearEarthObject(**neo_dict_2)

        self.assertEqual(neo_1.name, 'Eros')
        self.assertAlmostEqual(neo_1.diameter, 16.84, 2)
        self.assertEqual(neo_1.hazardous, False)
        self.assertEqual(neo_2.name, None)
        self.assertEqual(neo_2.hazardous, False)
                


if __name__ == '__main__':
    unittest.main()