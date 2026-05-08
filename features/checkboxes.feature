Feature: Checkboxes
  As a test automation practitioner
  I want to interact with checkboxes on practice.expandtesting.com
  So that I can verify checkbox state changes work correctly

  @checkboxes @regression
  Scenario: Verify both checkboxes start unchecked
    Given I am on the checkboxes page
    Then both checkboxes should be unchecked

  @checkboxes @regression
  Scenario: Check the first checkbox
    Given I am on the checkboxes page
    When I check checkbox 1
    Then checkbox 1 should be checked

  @checkboxes @regression
  Scenario: Toggle checkbox state check then uncheck
    Given I am on the checkboxes page
    When I check checkbox 2
    And I uncheck checkbox 2
    Then checkbox 2 should be unchecked

  @checkboxes @regression
  Scenario: Check all checkboxes
    Given I am on the checkboxes page
    When I check checkbox 1
    And I check checkbox 2
    Then checkbox 1 should be checked
    And checkbox 2 should be checked
