from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="California Housing Price Prediction API", description="An API to predict California housing prices using a trained Random Forest model.", version="1.0.0")
model = joblib.load('california_housing_model.joblib')


class HouseFeatures(BaseModel):
    MedInc: float
    AveRooms: float
    AveBedrms: float
    Population: float
    HouseAge: float

    class Config:
        schema_extra = {
            "example": {
                "MedInc": 8.3252,
                "AveRooms": 6.9841,
                "AveBedrms": 1.0238,
                "Population": 322,
                "HouseAge": 41
            }
        }


@app.get("/")
def read_root():
    """Root endpoint providing basic information about the API."""
    return {"message": "Welcome to the California Housing Price Prediction API. Use the /predict endpoint to get predictions."}


@app.post("/predict")
def predict_price(features: HouseFeatures):
    """Predicts the median house value based on the provided features."""
    input_data = pd.DataFrame([features.dict()])
    prediction = model.predict(input_data)
    predicted_value = float(prediction[0])
    return {"predicted_median_house_value": predicted_value}