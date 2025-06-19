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

# Scroll and click on DRAGANDDROP option
drag_text = wait.until(lambda x: x.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'
))
drag_text.click()

# Source and destination elements
source = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw"))
target = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2"))

# Coordinates
start_x = source.location['x'] + source.size['width'] // 2
start_y = source.location['y'] + source.size['height'] // 2
end_x = target.location['x'] + target.size['width'] // 2
end_y = target.location['y'] + target.size['height'] // 2

# Create W3C Touch Actions
touch = PointerInput(POINTER_TOUCH, "finger")
actions = ActionChains(driver)
actions.w3c_actions = ActionChains(driver).w3c_actions  # get fresh builder

# Add pointer input actions
actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.2)
actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
actions.w3c_actions.pointer_action.release()

# Perform the gesture
actions.perform()

time.sleep(4)
driver.quit()
