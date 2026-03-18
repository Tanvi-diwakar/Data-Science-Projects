import streamlit as st
import pandas as pd
import numpy as np
import joblib

kmeans = joblib.load("customer_segmentation_kmeans.pkl")
scaler = joblib.load("customer_segmentation_scaler.pkl")

st.title("Customer Segmentation and Retention Analysis")
st.write("This app allows you to input customer data and predicts the customer segment using a pre-trained KMeans model.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income", min_value=0,max_value=200000, value=50000)
total_spent = st.number_input("Total Amount Spent", min_value=0, max_value=100000, value=1000)
num_web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=100, value=5)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=100, value=3)
num_web_visits = st.number_input("Number of Web Visits", min_value=0, max_value=100, value=10)
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)

input_data  = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Total_spending": [total_spent],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency]
})

if st.button("Predict Customer Segment"):

    try:
        input_scaled = scaler.transform(input_data)
        cluster = kmeans.predict(input_scaled)[0]

        # 🔥 ADDED THIS PART
        cluster_labels = {
            0: "💤 Low Value Customer",
            1: "💰 High Value Customer",
            2: "🛍️ Regular Customer"
        }

        st.success(f"🎯 Customer Segment: {cluster_labels.get(cluster, 'Unknown')}")

    except Exception as e:
        st.error(f"Error: {e}")