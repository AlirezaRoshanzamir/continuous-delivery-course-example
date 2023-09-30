Feature: Analyses
    Scenario Outline: BMI Analysis
        Given I am in the Analyses page
        When I analyze my BMI with <weight> kg and <height> cm
        Then I should receive the <bmi_analyzation> result

        Examples:
        | weight | height | bmi_analyzation |
        |   40   |  180   |   UNDERWEIGHT   |
        |   74   |  176   |     HEALTHY     |
        |   90   |  176   |   OVERWEIGHT    |
