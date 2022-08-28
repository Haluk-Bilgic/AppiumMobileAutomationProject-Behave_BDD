from appium import webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['udid'] = 'emulator-5554'
        desired_caps['deviceName'] = 'Pixel 5'
        desired_caps['app'] = ('C://Users//haluk//Downloads//demoApp.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver
