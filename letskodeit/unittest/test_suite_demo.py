import unittest
from letskodeit.unittest.assert_tests import DemoAssert
from letskodeit.unittest.demo_unittest import DemoUnitTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(DemoAssert)
tc2 = unittest.TestLoader().loadTestsFromTestCase(DemoUnitTest)

smoke_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smoke_test)