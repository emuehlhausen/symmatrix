import unittest
import SymMatrix

class TestSymMatrix(unittest.TestCase):
    
    def test_onethousand(self):
        N = 1000
        m = SymMatrix.SymMatrix(N)
        
        for x in xrange(N):
            for y in xrange(x, N):
                m[x,y] = x * y
        
        for x in xrange(N):
            for y in xrange(x+1):
                self.assertEqual(m[x,y], m[y,x], "matrix is not symmetric!")
        
        self.assertLessEqual(len(m.data), N*(N+1)/2, "storage is too big!")
        
if __name__ == "__main__":
    unittest.main()