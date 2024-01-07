import requests
from flask import Blueprint, abort, render_template, request

from fitzy.portal.helpers import resolve_or_default

blueprint = Blueprint(
    name=__name__.split(".")[-1],
    import_name=__name__,
    url_prefix="/{}".format(__name__.split(".")[-1]),
)


@blueprint.route("/")
def index() -> str:
    """Show the analyses page."""
    return render_template("analyses.html")


@blueprint.route("/", methods=["POST"])
def calculate_bmi() -> str:
    """Calculate the specified analyzation and return the result."""
    form_parameters = dict(request.form)
    analyzation_name = form_parameters["analyzation_name"]
    analyzation_result = None
    if analyzation_name == "bmi":
        response = requests.get(
            "http://{}:6791/bmi/analyze".format(resolve_or_default("analyzer_rest")),
            params={
                "weight": int(form_parameters["weight"]),
                "height": int(form_parameters["height"]),
            },
        )
        response.raise_for_status()
        analyzation_result = response.text

    if analyzation_result is None:
        return abort(404)
    return render_template(
        "analyses.html",
        analyzation_name=analyzation_name,
        analyzation_result=analyzation_result,
    )
