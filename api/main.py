import os
from fastapi import FastAPI
import pandas as pd
from modelisation.model import predict,load_pipe
from modelisation.data import clean_data  

app = FastAPI()

@app.get("/")
def read_root():
    return {"AAAAAAAAAAAH !! L'elephant": f"barit, cours {os.environ.get('NAME')}, {os.environ.get('OTHERNAME')} te poursuit !!! 😱"}

@app.get("/healthcheck")
def is_alive():
    return {"status": "ok"}


@app.post("/predict_one")
def predict_one(data: dict):
    """
    Return the prediction for one house
    """
    # Convert the values to int and float when possible
    
    for key in data.keys():
        try:
            data[key] = float(data[key])
        except:
            pass

    
    data = {key: [value] for key, value in data.items()}

    df = (pd.DataFrame(data))
    df_clean = clean_data(df)
    
    preproc = load_pipe("preprocessor.pkl")
    model = load_pipe("model.pkl")
    
    df_preproc = pd.DataFrame(preproc.transform(df_clean),columns=preproc.get_feature_names_out())
    prediction = model.predict(df_preproc)
    return {"prediction": prediction[0]}
    
    

@app.post("/predict_batch")
def predict_batch():
    """
    Return a CSV file with the predictions for a batch of houses
    """
    pass
