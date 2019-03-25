#!/usr/bin/python3
"""Unit test for class State"""
import unittest
from models.base_model import BaseModel
from models.state import State
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


class TestState(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model1 = State()
        self.my_model1.name = "Me"
        self.my_model2 = State()
        self.my_model2.name = 2
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_state(self):
        """test for review"""
        self.assertEqual(self.my_model1.name, "Me")
        self.assertEqual(type(self.my_model1.name), str)

if __name__ == '__main__':
    unittest.main()
