from flask import Flask

from fitzy.portal.blueprints import about, analyses, home

app = Flask(__name__)
app.register_blueprint(about.blueprint)
app.register_blueprint(analyses.blueprint)
app.register_blueprint(home.blueprint)
