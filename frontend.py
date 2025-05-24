import streamlit as st
import numpy as np
import pickle
import base64

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Page setup
st.set_page_config(page_title="Weather Prediction", layout="centered")

# Set background image using base64 encoding
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(f"""
        <style>
        html, body, .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        label, h1, h2, h3, h4, h5, h6, p, div, span {{
            color: white !important;
        }}
        .custom-container {{
            background: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 10px;
            max-width: 700px;
            margin: 3rem auto;
            box-shadow: 0 0 20px rgba(255,255,255,0.2);
        }}
        </style>
    """, unsafe_allow_html=True)

# Apply background image
set_background("background.jpg")

# Start of main content
st.markdown('<div class="custom-container">', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center;">🌤️ Weather Prediction Dashboard</h1>', unsafe_allow_html=True)

# Input fields
pressure = st.number_input("Pressure (hPa)", value=1013.0)
dewpoint = st.number_input("Dew Point (°C)", value=10.0)
humidity = st.number_input("Humidity (%)", value=75.0)
cloud = st.number_input("Cloud Coverage (%)", value=40.0)
sunshine = st.number_input("Sunshine (hours)", value=5.0)
winddirection = st.number_input("Wind Direction (°)", value=180.0)
windspeed = st.number_input("Wind Speed (km/h)", value=10.0)

# Predict button and result
if st.button("Predict Weather"):
    input_data = np.array([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])
    prediction = model.predict(input_data)
    
    result = "🌧️ Rain is expected." if prediction[0] == 1 else "☀️ No rain expected."
    
    st.markdown(
        f"<div style='text-align:center; font-size:20px; margin-top:20px; font-weight:bold;'>{result}</div>",
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)
