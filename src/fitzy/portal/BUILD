resources(name="resources", sources=["**/*.html"])

python_sources(name="python_sources", sources=["**/*.py"])

pex_binary(
    name="pex_binary",
    dependencies=[":resources", ":python_sources"],
    entry_point="__main__.py",
    execution_mode="venv",
    output_path="fitzy-portal.pex",
)

docker_image(
    name="docker_image",
    repository="fitzy.portal",
)
