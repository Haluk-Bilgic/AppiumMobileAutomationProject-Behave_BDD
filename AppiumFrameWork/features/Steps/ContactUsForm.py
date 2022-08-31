from behave import *
from AppiumFrameWork.pages.ContactUsFormPage import ContactForm


@given("Launch the App and Tap on ContactForm Button")
def step_impl(context):
    context.cf = ContactForm(context.driver)
    context.cf.clickContactFormButton()


@when("Verify Contact Page")
def step_impl(context):
    context.cf.verifyContactPage()


@step("Enter {name} Name")
def step_impl(context, name):
    context.cf.enterName(name)


@step("Enter {email} Email")
def step_impl(context, email):
    context.cf.enterEmail(email)


@step("Enter {address} Address")
def step_impl(context, address):
    context.cf.enterAddress(address)


@step("Enter {mNumber} Mobile Number")
def step_impl(context, mNumber):
    context.cf.enterMNumber(mNumber)


@step("Tap on Submit button")
def step_impl(context):
    context.cf.clickSubmitButton()


@then("Take screenshot")
def step_impl(context):
    context.cf.screenShot("final")
