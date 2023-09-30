import requests
from pytest_bdd import given, scenarios, then, when

scenarios("portal_accessability.feature")


@given("the application is deployed")
def _() -> None:
    pass


@when("opening the portal in the browser", target_fixture="visited_page_content")
def _(deployed_application: dict) -> str:
    response = requests.get(
        "http://{}".format(deployed_application["portal-service-url"])
    )
    response.raise_for_status()
    return response.text


@then("the home page should be visible")
def _(visited_page_content: str) -> None:
    assert "Home" in visited_page_content
    assert "Welcome" in visited_page_content
