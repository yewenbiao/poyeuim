from appium import webdriver
def get_driver(appPackage,appActivity):
    # server 启动参数
    desired_caps = {}
    # 设备信息 android不区分大小写
    desired_caps['platformName'] = 'Android'
    # 要和你自己测试手机版本对应上
    desired_caps['platformVersion'] = '5.1'
    # 设备名称值Android是可以随意写的
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 输入中文的配置参数
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # app信息
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity
    # 理解成是 手机的大管家
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)