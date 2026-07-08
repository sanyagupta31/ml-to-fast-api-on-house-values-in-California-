# California Housing Price API

This project trains a machine learning model on the California housing dataset and exposes it through a FastAPI service.

## What it does
- Trains a Random Forest regressor on the California housing dataset
- Saves the trained model to a joblib file
- Serves predictions through a FastAPI API

## Files
- `train.py` — trains and saves the model
- `main.py` — loads the model and exposes the API
- `california_housing_model.joblib` — trained model artifact

## Requirements
Install the required packages:

```bash
pip install fastapi uvicorn scikit-learn pandas joblib requests
```

## Run training
```bash
python train.py
```

## Run the API
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Then open:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

## API endpoint
### POST /predict
Send a JSON body like:

```json
{
  "MedInc": 8.3252,
  "AveRooms": 6.9841,
  "AveBedrms": 1.0238,
  "Population": 322,
  "HouseAge": 41
}
```

Response:

```json
{
  "predicted_median_house_value": 206855.0
}
```
