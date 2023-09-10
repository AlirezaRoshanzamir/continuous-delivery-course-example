import requests
from flask import Blueprint, abort, render_template, request

blueprint = Blueprint(
    name=__name__.split(".")[-1],
    import_name=__name__,
    url_prefix="/{}".format(__name__.split(".")[-1]),
)


@blueprint.route("/")
def index() -> None:
    """Show the analyses page."""
    return render_template("analyses.html")


@blueprint.route("/", methods=["POST"])
def calculate_bmi() -> None:
    """Calculate the specified analyzation and return the result."""
    form_parameters = dict(request.form)
    analyzation_name = form_parameters["analyzation_name"]
    analyzation_result = "Healthy"
    if analyzation_name == "bmi":
        response = requests.get(
            "localhost:6791/bmi/analyze",
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
