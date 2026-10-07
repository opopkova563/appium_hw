import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    options = UiAutomator2Options()

    options.set_capability("platformName", "Android")
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability("appium:deviceName", "Android")
    options.set_capability("appium:appPackage", "com.csdroid.pkg")
    options.set_capability(
        "appium:appActivity",
        "com.csdroid.pkg.MainActivity",
    )

    android_driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options,
    )

    yield android_driver
    android_driver.quit()