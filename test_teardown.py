import pytest

@pytest.fixture
def lifecycle_fixture():
    print("\n[setup]")
    yield
    print("\n[teardown]")

def test_first_action(lifecycle_fixture):
    assert True

def test_second_action(lifecycle_fixture):
    assert True