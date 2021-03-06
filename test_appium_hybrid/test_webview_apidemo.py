'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_webview_apidemo.py
@time: 2021/2/23 17:52
@Email: Warron.wang
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestBrowser():
    def setup(self):
        des_caps = {
            "platformName": "android",
            "platformVersion": "6.0.1",
            "appPackage":"io.appium.android.apis",
            "appActivity":"io.appium.android.apis.ApiDemos",
            # "browserName": "Browser",  # 被测浏览器
            "deviceName": "emulator-5554",
            "noReset": True,  # 去掉页面弹窗，提升云效速度
            "chromedriverExecutable": "/Users/xmly/Documents/chromedriver20"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        #滑动验证
        webview = "WebView"
        print(self.driver.contexts) # 打印下上下文
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}").'
                                                        'instance(0));').click()
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "i has no focus").send_keys("this is a test string")
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "i am a link").click()
        # print(self.driver.page_source)

        print(self.driver.contexts) # 打印下上下文

        # 切换最后一个上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, "i_am_a_textbox").send_keys("this is a test string use chrome inspect")
        self.driver.find_element(MobileBy.ID, "i am a link").click()
        print(self.driver.page_source)


