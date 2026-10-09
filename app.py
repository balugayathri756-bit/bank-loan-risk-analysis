import streamlit as st

st.set_page_config(
    page_title="Bank Loan Risk Analysis",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank Loan Risk Analysis")
st.write("Enter customer details to view a demo loan prediction.")

st.warning(
    "Educational demo only. This is not a real bank loan decision system."
)

age = st.number_input("Customer Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income (₹)", min_value=0, value=50000, step=5000)
loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=20000, step=5000)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=750)

if st.button("Predict Loan Status"):
    if credit_score >= 650 and income >= 40000:
        st.success("Demo Prediction: Approved ✅")
    else:
        st.error("Demo Prediction: Rejected ❌")

st.caption("This simple demo uses the project's original rule, not a trained model.")
