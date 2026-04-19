import streamlit as st
import pandas as pd
import joblib

# Load
model = joblib.load("models/logistic/model.pkl")
scaler = joblib.load("models/logistic/scaler.pkl")
features = joblib.load("models/logistic/features.pkl")
kmeans = joblib.load("models/kmeans/kmeans.pkl")

st.title("📊 Telco Customer Analytics")
st.write("Predict Churn + Customer Segmentation")

# ---------------- INPUTS ---------------- #
st.header("Enter Customer Details")

tenure = st.slider("Tenure (months)", 0, 72)
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
gender = st.selectbox("Gender", ["Male", "Female"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

# ---------------- CREATE INPUT DATA ---------------- #
input_dict = {
    'tenure': tenure,
    'MonthlyCharges': monthly,
    'TotalCharges': total,
    'Contract': contract,
    'gender': gender,
    'Partner': partner,
    'Dependents': dependents
}

input_df = pd.DataFrame([input_dict])

# ---------------- ENCODING ---------------- #
input_df = pd.get_dummies(input_df)

# Match training columns
for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[features]

# ---------------- SCALING ---------------- #
input_scaled = scaler.transform(input_df)

# ---------------- PREDICTION ---------------- #
if st.button("Analyze Customer"):

    # 🔹 Churn Prediction
    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    # 🔹 Customer Segmentation
    cluster = kmeans.predict(input_scaled)[0]

    st.subheader("📢 Results")

    # Churn Result
    if pred == 1:
        st.error(f"⚠️ Customer likely to churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer likely to stay (Probability: {prob:.2f})")

    # Segmentation Result
    cluster_map = {
        0: "🔴 High Risk Customer",
        1: "🟢 Loyal Customer",
        2: "🟡 Medium Risk Customer"
    }

    st.info(f"Customer Segment: {cluster_map[cluster]}")

    # ---------------- BUSINESS INSIGHTS ---------------- #
    st.subheader("Business Suggestion")

    if cluster == 0:
        st.write("👉 Offer discounts, retention calls, or special plans.")
    elif cluster == 1:
        st.write("👉 Upsell premium services and maintain satisfaction.")
    else:
        st.write("👉 Monitor behavior and provide targeted offers.")