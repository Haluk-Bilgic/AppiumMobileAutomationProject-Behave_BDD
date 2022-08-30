from AppiumFrameWork.base.BasePage import BasePage


class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _contactFromButton = "com.code2lead.kwad:id/ContactUs"  # id
    _pageTitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "4"  # index number
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFromButton, "id")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pageTitle, "text")
        assert element == True

    def enterName(self, name):
        self.sendText(name, self._enterName, "text")

    def enterEmail(self, mail):
        self.sendText(mail, self._enterEmail, "text")

    def enterAddress(self, address):
        self.sendText(address, self._enterAddress, "text")

    def enterMNumber(self, mNumber):
        self.sendText(mNumber, self._enterMobileNumber, "index")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton, "text")
