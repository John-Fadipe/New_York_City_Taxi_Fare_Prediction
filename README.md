# 🗽 New York City Taxi Fare Prediction

This project involves building a machine learning model to predict NYC taxi fares based on various ride-related features such as date, time, location, and passenger count.

📊 **Dataset**: [NYC Taxi Fare Prediction - Kaggle](https://www.kaggle.com/competitions/new-york-city-taxi-fare-prediction/data)

---

## 🚀 Tech Stack & Tools

- **Languages**: Python  
- **Libraries**: `Scikit-learn`, `NumPy`, `Pandas`  
- **Models Used**:
  - Linear Regression  
  - Ridge Regression  
  - Random Forest  
  - Gradient Boosting  

- **Framework**: Flask (for API deployment)  
- **Hosting**: Render  

---

## ⚙️ Key Processes

- **Data Preprocessing**: Handled missing values, removed outliers, and processed geographic coordinates.
- **Feature Engineering**: 
  - Extracted datetime features (hour, day of week, etc.)
  - Calculated haversine distance between pickup and dropoff.
- **Model Training**: Trained and evaluated various regression models using RMSE.
- **Deployment**: 
  - Built a Flask API to serve the trained model.
  - Deployed on [Render](####) for live access.