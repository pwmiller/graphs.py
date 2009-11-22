'''
This module contains unit tests
'''

# The following is to keep pylint from complaining needlessly about
# "method could be a function," missing docstrings, or wildcard imports.
# Normally, these would be things to consider fixing, but for this
# specific module, the method names tell exactly what the tests are
# testing, and wildcard imports are no problem because the domain of
# this module is \emph{strictly} graph-theoretical (hence no need to
# worry about future namespace pollution).

# pylint: disable-msg=R0201
# pylint: disable-msg=C0111
# pylint: disable-msg=W0401

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

    # The following is to stop pylint from complaining about "too many
    # public methods":

    # pylint: disable-msg = R0904

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

    def testEigenvalues (self):
        eigenvals = eigenvalues (G)

        # The octahedron has eigenvalues $-2$, $0$, and $4$, with
        # respective multiplicties $2$, $3$, and $1$.

        assert (sorted (eigenvals.keys()) == [-2, 0, 4])
        assert (eigenvals [-2] == 2)
        assert (eigenvals [0]  == 3)
        assert (eigenvals [4]  == 1)

def suite():
    tests = unittest.TestSuite(OctahedralGraphTestCase)

if __name__ == '__main__':
    unittest.main()
