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
    """set up"""
    ob = storage.all()
    ob.clear()
    storage.save()
    if os.path.isfile('file.json'):
        os.remove('file.json')


def tearDownModule():
    """tear down"""
    ob = storage.all()
    ob.clear()
    storage.save()
    if os.path.isfile('file.json'):
        os.remove('file.json')


class TestConsole(unittest.TestCase):
    """Test for the console"""
    def setUp(self):
        """Set up for the tests"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """create api enviroment"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last 'n' output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(
            lambda c: c[0][0], self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        """test quit"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))
        self.assertTrue(cli.onecmd("EOF"))

if __name__ == '__main__':
    unittest.main()
