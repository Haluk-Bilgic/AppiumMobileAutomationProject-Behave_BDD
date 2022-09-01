
  Feature: Unable to Login with Wrong Password

      Scenario Outline: User login credentials

        Given Launch the App and Tap on Login Button
        When Enter <email> E-mail
        And Enter <password> Password
        And Tap on login button
        Then Verify Wrong Credentials Screen
        And Return homePage
        Examples:
          |email|password|
          |admin@gmail.com| wrongPassword |
          |wrongEmail@gmail.com  | admin123 |
          |wrongValue| wrongValue |



