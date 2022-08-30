from AppiumFrameWork.base.BasePage import BasePage


class LoginPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _loginbutton = "com.code2lead.kwad:id/Login"  # id
    _enterEmail = "3"  # index
    _enterPassword = "Enter Password"  # text
    _clickloginButton = "com.code2lead.kwad:id/Btn3"  # id
    _wrongCredentials = "Wrong Credentials"  # text
    _pageTitle = "Enter Admin"  # text
    _enterText = "com.code2lead.kwad:id/Edt_admin"  # id
    _submitButton = "SUBMIT"  # text

    def clickLoginButton(self):
        self.clickElement(self._loginbutton, "id")

    def enterEmail(self, email):
        self.sendText(email, self._enterEmail, "index")

    def enterPassword(self, password):
        self.sendText(password, self._enterPassword, "text")

    def clickOnLoginB(self):
        self.clickElement(self._clickloginButton, "id")

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._pageTitle, "text")
        assert adminScreen == True

    def verifyWrongCrendentialsScreen(self):
        wrongScreen = self.isDisplayed(self._wrongCredentials, "text")
        assert wrongScreen == True

    def enterText(self):
        self.sendText("Code2Lead", self._enterText, "id")

    def clickOnSubmit(self):
        self.clickElement(self._submitButton, "text")
