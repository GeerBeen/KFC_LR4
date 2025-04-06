from pydantic import BaseModel, ValidationError
from flask import Flask, render_template, request
from Practise4.plot import generate_lorenz_plot
import pytest

app = Flask(__name__)


class State(BaseModel):
    x: float
    y: float
    z: float


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        state = State(**request.json)
        generate_lorenz_plot([state.x, state.y, state.z])
        return "", 200
    except ValidationError as e:
        return str(e), 400


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


if __name__ == '__main__':
    app.run(debug=True)
