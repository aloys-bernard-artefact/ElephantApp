
import logging
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from data import load_data,clean_data
from modelisation.model import save_model, save_metrics, create__preproc_pipe, create_model_pipe


# TODO : Turn the print into logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def train():
    """ """
    logger.info("Training the model")
    # Load the data
    data = load_data()
    data = clean_data(data)
    preproc = create__preproc_pipe()
    model = create_model_pipe()
    # Split the data into train and test sets
    # TODO :
    y = data.pop("SalePrice")
    x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.2, random_state=42)

    # Fit the model
    x_train_preproc = preproc.fit_transform(x_train)
    model.fit(x_train_preproc, y_train)

    # Evaluate the model
    x_test_preproc = preproc.transform(x_test)

    logger.log(logging.INFO,"Evaluating the model")
    y_pred = model.predict(x_test_preproc)
    mae = mean_absolute_error(y_test, y_pred)
    logger.log(logging.INFO,f"Mean Absolute Error: {mae}")
    logger.log(logging.INFO,"Model trained successfully")

    logger.log(logging.INFO,"Saving the model")
    save_model(model, "model.pkl")
    logger.log(logging.INFO,"✅ Model saved successfully")
    
    logger.log(logging.INFO,"Saving the preprocessor")
    save_model(preproc, "preprocessor.pkl")
    logger.log(logging.INFO,"✅ preprocessor saved successfully")
    
    logger.log(logging.INFO,"Saving the metrics")
    save_metrics(model, x_test_preproc, y_test)

    logger.log(logging.INFO,"✅ Metrics saved successfully")
    
    logger.log(logging.INFO,"✅ Training completed ")

if __name__ == "__main__":
    train()
