python_sources(name="python_sources")

pex_binary(
    name="pex_binary",
    dependencies=[":python_sources"],
    entry_point="__main__.py",
    execution_mode="venv",
    output_path="api.pex",
)
