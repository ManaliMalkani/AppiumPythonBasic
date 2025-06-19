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

ele_xpath = driver.find_element(AppiumBy.XPATH,
                                '//android.widget.Button[@content-desc="Btn1"]')  # By using xpath and Con-des
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]') Xpath and Res-id
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ENTER SOME VALUE"]') Xpath and text
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[3]') xpath and Index value
ele_xpath.click()

time.sleep(2)

ele_xpath2 = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
ele_xpath2.send_keys("Skill2lead.com")

driver.quit()