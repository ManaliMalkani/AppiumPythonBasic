from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
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

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[
    ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

# Tap on ScrollView
scroll_view_btn = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("ScrollView")'))
scroll_view_btn.click()

# Get screen dimensions
size = driver.get_window_size()
width = size["width"]
height = size["height"]

print(f"Screen size: {width}x{height}")

def swipe(start_x, start_y, end_x, end_y):
    finger = PointerInput("touch", "finger1")
    actions = ActionChains(driver, devices=[finger])

    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
    actions.w3c_actions.pointer_action.pointer_up()

    actions.perform()

# Bottom to Top
time.sleep(2)
swipe(width // 2, int(height * 0.8), width // 2, int(height * 0.2))

# Top to Bottom
time.sleep(2)
swipe(width // 2, int(height * 0.2), width // 2, int(height * 0.8))

driver.quit()