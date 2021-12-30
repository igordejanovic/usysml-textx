import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--update-outputs", action="store_true", default=False,
        help="Update .sysml outputs"
    )


@pytest.fixture
def update(request):
    return request.config.getoption("--update-outputs")
