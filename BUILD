python_source(
    name="python_source",
    source="deploy.py",
)

pex_binary(
    name="deploy_pex_binary",
    dependencies=[":python_source"],
    entry_point="deploy.py",
    execution_mode="venv",
    output_path="deploy.pex",
)
