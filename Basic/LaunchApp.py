from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

# Step 1: Import Appium Service Class
from appium.webdriver.appium_service import AppiumService

# Step 2: Create Object for Appium Service Class
appium_service = AppiumService()

# Step 3: Call start method by using Appium Service class object
appium_service.start()
print(appium_service.is_running)
print(appium_service.is_listening)

# Step 4: Create Desired Capabilities
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '14'
desired_caps['deviceName'] = 'Test'
desired_caps['app'] = ('/Users/mamalkani/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(5)
driver.quit()

# Step 5: Call Stop method by using Appium Service class object
appium_service.stop()