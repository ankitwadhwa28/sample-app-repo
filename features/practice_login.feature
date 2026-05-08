Feature: Practice Login Page
  As a test automation practitioner
  I want to verify the login functionality on practice.expandtesting.com
  So that I can ensure authentication flows work correctly

  Background:
    Given I am on the practice login page

  @practice_login @regression
  Scenario: Successful login with valid credentials
    When I login with username "practice" and password "SuperSecretPassword!"
    Then I should be redirected to the secure page
    And I should see flash message "You logged into a secure area!"

  @practice_login @regression @negative
  Scenario: Login with invalid username
    When I login with username "invalid_user" and password "SuperSecretPassword!"
    Then I should see flash message "Your username is invalid!"

  @practice_login @regression @negative
  Scenario: Login with invalid password
    When I login with username "practice" and password "wrong_password"
    Then I should see flash message "Your password is invalid!"
