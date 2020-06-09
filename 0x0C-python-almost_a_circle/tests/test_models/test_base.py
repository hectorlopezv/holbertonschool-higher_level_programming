"""testing_base_class"""
import unittest
from models.base import Base
import sys
import io


class TestBase(unittest.TestCase):

    """base test for all test"""

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
        self.base_obj = Base()

    def tearDown(self):
        """do something after every test"""
        Base._Base__nb_object = 0

    def test_0(self):
        """test if cls atributte its intialized"""
        self.assertTrue(hasattr(Base, "_Base__nb_object"))

    def test_1(self):
        """test if object type is the correct one"""
        self.assertEqual(str(type(self.base_obj)),
                         "<class 'models.base.Base'>")

    def test_2(self):
        """test correct behavior of constructor"""
        self.assertEqual(self.base_obj.id, 1)

        self.base_obj.id = 4
        self.assertEqual(self.base_obj.id, 4)

    def test_3(self):
        """check for expected error  multiple args"""

        with self.assertRaises(TypeError):
            Base(1, 25)

    def test_4(self):
        """checked for expected error when getting
            class atribute with obj.__nb_object"""
        with self.assertRaises(AttributeError):
            self.base_obj.__nb_object

    """
    def test_pep8_model(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    """


if __name__ == '__main__':
    unittest.main()
