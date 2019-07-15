from appium import webdriver


def get_phone_driver(pac, act):
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'emulator-5554'
    # app的信息
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    # 中文输入
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
    # 获取toast消息支持
    desired_caps['automationName'] = 'Uiautomator2'
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
