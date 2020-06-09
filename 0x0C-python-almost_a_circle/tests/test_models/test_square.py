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
        pass
    def tearDown(self):
        """do something after every test"""
        pass

    def test_size(self):
        """test if size is working"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        s1.size = 10
        self.assertEqual(s1.width, 10)
    
    def test_str(self):
        """test_str"""
        s3 = Square(3, 1, 3)
        self.assertEqual("[Square] (1) 1/3 - 3)",s3.__str__())
        """[Square] (<id>) <x>/<y> - <size>"""
        s2 = Square(2, 2)
        self.assertEqual("[Square] (2) 2/0 - 2)",s2.__str__())
    
    def test_update(self):
        """test update method for Square"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 2)

        s1.update(1, 2, 3)
        self.assertEqual(s1.x, 3)

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.y, 4)

        s1.update(x=12)
        self.assertEqual(s1.x, 12)

        s1.update(size=7, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)

        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)


    
    def test_to_dictionary_square(self):
        """test_to_dictionary_square"""
        s1 = Square(10, 2, 1)
        s1_res = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), s1_res)

        s2 = Square(1, 1)
        s1_res = {'id': 2, 'x': 1, 'size': 1, 'y': 0}
        self.assertEqual(s1.to_dictionary(), s1_res)

        self.assertIsInstance(s1.to_dictionary(), dict)




