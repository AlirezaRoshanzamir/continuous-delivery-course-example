resources(name="resources", sources=["*.feature"])

python_test_utils(name="python_test_utils")

python_tests(
    name="python_tests",
    dependencies=[":resources", ":python_test_utils"],
    runtime_package_dependencies=["//src/fitzy/analyzer/api:pex_binary"]
)
