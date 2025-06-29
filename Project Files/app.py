import pickle
import pandas as pd
import numpy as np

import os
from flask import Flask, request, render_template

app = Flask(__name__)


# Load model and scaler
model = pickle.load(open("model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))
columns = pickle.load(open("columns.pkl","rb"))  # Your notebook has X_encoded.columns, save as columns.pkl

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    try:
        # Extract individual inputs by name for clarity
        temp = float(request.form['temp'])
        rain = float(request.form['rain'])
        snow = float(request.form['snow'])
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])
        second = int(request.form['second'])
        holiday = request.form['holiday']
        weather = request.form['weather']

     

        # Initialize input data dictionary with zeros for all columns
        input_dict = {col: 0 for col in columns}

        # Set numerical feature values
        input_dict['temp'] = temp
        input_dict['rain'] = rain
        input_dict['snow'] = snow
        input_dict['year'] = year
        input_dict['month'] = month
        input_dict['day'] = day
        input_dict['hour'] = hour
        input_dict['minute'] = minute
        input_dict['second'] = second

        # Set one-hot encoded categorical features
        holiday_col = f"holiday_{holiday}"
        if holiday_col in input_dict:
            input_dict[holiday_col] = 1

        weather_col = f"weather_{weather}"
        if weather_col in input_dict:
            input_dict[weather_col] = 1

        # Convert to DataFrame with columns in correct order
        data = pd.DataFrame([input_dict])[columns]


        # Scale features
        data_scaled = scaler.transform(data)

        # Predict
        prediction = model.predict(data_scaled)
        output = int(prediction[0])

        return render_template("output.html", prediction_text=f"Estimated Traffic Volume: {output} vehicles")

    except Exception as e:
        print(f"Prediction error: {e}")
        return render_template("output.html", prediction_text="❌ Error in prediction. Check input data and server logs.")

if __name__ == "__main__":
    app.run(debug=True,port=5001)
