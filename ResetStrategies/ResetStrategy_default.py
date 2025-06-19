from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '14'
desired_caps['deviceName'] = 'Test'
desired_caps['app'] = ('/Users/mamalkani/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

options = UiAutomator2Options().load_capabilities(desired_caps)

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

time.sleep(5)

driver.quit()