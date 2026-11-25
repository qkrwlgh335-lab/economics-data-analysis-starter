import unittest
from examples.demo import demo

class DemoTest(unittest.TestCase):
    def test_synthetic_regression(self):
        n, slope = demo()
        self.assertEqual(n, 240)
        self.assertAlmostEqual(slope, 2.0, delta=0.05)

if __name__ == "__main__":
    unittest.main()
