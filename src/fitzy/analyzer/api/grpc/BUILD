protobuf_sources(name="protobuf_sources", sources=["**/*.proto"], grpc=True)

python_sources(name="python_sources", sources=["**/*.py"])

pex_binary(
    name="pex_binary",
    dependencies=[":python_sources"],
    entry_point="__main__.py",
    output_path="fitzy-analyzer-api-grpc.pex",
    execution_mode="venv",
)

docker_image(
    name="docker_image",
    repository="fitzy.analyzer.api.grpc",
    dependencies=[":pex_binary"],
)
