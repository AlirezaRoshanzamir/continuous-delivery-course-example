from flask import Blueprint, render_template

blueprint = Blueprint(
    name=__name__.split(".")[-1],
    import_name=__name__,
    url_prefix="/{}".format(__name__.split(".")[-1]),
)


@blueprint.route("/")
def index() -> str:
    """Show the about page."""
    return render_template("about.html")
