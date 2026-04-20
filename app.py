import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD MODELS ---------------- #
model = joblib.load("models/logistic/model.pkl")
scaler = joblib.load("models/logistic/scaler.pkl")
features = joblib.load("models/logistic/features.pkl")
kmeans = joblib.load("models/kmeans/kmeans.pkl")

# ---------------- TITLE ---------------- #
st.title("📊 Telco Customer Analytics Dashboard")
st.write("Predict Customer Churn & Segment Customers")

# ---------------- INPUT SECTION ---------------- #
st.header("Enter Customer Details")

# Layout for better UI
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

# ---------------- CREATE INPUT DATA ---------------- #
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

# Match training features
for col in features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[features]

# ---------------- SCALING ---------------- #
input_scaled = scaler.transform(input_df)

# ---------------- PREDICTION ---------------- #
if st.button("🔍 Analyze Customer"):

    # Churn Prediction
    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    # Customer Segmentation
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
    st.subheader("💡 Business Recommendations")

    if cluster == 0:
        st.write("👉 Offer discounts, retention campaigns, or special plans.")
    elif cluster == 1:
        st.write("👉 Upsell premium services and maintain satisfaction.")
    else:
        st.write("👉 Monitor behavior and provide targeted offers.")

    # ---------------- EXTRA INFO ---------------- #
    st.subheader("📊 Model Insights")
    st.write(f"Churn Probability: {prob:.2%}")