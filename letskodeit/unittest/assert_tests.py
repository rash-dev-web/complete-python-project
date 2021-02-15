import unittest


class DemoAssert(unittest.TestCase):

    def test_assert_equals(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, msg="a and b are not equal")

    def test_assert_equals1(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, msg="a and b are not equal")

    def test_assert_true(self):
        a = True
        self.assertTrue(a)

    def test_assert_false(self):
        a = False
        self.assertFalse(a)


if __name__ == "__main__":
    unittest.main(verbosity=2)