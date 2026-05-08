Feature: Radio Buttons
  As a test automation practitioner
  I want to interact with radio buttons on practice.expandtesting.com
  So that I can verify single-selection behavior within groups

  @radio_buttons @regression
  Scenario: Select a favorite color
    Given I am on the radio buttons page
    When I select color "blue"
    Then color "blue" should be selected

  @radio_buttons @regression
  Scenario: Select a favorite sport
    Given I am on the radio buttons page
    When I select sport "football"
    Then sport "football" should be selected

  @radio_buttons @regression
  Scenario: Change color selection within the group
    Given I am on the radio buttons page
    When I select color "blue"
    And I select color "red"
    Then color "red" should be selected
    And color "blue" should not be selected

  @radio_buttons @regression
  Scenario: Select both a color and a sport independently
    Given I am on the radio buttons page
    When I select color "green"
    And I select sport "basketball"
    Then color "green" should be selected
    And sport "basketball" should be selected
