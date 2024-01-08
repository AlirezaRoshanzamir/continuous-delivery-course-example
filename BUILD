# remote_environment(
#     name="remote_busybox",
#     platform="linux_x86_64",
#     fallback_environment="local",
# )

# local_environment(
#     name="local",
# )

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
