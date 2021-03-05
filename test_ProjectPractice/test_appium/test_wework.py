'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_wework.py
@time: 2021/3/5 11:10
@Email: Warron.wang
'''


import time

import pytest
from appium import webdriver   # pip install appium-python-client
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from test_ProjectPractice.test_appium.test_swipe_find import *

class TestSign():
    def setup(self):
        des_caps = {
            "platformName": "android",
            "platformVersion": "6.0.1",

            # 获取appPackage和appActivity最佳命令
            # adb logcat ActivityManager:I | grep "cmp"

            # 通讯录
            # "appPackage":"com.android.contacts",
            # "appActivity":"com.android.contacts.activities.PeopleActivity",

            # 企业微信
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.LaunchSplashActivity",

            # 个人微信
            # "appPackage": "com.tencent.mm",
            # "appActivity": "com.tencent.mm.ui.LauncherUI",

            # qq
            # "appPackage": "om.tencent.mobileqq",
            # "appActivity": "com.tencent.mobileqq.activity.SplashActivity",

            # "deviceName": "T3Q6T16301006992",  # honor：T3Q6T16301006992   #oppo:1b3129a9
            "deviceName": "emulator-5554",  # honor：T3Q6T16301006992   #oppo:1b3129a9
            "noReset": True,  # 去掉页面弹窗，提升云效速度
            "skipServerInstallation": 'true',  # 跳过安装、权限设置等操作(提升app运行速度),
            "skipDeviceInitialization": 'true',
            "settings[waitForIdleTimeout]": 1, # settings 控制 动态页面的等待时长
            'automationName': 'UiAutomator1',
            'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串
            'resetKeyboard': True  # 将键盘隐藏起来
        }
        # 客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_sign(self):
        '''
        前提条件：已登录
        打卡用例：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()
        # 滑动查找  目前是向下滑动两次，再向上查找，知道找到元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print(self.driver.page_source) #打印当前页面结构
        time.sleep(2)
        assert "外出打卡成功" in self.driver.page_source

        # 激活隐式等待
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    @pytest.mark.parametrize("username, mobilephone", [
        ('测试08', '13524631108'),
        ('测试09', '13524631109')
    ])
    def test_address(self, username, mobilephone):
        '''
        前提条件：已登录
        打卡用例：
        1、打开【企业微信】应用
        2、进入【通讯录】
        3、滑动页面查询【添加成员】并点击
        4、点击【手动输入添加】
        5、输入【姓名】、【手机号】，点击【保存】
        6、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滑动查找  目前是向下滑动两次，再向上查找，知道找到元素
        # 方案一
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().text("添加成员").'
        #                                                 'instance(0));').click()
        # 方案二
        Add_locator = (MobileBy.XPATH, "//*[@text='添加成员']")
        swipe_up_search_element(self.driver, Add_locator)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys(username)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(mobilephone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
