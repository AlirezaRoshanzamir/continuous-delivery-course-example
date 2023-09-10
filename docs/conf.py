# -- Project information -----------------------------------------------------
project = "Fitzy"
version = "0.1.0"
copyright = "Alireza Roshanzamir"
author = "Alireza Roshanzamir"
language = "en"

# -- Extensions --------------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx_autodoc_defaultargs",
    "sphinx_rtd_theme",
    "sphinx_paramlinks",
    "sphinx.ext.viewcode",
    "sphinx_markdown_builder",
    "sphinx.ext.inheritance_diagram",
    "jupyter_sphinx",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.autohttp.flask",
    "sphinxcontrib.autohttp.flaskqref",
]

# General options ------------------------------------------------------------
nitpicky = True
nitpick_ignore = [
    # For more information, see nitpick common exception list.
    ("py:class", "module"),
]
add_module_names = False
rst_prolog = ""

# Options for HTML output ----------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_permalinks_icon = "<small>🔗</small>"

# Options for sphinx.ext.intersphinx -----------------------------------------
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# Options for sphinx.ext.autodoc ---------------------------------------------
autodoc_default_options = {
    "show-inheritance": True,
    "members": True,
    # See https://github.com/zwang123/sphinx-autodoc-defaultargs/issues/3
    "exclude-members": "with_traceback",
}
autodoc_member_order = "bysource"

# Options for sphinx_autodoc_defaultargs -------------------------------------
rst_prolog += (
    """
.. |default| raw:: html

    <div class="default-value-section">"""
    + " <span class='default-value-label'>Default:</span>"
)

# Options for sphinx_autodoc_typehints ---------------------------------------
set_type_checking_flag = False

# Options for sphinx.ext.inheritance_diagram ---------------------------------
inheritance_graph_attrs = {"rankdir": "TD"}
