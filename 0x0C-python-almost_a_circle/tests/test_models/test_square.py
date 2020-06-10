"""test square py"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout
import pep8


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
        self.assertEqual("[Square] (3) 1/3 - 3", s3.__str__())
        """[Square] (<id>) <x>/<y> - <size>"""
        s2 = Square(2, 2)
        self.assertEqual("[Square] (4) 2/0 - 2", s2.__str__())

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
        s1_res = {'id': 5, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1.to_dictionary(), s1_res)

        s2 = Square(1, 1)
        s1_res = {'id': 6, 'x': 1, 'size': 1, 'y': 0}
        self.assertEqual(s2.to_dictionary(), s1_res)

        self.assertIsInstance(s1.to_dictionary(), dict)

    def test_pep8_model(self):
        """test pepe model"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test(self):
        """testp pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """Test to see if documentation is created and correct"""
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Square, "height"))
        self.assertTrue(Square.height.__doc__)
        self.assertTrue(hasattr(Square, "x"))
        self.assertTrue(Square.x.__doc__)
        self.assertTrue(hasattr(Square, "y"))
        self.assertTrue(Square.y.__doc__)
        self.assertTrue(hasattr(Square, "area"))
        self.assertTrue(Square.area.__doc__)
        self.assertTrue(hasattr(Square, "display"))
        self.assertTrue(Square.display.__doc__)
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(Square.update.__doc__)
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertTrue(Square.to_dictionary.__doc__)
