from fastapi import FastAPI
import uvicorn
import joblib
import numpy as np

app = FastAPI(debug=True)


@app.get('/')
def home():
    return {'text': 'Titanic Survival Prediction'}


@app.get('/predict')
def predict(Age: int, Gender: int, Passenger_class: int, Fare_Amount: int):

    features = np.array([[Age, Gender, Passenger_class, Fare_Amount]])
    model = joblib.load('titanic_rf_model.pkl')

    predictions = model.predict(features)
    if predictions == 0:
        return {"This Person did not survive the Titanic Crash"}
    elif predictions == 1:
        return {"This Person Survived the Titanic Crash"}


if __name__ == '__main__':
    uvicorn.run(app)
