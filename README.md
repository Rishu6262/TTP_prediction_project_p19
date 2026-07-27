# 🚕 Taxi Trip Pricing Prediction System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-success)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

An **End-to-End Machine Learning Regression** project that predicts **Taxi Trip Prices** based on trip-related information such as **distance, duration, passenger count, pickup and drop-off locations, traffic conditions, weather conditions, and travel time**. The project demonstrates the practical application of **Data Analytics**, **Machine Learning**, **Feature Engineering**, and **Interactive Web Deployment** to solve a real-world transportation pricing problem.

---

# 📌 Project Overview

The **Taxi Trip Pricing Prediction System** is designed to estimate taxi fares using historical trip data and machine learning regression techniques. The application analyzes multiple trip-related factors—including **distance traveled**, **trip duration**, **passenger count**, **traffic conditions**, **weather conditions**, **pickup and drop-off locations**, and **time of day**—to accurately predict the expected fare.

Before model training, the dataset undergoes comprehensive **data cleaning**, **data preprocessing**, **feature engineering**, and **exploratory data analysis (EDA)** to improve data quality and prediction performance. Multiple regression algorithms are trained, evaluated, and compared to identify the best-performing model.

The final model can be deployed as an interactive **Streamlit web application** or integrated with a **FastAPI REST API**, allowing users to enter trip details and receive instant fare predictions through a user-friendly interface.

---

## 🎯 Project Objectives

The primary objective of this project is to develop an intelligent **Machine Learning Regression** system capable of accurately predicting taxi trip fares based on various trip-related factors. The project focuses on applying data analytics and predictive modeling techniques to improve fare estimation and support data-driven decision-making in the transportation industry.

### Key Objectives

- 🚕 Analyze historical taxi trip data to identify pricing patterns and trends.
- 🧹 Perform comprehensive data cleaning, preprocessing, and feature engineering.
- 📊 Conduct Exploratory Data Analysis (EDA) to understand the relationship between trip features and fare prices.
- 🤖 Train and compare multiple Machine Learning regression algorithms.
- 📏 Evaluate model performance using MAE, MSE, RMSE, and R² Score.
- 💾 Save the best-performing model for future predictions using Pickle.
- 🌐 Develop an interactive Streamlit application for real-time fare prediction.
- 🚀 Build a deployment-ready end-to-end Machine Learning solution.
- 💼 Strengthen practical skills in Python, Data Analytics, Machine Learning, and Model Deployment through a real-world transportation pricing use case.

---

# 📂 Dataset Information

The project uses the **Taxi Trip Pricing Dataset**, which contains historical taxi trip records and fare information. The dataset is used to train and evaluate machine learning regression models for accurate taxi fare prediction.

## 📊 Dataset Summary

| Attribute | Details |
|-----------|---------|
| 📂 Dataset Name | Taxi Trip Pricing Dataset |
| 📄 File Name | `taxi_trip_pricing.csv` |
| 🎯 Target Variable | Trip Price / Fare Amount |
| 📚 Dataset Type | Structured Tabular Dataset |
| 🚕 Domain | Transportation Analytics / Fare Prediction |

---

## 📋 Dataset Features

| Feature | Description |
|---------|-------------|
| 🚕 Trip Distance | Total distance traveled during the trip |
| ⏱️ Trip Duration | Total travel time from pickup to drop-off |
| 👥 Passenger Count | Number of passengers in the trip |
| 📍 Pickup Location | Starting location of the journey |
| 🏁 Drop-off Location | Destination of the journey |
| 🕒 Time of Day | Time when the trip was taken |
| 🚦 Traffic Conditions | Traffic intensity during the trip |
| 🌦️ Weather Conditions | Weather at the time of travel |
| 💵 Base Fare | Initial fare before additional charges |
| ➕ Additional Charges | Extra charges such as tolls or surge pricing |
| 💰 Trip Price | Final taxi fare (Target Variable) |

---

## 🎯 Dataset Importance

This dataset provides valuable insights into the factors affecting taxi fares and serves as an excellent resource for building regression models. It enables developers and data scientists to practice **data preprocessing**, **exploratory data analysis (EDA)**, **feature engineering**, **regression modeling**, and **predictive analytics** using real-world transportation data.
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
