# Created by sfrog at 2023-02-20
Feature: Amazon search tests

  Scenario: User can search for coffee on Amazon
    Given Open Amazon page
    When Input text coffee
    And Click on search button
    Then Verify that text "coffee" is shown

#  Scenario: User can search for a table on Amazon
#    Given Open Amazon page
#    When Input text table
#    When Click on search button
#    Then Verify that text "table" is shown