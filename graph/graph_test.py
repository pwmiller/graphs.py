'''
This module contains unit tests only.
'''
import unittest
import instances
import invariants

class OctahedralGraphTestCase (unittest.TestCase):
    def setUp (self):
	self.G = instances.octahedron()

    def testOrder (self):
	self.failUnless (invariants.order (self.G) == 6)

    def testSize (self):
	self.failUnless (invariants.size (self.G) == 12)
	
    def testIsConnected (self):
	self.failUnless (invariants.is_connected (self.G))

    def testIsRegular (self):
	self.failUnless (invariants.is_regular (self.G))

    def testDegreeSequence (self):
	self.failUnless (list (invariants.degreeSequence (self.G)) == \
			 [4, 4, 4, 4, 4, 4] )

    def testIsTree (self):
	self.failIf (invariants.is_tree (self.G))

    def testIsTriangleFree (self):
	self.failIf (invariants.is_triangleFree (self.G))

    def testIsComplete (self):
	self.failIf (invariants.is_complete (self.G))
	
def suite():
    tests = unittest.TestSuite(OctahedralGraphTestCase)
    
if __name__ == '__main__':
    unittest.main()
    
