import pytest
@pytest.fixture
def sample_data():
    return {"name":"mayur","lname":"baviskar"}


def test_fun(sample_data):
    print(sample_data["name"])
    print(sample_data["lname"])