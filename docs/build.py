import logging
import os
import subprocess
import sys
from os.path import join
from subprocess import CalledProcessError

import click

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter("%(asctime)s.%(msecs)02d [%(levelname)s] %(message)s", "%H:%M:%S")
)
logger.addHandler(handler)


@click.command()
@click.option(
    "--auto",
    "-a",
    is_flag=True,
    help=(
        "Rebuild the documents on change automatically. Also, serve the docs on"
        " localhost:8000."
    ),
)
def build(auto: bool) -> None:
    """Build the documents."""

    logger.info("Building documents:")

    is_passed = True
    try:
        python_path = join(sys.prefix, "bin", "python3")
        cwd = os.getcwd()
        env = {**os.environ, "PYTHONPATH": ":".join(sys.path[1:])}

        build_command_module = "sphinx"
        command_dependent_args = []
        if auto:
            build_command_module = "sphinx_autobuild"
            command_dependent_args = ["--host", "0.0.0.0"]

        args = [
            python_path,
            "-m",
            build_command_module,
            "-W",
            *command_dependent_args,
            "docs/",
            "dist/docs/html/",
        ]

        subprocess.run(args, env=env, cwd=cwd, check=True)

    except CalledProcessError as e:
        is_passed = False
        logger.error(
            'Executing command "{}" failed:\n'
            "======== Exit code ========\n{}\n"
            "======== Stdout ========\n{}\n"
            "======== Stderr ========\n{}\n".format(
                " ".join(e.cmd),
                e.returncode,
                e.stdout.decode() if e.stdout else "Empty!",
                e.stderr.decode() if e.stderr else "Empty!",
            )
        )

    if is_passed:
        logger.info("Building documentations completed.")
    else:
        logger.error("Building documentations failed.")
        exit(1)


if __name__ == "__main__":
    build()
