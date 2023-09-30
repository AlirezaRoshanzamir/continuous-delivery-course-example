import logging
import os
import subprocess
from typing import Optional

import click

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter("%(asctime)s.%(msecs)02d [%(levelname)s] %(message)s", "%H:%M:%S")
)
logger.addHandler(handler)


@click.group()
def deploy() -> None:
    pass


docker_host_option = click.option(
    "--docker-host",
    "-d",
    default=None,
    help="Where to deploy the application (e.g. ssh://user@remotehost).",
)


@deploy.command()
@docker_host_option
def up(docker_host: Optional[str]) -> None:
    """Deploy Fitzy."""

    is_passed = True
    try:
        subprocess.run(
            [
                "./pants",
                "--filter-target-type=docker_image",
                "publish" if docker_host else "package",
                "::",
            ],
            env={"PANTS_CONCURRENT": "True", **os.environ},
            cwd=os.getcwd(),
            check=True,
        )
        subprocess.run(
            ["docker", "compose", "up", "-d"],
            env={**os.environ, **({"DOCKER_HOST": docker_host} if docker_host else {})},
            cwd=os.getcwd(),
            check=True,
        )
    except subprocess.CalledProcessError as e:
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
        logger.info("Deployment is completed.")
    else:
        logger.error("Deployment is failed.")
        exit(1)


@deploy.command()
@docker_host_option
def down(docker_host: str) -> None:
    """Shutdown Fitzy."""

    is_passed = True
    try:
        subprocess.run(
            ["docker", "compose", "down"],
            env={**os.environ, **({"DOCKER_HOST": docker_host} if docker_host else {})},
            cwd=os.getcwd(),
            check=True,
        )
    except subprocess.CalledProcessError as e:
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
        logger.info("Shutting down is completed.")
    else:
        logger.error("Shutting down is failed.")
        exit(1)


if __name__ == "__main__":
    deploy()
