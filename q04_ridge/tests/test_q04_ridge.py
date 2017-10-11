import numpy as np
from unittest import TestCase
from ..build import ridge
from inspect import getargspec

np.random.seed(9)


class TestRidge(TestCase):
    def test_ridge(self):

        # Input parameters tests
        args = getargspec(ridge)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))
        self.assertEqual(args[3], (0.01,), "Expected default values do not match given default values")

        # Return type tests
        rmse1, rmse2 = ridge(0.01)
        self.assertIsInstance(rmse1, float,
                              "Expected data type for return value is `float`, you are returning %s" % (
                                  type(rmse1)))
        self.assertIsInstance(rmse2, float,
                              "Expected data type for return value is `float`, you are returning %s" % (
                                  type(rmse2)))

        # Return value tests
        self.assertAlmostEqual(rmse1, 33775.6544815, places=3)
        self.assertAlmostEqual(rmse2, 37702.0033295, places=3)
