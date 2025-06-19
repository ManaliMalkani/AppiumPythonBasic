from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
import time

# Desired Capabilities
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14',
    'deviceName': 'Test',
    'app': '/Users/mamalkani/Downloads/Android_Demo_App.apk',
    'appPackage': 'com.code2lead.kwad',
    'appActivity': 'com.code2lead.kwad.MainActivity',
    'fullReset': True
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("TAB ACTIVITY")'))
ele.click()

######Right to Left#######
hometab = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'textContains("Home")'))
time.sleep(5)
driver.execute_script("mobile: swipeGesture", {'elementId': hometab, 'direction': 'left', "percent": 0.98})

time.sleep(5)
###### Left to Right    #######
sporttab = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'textContains("Sport")'))

driver.execute_script("mobile: swipeGesture", {'elementId': sporttab, 'direction': 'right', "percent": 0.98})
