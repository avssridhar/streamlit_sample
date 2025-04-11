"""import streamlit as st
import pandas as pd
from datetime import datetime

# Load customer data and treatment logic
from customer_treatment_engine import customers_df, determine_state, treatment_repository, get_treatment, feedback_loop

st.set_page_config(page_title="Customer Treatment Engine", layout="wide")
st.title("Customer Treatment Recommendation UI")

# Customer selection
customer_id = st.selectbox("Select Customer ID", customers_df['customer_id'].tolist())

# Show customer profile
customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0]
st.subheader("Customer Profile")
st.json(customer.to_dict())

# Determine customer state
state = determine_state(customer)
st.subheader("Customer State")
st.write(state)

# Lookup treatment
matched_treatment = get_treatment(state, treatment_repository)
st.subheader("Recommended Treatment")
if matched_treatment:
    st.write(matched_treatment)
else:
    st.write("No matching treatment found. Consider adding new rules to the treatment repository.")

# Simulate feedback loop
st.subheader("Simulate Feedback")
feedback = st.radio("Customer Response on Channel", ["WhatsApp Clicked", "No Response", "IVR Success", "SMS Ignored", "Payment Made"])

if st.button("Update State Based on Feedback"):
    updated_state = feedback_loop(state, feedback)
    updated_treatment = get_treatment(updated_state, treatment_repository)

    st.success("State and treatment updated successfully!")
    st.write("Updated State:", updated_state)
    st.write("Updated Treatment:", updated_treatment if updated_treatment else "No treatment found.")

# Display full customer dataset if needed
with st.expander(" View All Customers"):
    st.dataframe(customers_df)

with st.expander("View Treatment Repository"):
    tr_df = pd.DataFrame(treatment_repository)
    st.dataframe(tr_df)



#brew install python@3.12
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# Load customer data and treatment logic
from customer_treatment_engine import customers_df, determine_state, treatment_repository, get_treatment, feedback_loop

st.set_page_config(page_title="Customer Treatment Engine", layout="wide")
st.title("Customer Treatment Recommendation UI")

# Customer selection
customer_id = st.selectbox("Select Customer ID", customers_df['customer_id'].tolist())

# Show customer profile
customer = customers_df[customers_df['customer_id'] == customer_id].iloc[0]
st.subheader("Customer Profile")
st.json(customer.to_dict())

# Determine customer state
state = determine_state(customer)
st.subheader("Customer State")
st.write(state)

# Lookup treatment
matched_treatment = get_treatment(state, treatment_repository)
st.subheader("Recommended Treatment")
if matched_treatment:
    st.write(matched_treatment)
else:
    st.write("No matching treatment found. Consider adding new rules to the treatment repository.")

# Simulate feedback loop
st.subheader("Simulate Feedback")
feedback = st.radio("Customer Response on Channel", ["WhatsApp Clicked", "No Response", "IVR Success", "SMS Ignored", "Payment Made"])

if st.button("Update State Based on Feedback"):
    updated_treatment = feedback_loop(customer_id, feedback)
    
    st.success("State and treatment updated successfully!")
    st.write("Updated Treatment:", updated_treatment if updated_treatment else "No treatment found.")

# Display full customer dataset if needed
with st.expander(" View All Customers"):
    st.dataframe(customers_df)

with st.expander("View Treatment Repository"):
    tr_df = pd.DataFrame(treatment_repository)
    st.dataframe(tr_df)
