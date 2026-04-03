import streamlit as st
import numpy as np
import pickle
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ---------- TITLE ----------
st.title("🏠 House Price Prediction App")
st.write("Enter the details of the house to predict its price")

# ---------- LOAD MODEL SAFELY ----------
if not os.path.exists("house_model.pkl") or not os.path.exists("imputer.pkl"):
    st.error("❌ Model or imputer not found. Run train_model.py first!")
    st.stop()

with open("house_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("imputer.pkl", "rb") as f:
    imputer = pickle.load(f)

# ---------- INPUT SECTION ----------
st.subheader("📋 House Details")

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=0, max_value=10, value=2)

with col2:
    area = st.number_input("Area (sqft)", min_value=100, max_value=10000, value=1500)

# ---------- ENCODING ----------
def encode_input():
    return np.array([[bedrooms, bathrooms, area]])

# ---------- PREDICTION ----------
if st.button("🔍 Predict House Price"):
    try:
        data = encode_input()
        data = imputer.transform(data)  # handle missing values
        result = model.predict(data)
        st.success(f"🏡 Predicted House Price: ${result[0]:,.2f}")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# ---------- FOOTER ----------
st.markdown("---")
st.write("Made with ❤️ using Streamlit")