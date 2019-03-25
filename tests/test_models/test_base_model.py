#!/usr/bin/python3
"""Unit test for class BaseModel"""
import unittest
from models.base_model import BaseModel
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


class TestBaseModel(unittest.TestCase):
    """Tests for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model1 = BaseModel()
        self.my_model1.name = "hello"
        self.my_model1.number = 9
        self.my_model2 = BaseModel()
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

    def test_doctest(self):
        """test if docstring exists"""
        self.assertTrue(BaseModel.__doc__)
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)

    def test_attr(self):
        """test if class has attributes"""
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue("updated_at" in self.my_model1.__dict__)
        self.assertTrue("created_at" in self.my_model1.__dict__)
        self.assertTrue("id" in self.my_model1.__dict__)

    def test_quit(self):
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))
        self.assertTrue(cli.onecmd("EOF"))

    def test_str(self):
        """test __srt__"""
        pass

    def test_save(self):
        """test save"""
        self.my_model1.save()
        self.assertNotEqual(self.my_model1.created_at,
                            self.my_model1.updated_at)

    def test_to_dict(self):
        """test to_dict"""
        self.assertEqual(self.my_model1.__class__.__name__, "BaseModel")

    def test_pep8(self):
        """test if module is pep8 compliant"""
        pep = pep8.StyleGuide(quiet=False)
        sty = pep.check_files(["models/base_model.py",
                               "tests/test_models/test_base_model.py"])
        self.assertEqual(sty.total_errors, 0, "PEP8 Errors")

if __name__ == '__main__':
    unittest.main()
