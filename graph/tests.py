'''
This module contains unit tests
'''

import unittest

# The first several test cases test both the construction of the graphs in
# graph.instances and the functions in graph.invariants.  The beautiful
# thing about this is that the functions that calculate invariants and the
# functions that construct graph instances serve as checks on each other,
# thus effectively testing them both simultaneously.

from instances import *
from invariants import *

G = octahedron()

class OctahedralGraphTestCase (unittest.TestCase):

    def testOrder (self):
        assert (order (G) == 6)

    def testSize (self):
        assert (size (G) == 12)

    def testIsConnected (self):
        assert (is_connected (G))

    def testMinDegree (self):
        assert (minDegree (G) == 4)

    def testMaxDegree (self):
        assert (maxDegree (G) == 4)

    def testIsRegular (self):
        assert (is_regular (G))

    def testDegreeSequence (self):
        assert (list (degreeSequence (G)) == [4, 4, 4, 4, 4, 4] )

    def testIsTree (self):
        assert (not is_tree (G))

    def testIsTriangleFree (self):
        assert (not is_triangleFree (G))

    def testIsComplete (self):
        assert (not is_complete (G))

def suite():
    tests = unittest.TestSuite(OctahedralGraphTestCase)

if __name__ == '__main__':
    unittest.main()
