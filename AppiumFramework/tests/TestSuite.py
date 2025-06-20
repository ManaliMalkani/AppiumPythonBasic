#pytest -v -s AppiumFramework/tests/TestSuite.py --alluredir=../AppiumFramework/reports/allureReports
# 1. Import the files
import  unittest
from AppiumFramework.tests.Test_login import Test_login
from AppiumFramework.tests.Test_ContactUsForm import Test_ContactUsForm



# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(Test_ContactUsForm)
gt = unittest.TestLoader().loadTestsFromTestCase(Test_login)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf,gt])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

