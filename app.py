import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD FILES ---------------- #
model = joblib.load("models/logistic/LogisticRegression.pkl")
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
    tenure = st.slider("Tenure (months)", 0, 72,help="How long the customer has been with the company")
    

        # Text input for dollar values
    monthly_str = st.text_input("Monthly Charges", help="Monthly bill amount in USD")
    

    total_str = st.text_input("Total Charges", help="Enter amount (e.g., $1200)")
    st.caption("Total amount paid till date")

    # Convert to float safely
    def parse_dollars(value):
        try:
            return float(value.replace("$", "").strip())
        except:
            return 0.0   # fallback if invalid

    monthly = parse_dollars(monthly_str)
    total = parse_dollars(total_str)

    gender = st.selectbox("Gender", ["Male", "Female"],help="Customer's gender")

    senior = st.selectbox("Senior Citizen", ["Yes","No"],help="Is the customer 65 or older?")

    partner = st.selectbox("Partner", ["Yes", "No"],help="Does the customer have a spouse/partner?")
   

    dependents = st.selectbox("Dependents", ["Yes", "No"],help="Does the customer have dependents (children, family)?")
    

    phoneservice = st.selectbox("Phone Service", ["Yes", "No"],help="Does the customer have a landline phone connection?")
    "Does the customer have a landline phone connection?"

    multiplelines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"],help="Does the customer use more than one phone line?")
    

with col2:
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"],help="Type of internet connection")

    onlinesecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"],help="Extra protection against online threats")
    

    onlinebackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"],help="Cloud backup for files")

    deviceprotection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"],help="Covers device repair/replacement")

    techsupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"],help="24/7 technical support availability")

    streamingtv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"],help="TV streaming services included")

    streamingmovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"],help="Movie streaming services included")

    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"],help="Customer's contract type")

    paperless = st.selectbox("Paperless Billing", ["Yes", "No"],help="Bills sent via email instead of paper")

    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ],help="Preferred payment method")


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
