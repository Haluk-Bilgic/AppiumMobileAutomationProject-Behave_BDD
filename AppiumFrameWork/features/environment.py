import time
from AppiumFrameWork.base.DriverClass import Driver
import AppiumFrameWork.utilities.CustomLogger as cl

log = cl.customLogger()


def before_all(context):
    log.info("Automation Started")


def before_feature(context, feature):
    log.info("before feature")
    context.driver1 = Driver()
    context.driver = context.driver1.getDriverMethod()


def after_feature(context, feature):
    log.info("after feature")
    time.sleep(5)


def after_all(context):
    log.info("Automation Ended")
    context.driver.close()
