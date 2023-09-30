import requests
from pytest_bdd import given, scenarios, then, when
from pytest_bdd.parsers import parse

scenarios("analyses.feature")


@given("I am in the Analyses page")
def _() -> None:
    pass


@when(
    parse("I analyze my BMI with {weight:d} kg and {height:d} cm"),
    target_fixture="response",
)
def _(deployed_application: dict, weight: int, height: int) -> str:
    response = requests.post(
        "http://{}/analyses".format(deployed_application["portal-service-url"]),
        data={
            "analyzation_name": "bmi",
            "weight": weight,
            "height": height,
        },
    )
    response.raise_for_status()
    return response.text


@then(parse("I should receive the {bmi_analyzation} result"))
def _(response: str, bmi_analyzation: str) -> None:
    assert bmi_analyzation in response
