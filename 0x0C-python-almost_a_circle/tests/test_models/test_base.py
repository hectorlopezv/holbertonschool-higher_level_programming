"""testing_base_class"""
import unittest
from models.base import Base
import sys
import io
from models.rectangle import Rectangle


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

    def test_load_from_file(self):

        """load from file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_input:
            print("[{}] {}".format(id(rect), rect))

        print("---")

        for rect in list_rectangles_output:
            print("[{}] {}".format(id(rect), rect))

        print("---")
        print("---")
        self.assertIsNot(r1, list_rectangles_output[0])
        self.assertIsNot(r2, list_rectangles_output[1])


        self.assertEqual(r1.__str__(), list_rectangles_output[0].__str__())
        self.assertEqual(r2.__str__(), list_rectangles_output[1].__str__())

    def test_create_base(self):

        """Test create base"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)
        resu_str = '[Rectangle] (1) 1/0 - 3/5'
        self.assertEqual(r2.__str__(), resu_str)
        self.assertIsNot(r1, r2)
    
    def test_json_string_to_dictionary(self):

        """json_string_to_dictionary"""
        
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        resu_expected = [{'height': 4, 'width': 10, 'id': 89}, 
        {'height': 7, 'width': 1, 'id': 7}]
        self.assertEqual(list_output, resu_expected)
    
    def test_json_string_to_file(self):
        """json_String_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        resu_ = None
        resu_expected = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, 
        {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        
        with open("Rectangle.json", 'r') as f:
            resu = file.read()

        self.assertEqual(resu, resu_expected)

    def test_dict_to_json_base(self):
        """dictionary to json string """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        r1_res = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(json_dictionary, r1)

        self.assertIsInstance(json_dictionary, str)


   
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
