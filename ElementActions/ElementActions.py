from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '14'
desired_caps['deviceName'] = 'Test'
desired_caps['app'] = ('/Users/mamalkani/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps[f'appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps['fullReset'] = True

options = UiAutomator2Options().load_capabilities(desired_caps)

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Text on the Button ", ele_id.text)
print("Text on the Button ", ele_id.get_attribute("text"))
print("Content Des  of the Button ", ele_id.get_attribute("content-desc"))
ele_id.click()

time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Skill2Lead")
time.sleep(2)
ele_classname.clear()
time.sleep(2)
ele_classname.send_keys("Skill2Lead")

time.sleep(2)
driver.quit()