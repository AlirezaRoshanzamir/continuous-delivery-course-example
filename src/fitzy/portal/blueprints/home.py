from flask import Blueprint, render_template

blueprint = Blueprint(
    name=__name__.split(".")[-1], import_name=__name__, url_prefix="/"
)


@blueprint.route("/")
def index() -> None:
    """Show the home page."""
    return render_template("home.html")
