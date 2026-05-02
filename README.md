# Telco Customer Churn Analysis

##  Project Overview
This project analyzes customer churn behavior in a telecom company using data analytics and machine learning techniques. The goal is to identify key factors affecting churn and predict customers likely to leave.

## Project Workflow
- Cleaned & preprocessed raw data and performed EDA to uncover churn drivers
- Used SQL to generate KPIs like churn rate, revenue loss, and customer segments
- Built ML models (Logistic Regression & KMeans) for prediction and segmentation
- Created an interactive Power BI dashboard for business insights
- Deployed a Streamlit app for real-time churn prediction

## Key insights
High-Level KPI Summary
​- Churn Overview: Out of 7,032 total customers, 1,869 have churned, resulting in a significantly high churn rate of 26.58%.
​- Financial Impact: The company has lost approximately 139.13K in revenue due to churn, which is roughly 30% of the total revenue (455.66K).

​Key Drivers of Churn
​1. Contract and Tenure Vulnerability
​- Month-to-Month Risk: The vast majority of churn occurs among customers on Month-to-month contracts. In contrast, customers with one or two-year contracts show very high retention.
​- The "New Customer" Critical Period: Churn is highest in the first year. The 0-1 year tenure group has a massive churn rate of 48.54%. This rate drops drastically as tenure increases, falling to just 9.64% for those with 4+ years of loyalty.

​2. Service-Specific Pain Points
​- Fiber Optic Issues: Customers with Fiber optic internet service have a much higher churn rate (41.89%) compared to DSL users (18.96%). This suggests potential   issues with pricing or service stability for fiber.
​- Lack of Value-Added Services: Customers who do not have Tech Support, Online Security, or Device Protection are significantly more likely to leave. For example, churn among those without Tech Support is 41.65%, compared to only 15.20% for those who have it.

​3. Payment and Billing Friction
​- Electronic Checks: This payment method is associated with the highest volume of churned customers.
​- Paperless Billing: Customers signed up for paperless billing churn at a higher rate (33.59%) than those who receive paper bills (16.38%).

​4.Demographic and Behavioral Patterns
​- Monthly Charges: Churn appears to peak as monthly charges increase, specifically in the $70 - $100 range, suggesting that price sensitivity is a major factor.
​- Dependents and Partners: Customers with no dependents or no partners are more "nomadic" and likely to churn compared to those with family ties, who tend to be more stable.
​- Streaming Services: Interestingly, customers who do not use Streaming TV or Movies churn at a slightly higher rate, potentially because they see less value in the overall internet package.

​5.Strategic Recommendations
​- Incentivize Long-term Contracts: Offer discounts or loyalty rewards to move "Month-to-Month" users into 1-year agreements.
​- Improve the Onboarding Experience: Since nearly half of new customers leave within the first year, a "First 90 Days" engagement program is critical.
​- Bundle Security/Support: Offer Online Security or Tech Support as a free or discounted trial to Fiber Optic users to increase "stickiness" and perceived value.

## Business recommendation:
- Offer discounts or incentives to convert month-to-month customers into     long-term contracts
- Provide targeted retention offers for high monthly charge customers
- Focus on improving onboarding experience for new customers (low tenure)
- Encourage customers to switch from electronic check to auto-pay methods  for better retention
- Use churn prediction model to identify high-risk customers early and take proactive actions

## Live app :
[https://telco-customer-churn-7wdqtjqkmzbzbvkcktcycx.streamlit.app]
