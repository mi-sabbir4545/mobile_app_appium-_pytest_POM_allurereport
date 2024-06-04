# memorize-quran-app
Install Andriod Studio
Gradle
Install Node > node --version, npm --version, npx --version
Appium Inspector
npm i appium@next
npm i --location=global appium

npm i -g appium-doctor
appium-doctor –version
appium-doctor –android
appium -p 4724
appium driver install uiautomator2
appium driver install chromium
appium driver list --installed

for real devise:
developer mode on: about phone > tap build number
Developer option > USB debugging on
Turn on developer mode of the device 
Go to the developer option.
1.	Disable Permission Monitoring --> enable it.
2.	 Usb debugging option -> enable it 

First open Appium inspector
Set all capabilities
{
  "platformName": "Android",
  "appium:platformVersion": "14",
  "appium:deviceName": "R3CW20F4HXB",
  "appium:App": "C:\\Users\\user\\Downloads\\DailyDua_Release_V1.0.1_121123(1).apk",
  "appium:automationName": "UIAutomator2",
  "appium:ensureWebviewsHavePages": "true",
  "appium:ignoreHiddenApiPolicyError": "true",
  "appium:noReset": "true"
}
Then open cmd 
Run appium : appium -p 4724
Then Start session from Appium inspector
Then run pycharm python code

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

cap: Dict[str, Any] = {

    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'language': 'en',
    'locale': 'US',

}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.XPATH, value='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout')
el.click()

time.sleep(5)

driver.quit()

