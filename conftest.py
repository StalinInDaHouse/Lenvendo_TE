import pytest
from Application.BaseApp import App


@pytest.fixture(scope="session")
def my_fixture():
    app = App()
    yield app
    app.session_kill()
