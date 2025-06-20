from AppiumFramework.base.DriverClass import Driver
import AppiumFramework.utilities.CustomLogger as cl
from AppiumFramework.base.BasePage import BasePage
# py.test -v -s Test_ContactUsForm.py
#pytest -v -s tests/Test_ContactUsForm.py --alluredir=../reports/allureReports
# pytest -v -s AppiumFramework/tests/Test_ContactUsForm.py --alluredir=../AppiumFramework/reports/allureReports
#allure generate ../AppiumFramework/reports/allureReports -o ../AppiumFramework/reports/allureResults --clean
#allure open ../AppiumFramework/reports/allureResults
#allure serve ../AppiumFramework/reports/allureReports

import unittest
import pytest
from AppiumFramework.pages.ContactUsFormPage import ContactForm
import AppiumFramework.utilities.CustomLogger as cl

""""
# Step 1: Create Driver instance
driver_obj = Driver()

# Step 2: Get the actual Appium driver (this is the important fix)
driver = driver_obj.getDriverMethod()

# Step 3: Pass the actual driver to BasePage
#bp = BasePage(driver)




# Step 4: Log app launch
log = cl.customLogger()
log.info("Launch APP")
bp.screenShot("App")



# Step 5: Wait and click the element
element = bp.isDisplayed("com.code2lead.kwad:id/ContactUs", "id")
print(element)
bp.clickElement("com.code2lead.kwad:id/ContactUs", "id")
bp.sendText("code2lead","Enter Name","text")

bp.screenShot("code2Lead")


cf = ContactForm(driver)
cf.clickContactFormButton()
cf.verifyContactPage()
cf.enterName()
cf.enterEmail()
cf.enterAddress()
cf.enterMNumber()
cf.clickSubmitButton()
"""

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class Test_ContactUsForm(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.order(2)
    def test_enterDataInForm(self):
        self. cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.order(1)
    def test_opencontactForm(self):
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
