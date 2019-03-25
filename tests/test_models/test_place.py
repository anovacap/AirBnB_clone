#!/usr/bin/python3
"""Unit test for class Place"""
import unittest
from models.base_model import BaseModel
from models.place import Place
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


class TestPlace(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model1 = Place()
        self.my_model1.city_id = "SF"
        self.my_model1.user_id = "Me"
        self.my_model1.name = "MySelf"
        self.my_model1.description = "Big"
        self.my_model1.number_rooms = 2
        self.my_model1.number_bathrooms = 2
        self.my_model1.max_guest = 2
        self.my_model1.price_by_night = 200
        self.my_model1.latitude = 9.9
        self.my_model1.longitude = 9.9
        self.my_model1.amenity_ids = ["view"]
        self.my_model2 = Place()
        self.my_model2.name = "goodbye"
        self.my_model2.number = 19
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_place(self):
        """test for review"""
        self.assertEqual(self.my_model1.city_id, "SF")
        self.assertEqual(self.my_model1.user_id, "Me")
        self.assertEqual(self.my_model1.name, "MySelf")
        self.assertEqual(self.my_model1.description, "Big")
        self.assertEqual(self.my_model1.number_rooms, 2)
        self.assertEqual(self.my_model1.number_bathrooms, 2)
        self.assertEqual(self.my_model1.max_guest, 2)
        self.assertEqual(self.my_model1.price_by_night, 200)
        self.assertEqual(self.my_model1.latitude, 9.9)
        self.assertEqual(self.my_model1.longitude, 9.9)
        self.assertEqual(self.my_model1.amenity_ids, ["view"])
        self.assertEqual(type(self.my_model1.amenity_ids), list)
        self.assertEqual(type(self.my_model1.city_id), str)
        self.assertEqual(type(self.my_model1.user_id), str)
        self.assertEqual(type(self.my_model1.name), str)
        self.assertEqual(type(self.my_model1.description), str)
        self.assertEqual(type(self.my_model1.number_rooms), int)
        self.assertEqual(type(self.my_model1.number_bathrooms), int)
        self.assertEqual(type(self.my_model1.max_guest), int)
        self.assertEqual(type(self.my_model1.price_by_night), int)
        self.assertEqual(type(self.my_model1.latitude), float)
        self.assertEqual(type(self.my_model1.longitude), float)

if __name__ == '__main__':
    unittest.main()
