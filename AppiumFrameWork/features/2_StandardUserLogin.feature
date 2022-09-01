
  Feature: Login with standard user

      Scenario: User login credentials

        Given Launch the App and Tap on Login Button
        When Enter admin@gmail.com E-mail
        And Enter admin123 Password
        And Tap on login button
        Then Verify Admin Screen

