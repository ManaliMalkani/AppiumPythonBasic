from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time
import pytest


@pytest.mark.flaky(reruns=5)
def test_runAppiumTest():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '14'
    desired_caps['deviceName'] = 'Test'
    desired_caps['app'] = ('/Users/mamalkani/Downloads/Android_Demo_App.apk')
    desired_caps['appPackage'] = 'com.code2lead.kwad'
    desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

    options = UiAutomator2Options().load_capabilities(desired_caps)

    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValu")
    ele_id.click()

    time.sleep(5)
    driver.quit()

