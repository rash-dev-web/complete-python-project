import unittest


class DemoUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("once before all tests")

    def setUp(self):
        print("Before every test..")

    def test_method_a(self):
        print("method A")

    def test_method_b(self):
        print("method B")

    def tearDown(self):
        print("After every test...")

    @classmethod
    def tearDownClass(cls):
        print("once after all tests")


if __name__ == "__main__":
    unittest.main(verbosity=2)
