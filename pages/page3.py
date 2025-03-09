import streamlit as st
import re

# Helper function to validate SSN
def validate_ssn(ssn):
    ssn_pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(ssn_pattern, ssn))

# Helper function to check if the values are positive
def is_positive(value):
    return value > 0

# Create a tax filing form
with st.form("tax_filing_form", clear_on_submit=True):
    # Personal Information Section
    st.header("Personal Information")
    full_name = st.text_input("Full Name")
    ssn = st.text_input("Social Security Number (SSN)")

    if ssn and not validate_ssn(ssn):
        st.error("SSN must be in the format XXX-XX-XXXX.")
    
    address = st.text_input("Current Address")
    
    filing_status = st.selectbox(
        "Filing Status", 
        ["Single", "Married Filing Jointly", "Married Filing Separately", "Head of Household", "Qualifying Widow(er)"]
    )

    # Income Section
    st.header("Income")
    wages = st.number_input("Wages (from W-2)", min_value=0.0, format="%.2f")
    self_employment_income = st.number_input("Self-Employment Income", min_value=0.0, format="%.2f")
    other_income = st.number_input("Other Income (e.g., rental income, dividends)", min_value=0.0, format="%.2f")
    
    # Deductions and Credits Section
    st.header("Deductions and Credits")
    student_loan_interest = st.number_input("Student Loan Interest", min_value=0.0, format="%.2f")
    mortgage_interest = st.number_input("Mortgage Interest", min_value=0.0, format="%.2f")
    charitable_contributions = st.number_input("Charitable Contributions", min_value=0.0, format="%.2f")
    other_deductions = st.number_input("Other Deductions", min_value=0.0, format="%.2f")
    
    # Dependents Section
    st.header("Dependents")
    num_dependents = st.number_input("Number of Dependents", min_value=0, step=1)
    dependent_details = []
    for i in range(num_dependents):
        name = st.text_input(f"Dependent {i+1} Name", key=f"dependent_name_{i}")
        age = st.number_input(f"Dependent {i+1} Age", min_value=0, max_value=100, step=1, key=f"dependent_age_{i}")
        
        if age and not is_positive(age):
            st.error(f"Age of dependent {i+1} must be a positive number.")
        
        dependent_details.append((name, age))

    # Submit Button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        # Check if the required fields are entered correctly
        if not full_name:
            st.error("Full Name is required.")
        if not ssn or not validate_ssn(ssn):
            st.error("SSN must be in the format XXX-XX-XXXX.")
        if not is_positive(wages) and not is_positive(self_employment_income) and not is_positive(other_income):
            st.error("Income fields must contain positive values.")
        
        # Only display the summary if there are no validation errors
        if not st.session_state.get("error_occurred", False):
            st.write("### Tax Filing Information Summary")
            st.write(f"**Name:** {full_name}")
            st.write(f"**SSN:** {ssn}")
            st.write(f"**Address:** {address}")
            st.write(f"**Filing Status:** {filing_status}")
            
            st.write(f"**Wages (W-2):** ${wages}")
            st.write(f"**Self-Employment Income:** ${self_employment_income}")
            st.write(f"**Other Income:** ${other_income}")
            
            st.write(f"**Student Loan Interest Deduction:** ${student_loan_interest}")
            st.write(f"**Mortgage Interest Deduction:** ${mortgage_interest}")
            st.write(f"**Charitable Contributions:** ${charitable_contributions}")
            st.write(f"**Other Deductions:** ${other_deductions}")
            
            if num_dependents > 0:
                st.write("**Dependents:**")
                for idx, (name, age) in enumerate(dependent_details):
                    st.write(f"{idx+1}. {name}, Age: {age}")
            else:
                st.write("No dependents claimed.")
