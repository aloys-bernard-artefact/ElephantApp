import os
import pickle
from datetime import datetime
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    VotingRegressor,
)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np
from data import clean_data




def create__preproc_pipe() -> Pipeline:
    """
    Create a pipeline for preprocessing data, with parrallel processing for
    numeric and categorical features
    return: a pipeline object
    """
    num_preproc_pipe = Pipeline(
        [("Imputer", SimpleImputer(strategy="median")), ("Scaling", StandardScaler())]
    )

    cat_preproc_pipe = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("Encode", OneHotEncoder(drop="first", handle_unknown="ignore")),
        ]
    )
    preproc_pipe = ColumnTransformer(
        [
            (
                "NumPreproc",
                num_preproc_pipe,
                make_column_selector(dtype_include="number"),
            ),
            (
                "CatPreproc",
                cat_preproc_pipe,
                make_column_selector(dtype_include="object"),
            ),
        ]
    )
    return preproc_pipe


def create_model_pipe() -> Pipeline:
    """
    Create  training a model
    return: a pipeline or model object
    """
    return VotingRegressor(
        [
            ("rf", RandomForestRegressor()),
            ("gb", GradientBoostingRegressor()),
        ]
    )


def save_model(model: Pipeline, filename: str) -> None:
    """
    Save the model to the models folder
    """
    if not os.path.exists("models"):
        os.makedirs("models")
    with open(os.path.join("models",filename), "wb") as f:
        pickle.dump(model, f)


def save_metrics(model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> None:
    """
    Save the metrics to the metrics folder
    """
    if not os.path.exists("metrics"):
        os.makedirs("metrics")
        
    # Save the metrics in a csv file 
    # Containing Timestamp, MAE, RMSE, R2
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    metrics = pd.DataFrame({
        "Timestamp": [datetime.now()],
        "MAE": [mae],
        "RMSE": [rmse],
        "R2": [r2]
    })
    # Append the metrics to the metrics.csv file
    if os.path.exists(os.path.join("metrics", "metrics.csv")):
        metrics.to_csv(os.path.join("metrics", "metrics.csv"), mode="a", header=False, index=False)
    else:
        metrics.to_csv(os.path.join("metrics", "metrics.csv"), index=False)
    
    


def load_pipe(filename: str) -> Pipeline:
    """
    Load the model (or Pipeline) from the models folder
    """
    with open(os.path.join("models", filename), "rb") as f:
        return pickle.load(f)


def predict(data: pd.DataFrame, model: Pipeline) -> np.ndarray:
    """
    Make predictions using the trained model

    # WARNING : The data should be preprocessed before making predictions
    EXACTLY like the training data
    """
    data = clean_data(data)
    return model.predict(data)
