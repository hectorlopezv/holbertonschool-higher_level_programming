"""testing_base_class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):

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
        Rectangle._Base__nb_object = 0

    def tearDown(self):
        """do something after every test"""
        pass

    def test_id(self):
        """test_id"""
        Rectangle._Base__nb_object = 0
        self.assertEqual(Rectangle(1, 1).id, 1)
        self.assertEqual(Rectangle(1, 1).id, 2)
        obj_temp = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj_temp.id, 5)
        self.assertEqual(Rectangle(1, 1).id, 3)

    def test_istance(self):
        """test if rectangle is rectanglee and if recta chiild of base"""
        self.assertIsInstance(Rectangle(1, 1), Rectangle)
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_miss_arg(self):
        """test for misssing arguments"""
        with self.assertRaises(TypeError):
            temp_obj = Rectangle()

        with self.assertRaises(TypeError):
            temp_obj = Rectangle(1)

    def test_correct_init(self):
        """test for correct attributes"""
        dict_rect =  {'_Rectangle__height': 5, '_Rectangle__width': 10,
        '_Rectangle__x': 0, 
        '_Rectangle__y': 0, 
        'id': 1}

        self.assertEqual(Rectangle(10, 5).__dict__, dict_rect)

    def test_correct_methods(self):
        """test_correct_methods"""
        x = inspect.getmembers(Rectangle, inspect.ismethod)
        self.assertEqual(x, [])

    def test_area(self):
        """Test_area method"""
        self.assertEqual(Rectangle(2, 2).area(), 4)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display_0(self):
        """test display"""
        file_dup = io.StringIO()
        obj_temp = Rectangle(4, 6)
        res = '####\n####\n####\n####\n####\n####\n'
        with redirect_stdout(file_dup):
            obj_temp.display()
        self.assertEqual(res, file_dup.getvalue())

    def test_display_1(self):
        """test_display"""
        r = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()

        s = """\
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\




#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

    def test_str(self):
        """test string representation of Rectangle"""
        res_1 = """[Rectangle] (12) 2/1 - 4/6"""
        self.assertEqual(Rectangle(4, 6, 2, 1, 12).__str__(), res_1)

        res_1 = """[Rectangle] (1) 1/0 - 5/5"""
        self.assertEqual(Rectangle(5, 5, 1).__str__(), res_1)

        res_1 = """[Rectangle] (12) 0/0 - 8/7"""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).__str__(), res_1)

    def test_input_integer(self):
        """test_expected error to happen"""
        with self.assertRaises(TypeError) as e:
            Rectangle(2.5, 1)
        err = e.exception
        self.assertEqual(err.args[0], "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(1, '2')
        err = e.exception
        self.assertEqual(err.args[0], "height must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, (1, '2'))
        err = e.exception
        self.assertEqual(err.args[0], "x must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, [1, 2])
        err = e.exception
        self.assertEqual(err.args[0], "y must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, dict(k=2), 4)
        err = e.exception
        self.assertEqual(err.args[0], "y must be an integer")

    def test_update_0(self):
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_update_1(self):
        """test for cases in which  kwargs is skipped because args exist"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.y, 1)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.height, 2)

    def test_err_conditions(self):
        """test edge cases on valid input"""

        with self.assertRaises(ValueError) as e:
            Rectangle(0, 0)
        err = e.exception

        self.assertEqual(err.args[0], "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        err = e.exception
        self.assertEqual(err.args[0], "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        err = e.exception
        self.assertEqual(err.args[0], "height must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -1, -1)
        err = e.exception
        self.assertEqual(err.args[0], "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 1, -1)
        err = e.exception
        self.assertEqual(err.args[0], "y must be >= 0")
    
    def test_to_dictionary(self):
        """test for to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_resu = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), r1_resu)

        r1 = Rectangle(14, 5, 1, 1)
        r1_resu = {'x': 1, 'y': 1, 'id': 2, 'height': 5, 'width': 14}
        self.assertEqual(r1.to_dictionary(), r1_resu)
    
    
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

      def test_documentation(self):
        """Test to see if documentation is created and correct"""
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)


if __name__ == '__main__':
    unittest.main()
