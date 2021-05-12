# the plan is to have a class encapsulating a 'point'
# x and y values will define a point on a plane
# we will derive the hypotenuse
# the point can declare it's current position
# we can move the point by delta-x and delta-y (moveBy) NB default to zero
# The Point class should keep a count of how many instances exist

import unittest
# we will also need to import our Point class
from my_points import Point

class testPoint(unittest.TestCase):
    # setup before each test is run
    def setUp(self):
        # we need to create a fresh point for use by each test
        self.point = Point(3,5)

    # we declare our tests here (as part of this test suite)
    def testMoveByA(self):
        '''Test the moveBy method with +ve x and y values'''
        self.point.moveBy(5,2)
        # make an assertion
        self.assertEqual(self.point.display(), (8, 7))
    def testMoveByB(self):
        '''Test the moveBy method with -ve x and y values'''
        self.point.moveBy(-5,-2)
        # make an assertion
        self.assertEqual(self.point.display(), (-2, 3))
    def testMoveByC(self):
        '''Test the moveBy method with only x value (default y)'''
        self.point.moveBy(dy=9)
        # make an assertion
        self.assertEqual(self.point.display(), (3, 14))
    def testPointCounter(self):
        '''Test that we can accurately count the number of instances'''
        self.assertGreater(Point.points, 0)
    def testHypot(self):
        '''Derive the hypotenuse from x and y'''
        self.point.moveBy(0,-1) # leaves us at (3,4)
        r = self.point.hypot()
        self.assertAlmostEqual(r, 5.00, places=2)
    def testPosi_neg_hypot_equal(self):
        '''the hypot for +ve x and y should equal that of -ve x and y'''
        self.pos_h = Point(3,4)
        self.neg_h = Point(-3, -4)
        self.assertAlmostEqual( self.pos_h.hypot(), self.neg_h.hypot(), places=2 )
    def testStringValueFails(self):
        '''if x or y ar entered as strings, we should raise an exception'''
        with self.assertRaises(TypeError):
            Point('3', 4)

if __name__ == '__main__':
    # run our unit tests
    unittest.main()