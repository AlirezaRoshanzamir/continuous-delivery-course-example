from typing import Generator, Literal

import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--deployed-host",
        action="store",
        default="localhost",
        help="If the application is already deployed, determine its location.",
    )
    parser.addoption(
        "--deploy", action="store_true", help="Whether or not deploy the application."
    )
    parser.addoption(
        "--deployment-args",
        action="store_true",
        help="Arguments passed to the deployment script.",
    )
    parser.addoption(
        "--reuse-deployment",
        action="store_true",
        help="Whether or not reuse the deployed application for all of the tests.",
    )


def deployed_application_scope(
    fixture_name: str, config: pytest.Config
) -> Literal["session", "function"]:
    if config.getoption("--reuse-deployment", False):
        return "session"
    return "function"


@pytest.fixture(scope=deployed_application_scope)
def deployed_application(request: pytest.FixtureRequest) -> Generator[dict, None, None]:
    # Setup
    deploy = request.config.getoption("--deploy", False)

    if deploy:
        raise NotImplementedError(
            "The application deployment in the tests has not been implemented yet. It"
            " should be accomplished by executing the deployment script."
        )
    else:
        host = request.config.getoption("--deployed-host")

    yield {
        "api-service-url": "{}:6791".format(host),
        "portal-service-url": "{}:6792".format(host),
    }

    # Teardown
    if deploy:
        raise NotImplementedError(
            "The application shutdown in the tests has not been implemented yet. It"
            " should be accomplished by executing the deployment script."
        )
