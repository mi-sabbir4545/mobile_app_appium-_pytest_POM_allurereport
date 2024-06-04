from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

cap: Dict[str, Any] = {

    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "emulator-5554",
    "appPackage": "com.google.android.apps.nexuslauncher",
    #"appActivity": ".Memorize Quran",
    "app": "D:\\memorize\\Memorize-quran v200-ph2.apk",
    "appium:automationName": "UIAutomator2",
    "appium:ensureWebviewsHavePages": "true",
    "appium:ignoreHiddenApiPolicyError": "true",
    "appium:noReset": "true"

}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

open_app = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Memorize Quran')
open_app.click()

time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@resource-id="com.ilyn.memorizealquran:id/ivNav"]').click()

time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.ilyn.memorizealquran:id/tvSignIn"]').click()

time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.ilyn.memorizealquran:id/tvLogin"]').click()

time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.ilyn.memorizealquran:id/etEmailId"]').send_keys("moinul.islam@byslglobal.com")

time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.ilyn.memorizealquran:id/etLoginPass"]').send_keys("123456")

time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="com.ilyn.memorizealquran:id/laySignUpWithEmail"]').click()

time.sleep(5)

driver.quit()


