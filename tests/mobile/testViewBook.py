import unittest
import os
from appium import webdriver

class TestViewBook(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] =  os.path.abspath(os.path.join(os.path.dirname(__file__),'../../mlbc/platforms/android/ant-build/LibraryBookChecker-debug.apk'))
        print desired_caps['app']
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def testViewBook(self):
        pass


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestViewBook))
unittest.TextTestRunner(verbosity=2).run(suite)