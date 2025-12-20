import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ===============================
# Page config
# ===============================
st.set_page_config(
    page_title="🚕 Taxi Price Prediction",
    page_icon="🚕",
    layout="wide"
)

# ===============================
# Load model
# ===============================
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# ===============================
# Title
# ===============================
st.markdown(
    """
    <h1 style='text-align:center; color:#ff4b4b;'>
    🚖 Taxi Trip Price Predictor
    </h1>
    <p style='text-align:center;'>
    Predict taxi fare using Machine Learning models
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ===============================
# Sidebar Inputs
# ===============================
st.sidebar.header("📝 Trip Details")

trip_distance = st.sidebar.slider("Trip Distance (km)", 1.0, 1000.0, 100.0)
passengers = st.sidebar.selectbox("Passenger Count", [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
trip_duration = st.sidebar.slider("Trip Duration (minutes)", 1.0, 1000.0, 50.0)

base_fare = st.sidebar.number_input("Base Fare", 1.0, 1000.0, 5.0)
per_km_rate = st.sidebar.number_input("Per KM Rate", 0.1, 1000.0, 10.0)
per_min_rate = st.sidebar.number_input("Per Minute Rate", 0.1, 2000.0, 10.3)

time_of_day = st.sidebar.selectbox(
    "Time of Day",
    ["Morning", "Evening", "Night"]
)

day_of_week = st.sidebar.selectbox(
    "Day of Week",
    ["Weekday", "Weekend"]
)

traffic = st.sidebar.selectbox(
    "Traffic Conditions",
    ["Low", "Medium", "High"]
)

weather = st.sidebar.selectbox(
    "Weather",
    ["Clear", "Rain", "Snow"]
)

# ===============================
# Encode categorical (same as training)
# ===============================
data = {
    "Trip_Distance_km": trip_distance,
    "Passenger_Count": passengers,
    "Base_Fare": base_fare,
    "Per_Km_Rate": per_km_rate,
    "Per_Minute_Rate": per_min_rate,
    "Trip_Duration_Minutes": trip_duration,

    # "Time_of_Day_Evening": 1 if time_of_day == "Evening" else 0,
    # "Time_of_Day_Morning": 1 if time_of_day == "Morning" else 0,
    # "Time_of_Day_Night": 1 if time_of_day == "Night" else 0,

    # "Day_of_Week_Weekend": 1 if day_of_week == "Weekend" else 0,

    # "Traffic_Conditions_Low": 1 if traffic == "Low" else 0,
    # "Traffic_Conditions_Medium": 1 if traffic == "Medium" else 0,

    # "Weather_Rain": 1 if weather == "Rain" else 0,
    # "Weather_Snow": 1 if weather == "Snow" else 0,
}

input_df = pd.DataFrame([data])

# ===============================
# Prediction
# ===============================
st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Input Summary")
    st.dataframe(input_df, use_container_width=True)

with col2:
    if st.button("🚀 Predict Price"):
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Trip Price: ₹ {prediction:.2f}")

# ===============================
# Footer
# ===============================
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray;'>
    Built with ❤️ using Streamlit & Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)




