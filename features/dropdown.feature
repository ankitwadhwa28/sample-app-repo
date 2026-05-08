Feature: Dropdown
  As a test automation practitioner
  I want to interact with dropdown menus on practice.expandtesting.com
  So that I can verify dropdown selection behavior

  @dropdown @regression
  Scenario Outline: Select from the simple dropdown
    Given I am on the dropdown page
    When I select "<option>" from the dropdown
    Then the selected option should be "<option>"

    Examples:
      | option   |
      | Option 1 |
      | Option 2 |

  @dropdown @regression
  Scenario: Select a country from the country dropdown
    Given I am on the dropdown page
    When I select country "India"
    Then the selected country should be "India"

  @dropdown @regression
  Scenario: Change dropdown selection
    Given I am on the dropdown page
    When I select "Option 1" from the dropdown
    And I select "Option 2" from the dropdown
    Then the selected option should be "Option 2"
