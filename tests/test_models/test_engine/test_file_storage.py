#!/usr/bin/python3
"""Unit test for class FileStorage"""
import unittest
from models.engine.file_storage import FileStorage
from unittest.mock import create_autospec
import sys
import os
import pep8
from console import HBNBCommand
from models import storage
import json
import models


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


class TestBaseModel(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model1 = FileStorage()
        self.my_model1.name = "hello"
        self.my_model1.number = 9
        self.my_model2 = FileStorage()
        self.my_model2.name = "goodbye"
        self.my_model2.number = 19
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last 'n' output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(
            lambda c: c[0][0], self.mock_stdout.write.call_args_list[-nr:]))

    def tearDown(self):
        """tear down test set up"""
        self.all_ob = storage.all()
        self.all_ob.clear()
        storage.save()

    def test_init(self):
        """test __init__"""
        self.assertEqual(type(self.my_model1.name), str)
        self.assertEqual(self.my_model1.name, "hello")
        self.assertEqual(type(self.my_model1.number), int)
        self.assertEqual(self.my_model1.number, 9)

    def test_save(self):
        self.my_model1.save()
        with open('file.json') as f:
            jd = f.read()
            pyob = json.loads(jd)
            k = pyob.keys()
        for key in models.storage.all().keys():
            self.assertTrue(key in k)

    def test_pep8(self):
        """test if module is pep8 compliant"""
        pep = pep8.StyleGuide(quiet=False)
        sty = pep.check_files(["models/engine/file_storage.py",
                               "tests/test_models/" +
                               "test_engine/test_file_storage.py"])
        self.assertEqual(sty.total_errors, 0, "PEP8 Errors")

if __name__ == '__main__':
    unittest.main()
