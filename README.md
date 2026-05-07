🚀 End-to-End Telco Customer Churn Analysis & Prediction Project

Customer churn is one of the biggest challenges in the telecom industry, directly impacting revenue, customer lifetime value, and business growth.

The key business problem I focused on was:
👉 Why are customers leaving, and how can we predict and prevent it?

🔹 Project Workflow
Cleaned & preprocessed raw data and performed EDA to uncover churn drivers
Used SQL to generate KPIs like churn rate, revenue loss, and customer segments
Built ML models (Logistic Regression, Random Forest, XGBoost) and compared performance
Selected final model based on business objective (maximizing churn detection)
Applied K-Means clustering to segment customers into risk groups
Created an interactive Power BI dashboard for insights
Deployed a Streamlit app for real-time churn prediction

🔍 Why Customers Are Churning (Key Insights)
Churn rate: 26.58% (1,869 / 7,032 customers)
~30% revenue loss (~139K) linked to churn
Month-to-month contracts → highest churn risk
New customers (0–1 year) churn more (poor onboarding experience)
Fiber optic users churn ~2x more than DSL → possible service/value issues
Customers without Tech Support / Security churn significantly more
High monthly charges ($70–$100) strongly linked to churn
Electronic check users show higher churn behavior

🤖 Model Selection Strategy
I compared multiple models:
Logistic Regression → 94% recall (best at identifying churners)
Random Forest & XGBoost → higher accuracy (~76–77%) but lower recall
Since the business goal is to minimize customer loss, I selected Logistic Regression as the final model, prioritizing recall over accuracy to capture maximum at-risk customers.

💡 How This Solves a Real-World Problem
The deployed Streamlit app helps businesses:
Predict whether a customer is likely to churn in real time
Identify high-risk customers early
👉 This reduces revenue loss and improves customer retention strategies.

💡 Business Recommendations
Convert month-to-month users into long-term contracts with incentives
Target high monthly charge customers with personalized plans
Improve onboarding experience for new customers
Encourage auto-pay methods over electronic checks
Use churn prediction model for proactive retention campaigns

🛠️ Tools & Technologies
Python | Pandas | NumPy | scikit-learn | SQL | Power BI | Streamlit

🌐 Live App:[https://telcom-customer-churn-analysis-lr5plvx7jbflsq36avdwdx.streamlit.app⁠]
