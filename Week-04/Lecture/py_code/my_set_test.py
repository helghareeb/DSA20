# بسم الله الرحمن الرحيم

import unittest
from my_set import MySet

class TestMySum(unittest.TestCase):
    
    def setUp(self):
        self.a_courses = MySet()
        self.a_courses.add( "CSCI-112" )
        self.a_courses.add( "MATH-121" )
        self.a_courses.add( "HIST-340" )
        self.a_courses.add( "ECON-101" )

        self.h_courses = MySet()
        self.h_courses.add( "POL-101" )
        self.h_courses.add( "ANTH-230" )
        self.h_courses.add( "CSCI-112" )
        self.h_courses.add( "ECON-101" )

        self.c_courses = MySet()
        self.c_courses.add( "CSCI-112" )
        self.c_courses.add( "MATH-121" )
        self.c_courses.add( "HIST-340" )
        self.c_courses.add( "ECON-101" )

    def test_a_courses_names(self):
        self.assertTrue('CSCI-112' in self.a_courses)
        self.assertTrue('MATH-121' in self.a_courses)
        self.assertTrue('HIST-340' in self.a_courses)
        self.assertIn('ECON-101', self.a_courses)
        self.assertNotIn('CSCI-', self.a_courses)
        self.assertNotIn('MATH-21', self.a_courses)
        self.assertNotIn('HIST-30', self.a_courses)
        self.assertNotIn('ECON-11', self.a_courses)

    def test_a_b_equality(self):
        self.assertNotEqual(self.a_courses, self.h_courses)

    def test_a_c_equality(self):
        self.assertEqual(self.a_courses, self.c_courses)

    def test_sets_length(self):
        self.assertEqual(len(self.a_courses), 4)
        self.assertEqual(len(self.h_courses), 4)
        self.c_courses.add('test')
        self.assertEqual(len(self.c_courses), 5)

    def test_a_h_taking_same_courses(self):
        self.assertEqual(len(self.a_courses.intersect(self.h_courses)), 2)


    def test_h_courses(self):
        pass

    def tearDown():
        pass

if __name__ == '__main__':
    unittest.main()