# Continuous Delivery Course Example
This is an example repository where some practices of the [Continuous Delivery Course](http://alirezaroshanzamir.github.io/continuous-delivery-course) are demonstrated.

## Status
[![Commit Stage](https://github.com/AlirezaRoshanzamir/continuous-delivery-course-example/actions/workflows/commit.yml/badge.svg)](https://github.com/AlirezaRoshanzamir/continuous-delivery-course-example/actions/workflows/commit.yml) [![Acceptane Test Stage](https://github.com/AlirezaRoshanzamir/continuous-delivery-course-example/actions/workflows/acceptance.yml/badge.svg)](https://github.com/AlirezaRoshanzamir/continuous-delivery-course-example/actions/workflows/acceptance.yml)

## Build Tools and Software Stack
The following programming languages and tools are used in this repository:

- Programming and Scripting Language: [Python](https://www.python.org), [Bash](https://www.gnu.org/software/bash/)
- Web Framework: [FastAPI](https://fastapi.tiangolo.com), [Flask](https://flask.palletsprojects.com/)
- Web Server: [Uvicorn](https://www.uvicorn.org/), [gevent](http://www.gevent.org)
- Documentation: [SphinX](https://www.sphinx-doc.org), [reStructuredText](https://docutils.sourceforge.io/rst.html), [Swagger](https://swagger.io)
- Build System and Monorepo Tool: [Pants](https://www.pantsbuild.org)
- Packaging, Dependency Management, and Pinning: [Pex](https://pex.readthedocs.io/)
- Unit and Acceptance Testing: [Pytest](https://pytest.org/), [Pytest-BDD](https://pytest-bdd.readthedocs.io)
- Static Analysis and Formatter: [Flake8](https://flake8.pycqa.org/), [isort](https://pycqa.github.io/isort), [Mypy](https://mypy.readthedocs.io/), [Autoflake](https://github.com/fsouza/autoflake8), [ShellCheck](https://www.shellcheck.net), [Shfmt](https://webinstall.dev/shfmt)
- Virtualization and Container Orchestration: [Docker](https://www.docker.com), [Docker Compose](https://docs.docker.com/compose)
- Pipeline: [GitHub Actions](https://github.com/features/actions)

## Commands
You can perform common tasks on the repository as follows:

| Command | Description |
| ------- | ----------- |
| `./pants lint ::` | Run all the linters on all the files. |
| `./pants check ::` | Run all the checkers (e.g. Mypy) on all the files. |
| `./pants package ::` | Build and generate packages (e.g. Pex, Docker image, etc.) and place the results in the `dist/` directory. |
| `./pants run docs/build.py` | Build the documents and place the results in the `dist/` directory. |
| `./pants run docs/build.py -- --auto` | Build the documents and start a live reload server. |
| `./pants test tests/unit` | Run the unit tests. |
| `./pants test tests/acceptance` | Run the acceptance tests. |
| `./pants generate-lockfiles ::` | Generate lockfiles for the thirdparty requirements. |
| `./pants run src/fitzy/analyzer/api:pex_binary` | Run the Analyzer RestAPI service. |
| `./pants run src/fitzy/analyzer/api:docker_image` | Run the Analyzer RestAPI service using the Docker container. |
| `./pants run src/fitzy/portal:pex_binary` | Run the Portal web application. |
| `./pants run src/fitzy/portal:docker_image` | Run the Portal web apllication using the Docker container. |
| `docker compose up` | Start the application using the packaged Docker images. |
| `docker compose down` | Shut-down the started application. |
| `./pants run deploy.py` | Deploy and start the application on the specified server. |
