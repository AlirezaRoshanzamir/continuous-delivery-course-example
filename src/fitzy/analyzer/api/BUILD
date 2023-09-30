python_sources(name="python_sources", sources=["**/*.py"])

pex_binary(
    name="pex_binary",
    dependencies=[":python_sources"],
    entry_point="__main__.py",
    execution_mode="venv",
    output_path="fitzy-analyzer-api.pex",
)

docker_image(
    name="docker_image",
    repository="fitzy.analyzer.api",
)
