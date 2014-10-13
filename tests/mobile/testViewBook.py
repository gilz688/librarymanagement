import unittest
import os
from appium import webdriver

class TestViewBook(unittest.TestCase):
    @classmethod
    def setUpClass(self):
    	desired_caps = {}
    	desired_caps['platformName'] = 'Android'
    	desired_caps['deviceName'] = 'Android Emulator'
    	desired_caps['app'] = os.path.abspath('./applications/librarymanagement/mlbc/platforms/android/ant-build/LibraryBookChecker-debug.apk')
    	self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
    	return None
        
    def testViewBook(self):
        pass

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestViewBook))
unittest.TextTestRunner(verbosity=2).run(suite)