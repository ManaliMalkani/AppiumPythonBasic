import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

def create_driver(device_name, port, system_port):
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "platformVersion": "14",
        "deviceName": device_name,
        "app": "/Users/mamalkani/Downloads/Android_Demo_App.apk",
        "appPackage": "com.code2lead.kwad",
        "appActivity": "com.code2lead.kwad.MainActivity",
        "systemPort": system_port
    }
    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(f'http://127.0.0.1:{port}/wd/hub', options=options)
    return driver

def enter_text(driver):
    time.sleep(2)
    ele = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele.click()
    time.sleep(1)
    input_box = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    input_box.send_keys("Skill2Lead")
    driver.quit()

@pytest.mark.parametrize("device_name,port,system_port", [
    ("emulator-5554", 4723, 8200),
    ("emulator-5556", 4725, 8201)
])
def test_parallel_devices(device_name, port, system_port):
    driver = create_driver(device_name, port, system_port)
    enter_text(driver)
