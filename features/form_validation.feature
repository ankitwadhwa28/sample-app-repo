Feature: Form Validation
  As a test automation practitioner
  I want to verify form validation behavior on practice.expandtesting.com
  So that I can ensure required fields are properly validated

  @form_validation @regression
  Scenario: Submit form with all valid data
    Given I am on the form validation page
    When I fill contact name "John Doe"
    And I fill contact number "9876543210"
    And I fill pickup date "2025-12-01"
    And I select payment method "cash on delivery"
    And I submit the form
    Then the form should be submitted successfully

  @form_validation @regression @negative
  Scenario: Submit empty form shows validation errors
    Given I am on the form validation page
    When I submit the form
    Then I should see validation errors

  @form_validation @regression @negative
  Scenario: Submit form with only name filled shows remaining errors
    Given I am on the form validation page
    When I fill contact name "Jane Smith"
    And I submit the form
    Then I should see validation errors
