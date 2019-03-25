#!/usr/bin/python3
"""Unit test for class City"""
import unittest
from models.base_model import BaseModel
from models.city import City
from unittest.mock import create_autospec
import sys
import os
import pep8
from console import HBNBCommand
from models import storage


def setUpModule():
    ob = storage.all()
    ob.clear()
    storage.save()
    if os.path.isfile('file.json'):
        os.remove('file.json')


def tearDownModule():
    ob = storage.all()
    ob.clear()
    storage.save()
    if os.path.isfile('file.json'):
        os.remove('file.json')


class TestCity(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model1 = City()
        self.my_model1.name = "hello"
        self.my_model1.state_id = "Ca"
        self.my_model2 = City()
        self.my_model2.name = "goodbye"
        self.my_model2.number = 19
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_city(self):
        """test for review"""
        self.assertEqual(self.my_model1.name, "hello")
        self.assertEqual(self.my_model1.state_id, "Ca")

def test_pep8(self):
        """test if module is pep8 compliant"""
        pep = pep8.StyleGuide(quiet=False)
        sty = pep.check_files(["models/city.py",
                               "tests/test_models/test_city.py"])
        self.assertEqual(sty.total_errors, 0, "PEP8 Errors")

if __name__ == '__main__':
    unittest.main()
