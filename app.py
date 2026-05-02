import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD FILES ---------------- #
model = joblib.load("models/logistic/model.pkl")
scaler = joblib.load("models/logistic/scaler.pkl")
features = joblib.load("models/logistic/features.pkl")
kmeans = joblib.load("models/kmeans/kmeans_model.pkl")

# ---------------- TITLE ---------------- #
st.title("📊 Telco Customer Analytics")
st.write("Churn Prediction + Customer Segmentation")

# ---------------- INPUT ---------------- #
st.header("Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (months)", 0, 72)
    monthly = st.number_input("Monthly Charges")
    total = st.number_input("Total Charges")

    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["Yes","No"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])

    phoneservice = st.selectbox("Phone Service", ["Yes", "No"])
    multiplelines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

with col2:
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    onlinesecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    onlinebackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    deviceprotection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    techsupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

    streamingtv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streamingmovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])

# ---------------- DATAFRAME ---------------- #
input_dict = {
    'tenure': tenure,
    'MonthlyCharges': monthly,
    'TotalCharges': total,
    'gender': gender,
    'SeniorCitizen': senior,
    'Partner': partner,
    'Dependents': dependents,
    'PhoneService': phoneservice,
    'MultipleLines': multiplelines,
    'InternetService': internet,
    'OnlineSecurity': onlinesecurity,
    'OnlineBackup': onlinebackup,
    'DeviceProtection': deviceprotection,
    'TechSupport': techsupport,
    'StreamingTV': streamingtv,
    'StreamingMovies': streamingmovies,
    'Contract': contract,
    'PaperlessBilling': paperless,
    'PaymentMethod': payment
}

input_df = pd.DataFrame([input_dict])

# ---------------- ENCODING ---------------- #
input_df = pd.get_dummies(input_df)

for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[features]

# ---------------- SCALING ---------------- #
input_scaled = scaler.transform(input_df)

# ---------------- PREDICTION ---------------- #
if st.button("🔍 Analyze Customer"):

    # Churn prediction
    prob = model.predict_proba(input_scaled)[0][1]
    pred = 1 if prob > 0.4 else 0

    # Clustering
    cluster = kmeans.predict(input_scaled)[0]

    # Correct mapping based on your results
    cluster_map = {
        1: "🔴 High Risk (32% churn)",
        0: "🟡 Medium Risk (24% churn)",
        2: "🟢 Loyal Customer (7% churn)"
    }

    segment = cluster_map[cluster]

    # ---------------- OUTPUT ---------------- #
    st.subheader("📢 Results")

    # Churn
    if pred == 1:
        st.error(f"⚠️ High Risk of Churn ({prob:.2f})")
    else:
        st.success(f"✅ Low Risk of Churn ({prob:.2f})")

    # Segment
    st.info(f"Customer Segment: {segment}")

    # ---------------- BUSINESS INSIGHTS ---------------- #
    st.subheader("💡 Business Recommendation")

    if cluster == 1:
        st.write("👉 Offer discounts, retention plans, or proactive support.")
    elif cluster == 0:
        st.write("👉 Monitor customer behavior and engage with offers.")
    else:
        st.write("👉 Loyal customer – focus on upselling and premium services.")

    # ---------------- EXTRA ---------------- #
    st.subheader("📊 Model Confidence")
    st.write(f"Churn Probability: {prob:.2%}")