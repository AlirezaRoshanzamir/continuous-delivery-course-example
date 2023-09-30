Feature: Portal Accessability
    @smoke
    Scenario Outline: Check if the Portal Home Page is Accessible
        Given the application is deployed
        When opening the portal in the browser
        Then the home page should be visible
