from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"AAAAAAAAAAAH !! L'elephant": f"barit, cours {os.environ.get('NAME')}, {os.environ.get('OTHERNAME')} te poursuit !!! 😱"}

@app.get("/healthcheck")
def is_alive():
    return {"status": "ok"}


@appp.get("/predict_one")
def predict_one(data: dict):
    """
    Return the prediction for one house
    """
    pass


@app.post("/predict_batch")
def predict_batch(data: dict):
    """
    Return a CSV file with the predictions for a batch of houses
    """
    pass
