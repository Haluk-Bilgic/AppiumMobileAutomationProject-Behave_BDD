from behave import *
from AppiumFrameWork.pages.LoginPage import LoginPageTest


@given("Launch the App and Tap on Login Button")
def step_impl(context):
    context.lp = LoginPageTest(context.driver)
    context.lp.clickLoginButton()


@when("Enter {email} E-mail")
def step_impl(context, email):
    context.lp.enterEmail(email)


@step("Enter {password} Password")
def step_impl(context, password):
    context.lp.enterPassword(password)


@step("Tap on login button")
def step_impl(context):
    context.lp.clickOnLoginB()


@then("Verify Wrong Credentials Screen")
def step_impl(context):
    context.lp.verifyWrongCrendentialsScreen()


@then("Return homePage")
def step_impl(context):
    context.lp.keyCodes(4)


@then("Verify Admin Screen")
def step_impl(context):
    context.lp.verifyAdminScreen()
