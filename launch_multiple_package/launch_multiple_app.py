from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

# Setup desired capabilities
desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "14",
    "deviceName": "Test",
    "app": "/Users/mamalkani/Downloads/Android_Demo_App.apk",
    "appPackage": "com.code2lead.kwad",
    "appActivity": "com.code2lead.kwad.MainActivity",
    "noReset": True
}

# Load capabilities
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# Wait for app to load
time.sleep(2)

# Interact with a UI element from your app
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

# Switch to Settings app
print("Switching to Settings...")
driver.activate_app("com.android.settings")
time.sleep(3)

# Switch back to your app
print("Switching back to kwad app...")
driver.activate_app("com.code2lead.kwad")
time.sleep(3)


# Optionally close Settings
print("Closing Settings app...")
driver.terminate_app("com.android.settings")

# End session
time.sleep(2)
driver.quit()
