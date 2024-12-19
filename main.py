from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

with open('/Users/alexandre/Documents/california_regression/best_regression_model.pkl', 'rb') as f:
    saved_objects = pickle.load(f)

loaded_feature_engineering = saved_objects["pipeline"]
loaded_model = saved_objects["model"]

@app.post('/predict')
async def predict(input_data: InputData):
    X_new = np.array([[
        input_data.MedInc,
        input_data.HouseAge,
        input_data.AveRooms,
        input_data.AveBedrms,
        input_data.Population,
        input_data.AveOccup,
        input_data.Latitude,
        input_data.Longitude
    ]])

    X_new_transformed = loaded_feature_engineering.transform(X_new)

    prediction = loaded_model.predict(X_new_transformed)

    return {"prediction":float(prediction[0])}