import streamlit as st

st.set_page_config(page_title="Customer Churn Prediction")

st.title("📊 Customer Churn Prediction")

st.write("Customer Churn Prediction project using Machine Learning and Streamlit 🚀")

st.subheader("Customer Details")

gender = st.selectbox("Gender", ["Male", "Female"])

senior = st.selectbox("Senior Citizen", ["No", "Yes"])

tenure = st.slider("Tenure (Months)", 0, 72)

monthly = st.slider("Monthly Charges", 0, 200)

if st.button("Analyze Customer"):
    
    st.success("Customer data analyzed successfully!")
    
    st.write("### Customer Summary")
    st.write(f"Gender: {gender}")
    st.write(f"Senior Citizen: {senior}")
    st.write(f"Tenure: {tenure} months")
    st.write(f"Monthly Charges: ₹{monthly}")