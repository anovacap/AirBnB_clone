#!/usr/bin/python3
"""Unit test for class Amenity"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import sys
import os
import pep8
from unittest.mock import create_autospec
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


class TestAmenity(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model1 = Amenity()
        self.my_model1.name = "hello"
        self.my_model1.state_id = "Ca"
        self.my_model2 = Amenity()
        self.my_model2.name = 2
        self.my_model2.state_id = 2
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_amenity(self):
        """test for review"""
        self.assertEqual(self.my_model1.name, "hello")
        self.assertEqual(type(self.my_model1.name), str)
        self.assertEqual(self.my_model1.state_id, "Ca")
        self.assertEqual(type(self.my_model1.state_id), str)
        self.assertEqual(self.my_model2.state_id, 2)
        self.assertEqual(type(self.my_model2.name), int)

if __name__ == '__main__':
    unittest.main()
