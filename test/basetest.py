import pytest


@pytest.Mark.usesfixture("setup_and_teardown")
class BaseTest:
    pass