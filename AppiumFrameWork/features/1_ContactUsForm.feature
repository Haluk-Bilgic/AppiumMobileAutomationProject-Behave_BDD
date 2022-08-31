
  Feature: Fill the Contact Form

      Scenario: User Contact credentials

        Given Launch the App and Tap on ContactForm Button
        When Verify Contact Page
        And Enter Haluk Name
        And Enter abc@gmail.com Email
        And Enter Turkey Address
        And Enter 905654210 Mobile Number
        And Tap on Submit button
        Then Take screenshot