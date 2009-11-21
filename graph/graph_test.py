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

def ASSERT (expr, msg=''):
    if not expr:
        raise unittest.failureException, msg

G = octahedron()

class OctahedralGraphTestCase (unittest.TestCase):

    def testOrder (self):
        ASSERT (order (G) == 6)

    def testSize (self):
        ASSERT (size (G) == 12)

    def testIsConnected (self):
        ASSERT (is_connected (G))

    def testMinDegree (self):
        ASSERT (minDegree (G) == 4)

    def testMaxDegree (self):
        ASSERT (maxDegree (G) == 4)

    def testIsRegular (self):
        ASSERT (is_regular (G))

    def testDegreeSequence (self):
        ASSERT (list (degreeSequence (G)) == [4, 4, 4, 4, 4, 4] )

    def testIsTree (self):
        ASSERT (not is_tree (G))

    def testIsTriangleFree (self):
        ASSERT (not is_triangleFree (G))

    def testIsComplete (self):
        ASSERT (not is_complete (G))

def suite():
    tests = unittest.TestSuite(OctahedralGraphTestCase)

if __name__ == '__main__':
    unittest.main()
