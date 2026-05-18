# 🚕 Taxi Trip Pricing Prediction

A Machine Learning project that predicts taxi trip fares based on trip details such as distance, duration, passenger count, traffic conditions, and location data.

## 📌 Project Overview

Taxi pricing depends on multiple factors like trip distance, time, passenger count, traffic, and demand.

This project uses Machine Learning Regression algorithms to predict taxi trip prices accurately.

### Objectives
- Analyze taxi trip pricing data
- Perform data preprocessing and feature engineering
- Train regression models
- Evaluate model performance
- Build a deployable prediction system

---

## 📂 Dataset

Dataset used:
**taxi_trip_pricing.csv**

Features may include:
- Trip Distance
- Trip Duration
- Passenger Count
- Pickup Location
- Dropoff Location
- Time of Day
- Traffic Conditions
- Weather Conditions
- Base Fare
- Additional Charges

Target Variable:
- **Trip Price / Fare Amount**

---

## 🛠 Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle / Joblib
- Streamlit

---

## 🤖 Machine Learning Models Used

Regression algorithms:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor (optional)

Best model selected based on performance metrics.

---

## 📊 Project Workflow

### 1. Data Collection
Load taxi trip dataset.

### 2. Data Preprocessing
- Handle missing values
- Remove duplicates
- Fix incorrect data types

### 3. Exploratory Data Analysis (EDA)
Visualize:
- Fare distribution
- Distance vs Price
- Traffic impact
- Time-based pricing trends

### 4. Feature Engineering
- Encoding categorical columns
- Feature scaling
- Creating derived features

### 5. Train-Test Split
Split dataset into training and testing sets.

### 6. Model Training
Train regression models.

### 7. Model Evaluation
Evaluate using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### 8. Model Saving
Save trained model using pickle/joblib.

### 9. Deployment
Deploy using Streamlit.

---

## 📁 Project Structure

```bash
taxi-trip-pricing-prediction/
│
├── taxi_trip_pricing.csv
├── notebook.ipynb
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
