#!/usr/bin/python3
"""unittest for console.py

Unittest classes:
	TestHBNBCommand_prompting
    	TestHBNBCommand_help
    	TestHBNBCommand_exit
    	TestHBNBCommand_create
    	TestHBNBCommand_show
    	TestHBNBCommand_all
    	TestHBNBCommand_destroy
    	TestHBNBCommand_update
"""

import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand

class TestHBNBCommand_prompting(unittest.TestCase):
	
