# NYC Taxi Fare Prediction 🚖

This project predicts NYC taxi fares using a machine learning model trained on historical ride data, including geolocation and datetime features. The model ranked in the **top 30% submissions** on Kaggle.

## 📌 Project Overview

- Predicts fare amount based on pickup/dropoff location, passenger count, datetime, and landmark proximity.
- Includes a Flask web app interface for live user input and fare prediction.
- Built with a custom `TaxiFareModel` class for preprocessing and inference.

## 📊 Model

- **Model Type**: XGBoost Regressor (`reg:squarederror`)
- **Evaluation**: Root Mean Squared Error (RMSE)
- **Rank**: Top 30% on Kaggle leaderboard

## 🧠 Key Features

- **Haversine Distance** calculation
- Landmark distances (JFK, LGA, EWR, MET, WTC)
- Datetime feature extraction
- Geolocation via `geopy`
- Custom preprocessing pipeline
- Model wrapped for production use with `joblib`

## 🚀 App Features

- Frontend: HTML + CSS (Bootstrap)
- Backend: Flask
- Inputs: Pickup address, dropoff address, number of passengers
- Output: Predicted fare