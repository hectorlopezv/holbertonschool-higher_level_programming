import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """TestSquare"""
    
    @classmethod
    def setUpClass(cls):
        """set up of the class"""
        pass

    @classmethod
    def tearDownClass(cls):
        """tear down of classs"""
        pass

    def setUp(self):
        """reset cls attribute for test"""
        Rectangle._Base__nb_object = 0

    def tearDown(self):
        """do something after every test"""
        pass