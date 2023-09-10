files(name="rst_files", sources=["**/*.rst"])

python_sources(
    name="build_python_sources",
    dependencies=[
        # These dependencies are used at runtime, so should be explicitly stated.
        "//src/fitzy/analyzer/api:python_sources",
        "//src/fitzy/analyzer/core:python_sources",
        "//src/fitzy/portal:python_sources",
        "//thirdparty:python_requirements#sphinx-autobuild",
        "//thirdparty:python_requirements#jupyter-sphinx",
        "//thirdparty:python_requirements#sphinx",
        "//thirdparty:python_requirements#sphinx-autobuild",
        "//thirdparty:python_requirements#sphinx-autodocgen",
        "//thirdparty:python_requirements#sphinx-autodoc-typehints",
        "//thirdparty:python_requirements#sphinx-autodoc-defaultargs",
        "//thirdparty:python_requirements#sphinx-copybutton",
        "//thirdparty:python_requirements#sphinx-paramlinks",
        "//thirdparty:python_requirements#sphinx-rtd-theme",
        "//thirdparty:python_requirements#sphinx-toolbox",
        "//thirdparty:python_requirements#sphinxcontrib-httpdomain",
    ],
    sources=[
        "build.py",
        "conf.py",
    ],
)

pex_binary(
    name="build_pex_binary",
    dependencies=[
        ":build_python_sources",
    ],
    entry_point="build.py",
    execution_mode="venv",
    output_path="build_docs.pex",
)
