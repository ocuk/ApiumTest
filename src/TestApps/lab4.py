import unittest

# import your test modules
import login
import rmacc
import setup
import teardown

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite

suite.addTests(loader.loadTestsFromModule(setup))
suite.addTests(loader.loadTestsFromModule(login))
suite.addTests(loader.loadTestsFromModule(rmacc))
suite.addTests(loader.loadTestsFromModule(teardown))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)