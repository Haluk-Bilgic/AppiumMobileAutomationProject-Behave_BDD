from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFrameWork.utilities.CustomLogger as cl
import time


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):

        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorvalue)))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorvalue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorvalue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorvalue)
        except Exception:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " with the locatorValue :" + locatorvalue)

    def clickElement(self, locatorvalue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorvalue, locatorType)
            element.click()
            self.log.info(
                "Clicked on element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue)
        except Exception:
            self.log.info(
                "Unable to click on element with LocatorType: " + locatorType + " with the locatorValue :" + locatorvalue)

    def sendText(self, text, locatorvalue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorvalue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text on element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue)
        except Exception:
            self.log.info(
                "Unable to send text on element with LocatorType: " + locatorType + " with the locatorValue :" + locatorvalue)

    def isDisplayed(self, locatorvalue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorvalue, locatorType)
            element.is_displayed()
            self.log.info(
                "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue + " is displayed")
            return True
        except Exception:
            self.log.info(
                "Element with LocatorType: " + locatorType + " with the locatorValue :" + locatorvalue + " is not displayed")
            return False

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "C:\\Users\\haluk\\PycharmProjects\\HalukStudy\\AppiumFrameWork\\screenshots\\"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path:" + screenshotPath)
        except Exception:
            self.log.info("Unable to Screenshot save to Path:" + screenshotPath)

    def keyCodes(self, value):
        self.driver.press_keycode(value)
