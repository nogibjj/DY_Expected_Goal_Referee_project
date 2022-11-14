# test fastapi-app.py
from fastapi import FastAPI

def test_fastapi_app():
    app = FastAPI()
    assert app