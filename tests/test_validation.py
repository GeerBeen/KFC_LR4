import pytest
from Practise4.app import State
import pytest
from pydantic import ValidationError


def test_valid_state():
    s = State(x=1.0, y=2.0, z=3.0)
    assert s.x == 1.0
    assert s.y == 2.0
    assert s.z == 3.0


def test_missing_field():
    with pytest.raises(ValidationError):
        State(x=1.0, y=2.0)


def test_wrong_type():
    with pytest.raises(ValidationError):
        State(x="abc", y=2.0, z=3.0)


def test_flask_generate_endpoint(client):
    response = client.post("/generate", json={"x": 1.0, "y": 1.0, "z": 1.0})
    assert response.status_code == 200


def test_flask_generate_invalid_data(client):
    response = client.post("/generate", json={"x": "bad", "y": 1.0, "z": 1.0})
    assert response.status_code == 400


if __name__ == '__main__':
    test_valid_state()
    test_missing_field()
    test_wrong_type()
