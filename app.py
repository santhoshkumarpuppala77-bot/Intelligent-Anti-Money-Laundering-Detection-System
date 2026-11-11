import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf

# Intelligent Anti-Money Laundering Detection System
# Using Artificial Neural Networks

st.set_page_config(
    page_title="AML Detection System",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Intelligent Anti-Money Laundering Detection System")
st.subheader("Using Artificial Neural Networks")
st.write("Enter the transaction details to analyze the payment.")

MODEL_PATH = "AIML.keras"
PREPROCESSOR_PATH = "preprocessor"


@st.cache_resource
def load_artifacts():
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    return model, preprocessor


try:
    model, preprocessor = load_artifacts()
except Exception as error:
    st.error("Could not load the model or preprocessor. Check that both files are in this folder.")
    st.exception(error)
    st.stop()


# Dropdown values from the categories saved in the preprocessor
payment_currencies = [
    "Albanian lek", "Dirham", "Euro", "Indian rupee", "Mexican Peso",
    "Moroccan dirham", "Naira", "Pakistani rupee", "Swiss franc",
    "Turkish lira", "UK pounds", "US dollar", "Yen"
]

received_currencies = payment_currencies

bank_locations = [
    "Albania", "Austria", "France", "Germany", "India", "Italy",
    "Japan", "Mexico", "Morocco", "Netherlands", "Nigeria", "Pakistan",
    "Spain", "Switzerland", "Turkey", "UAE", "UK", "USA"
]

payment_types = [
    "ACH", "Cash Deposit", "Cash Withdrawal", "Cheque",
    "Credit card", "Cross-border", "Debit card"
]

st.divider()
st.markdown("### Transaction Details")

with st.form("transaction_form"):
    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0,
        step=100.0,
        format="%.2f"
    )

    col1, col2 = st.columns(2)

    with col1:
        payment_currency = st.selectbox("Payment Currency", payment_currencies)
        sender_bank_location = st.selectbox("Sender Bank Location", bank_locations)
        payment_type = st.selectbox("Payment Type", payment_types)

    with col2:
        received_currency = st.selectbox("Received Currency", received_currencies)
        receiver_bank_location = st.selectbox("Receiver Bank Location", bank_locations)

    submitted = st.form_submit_button(
        "Analyze Transaction",
        use_container_width=True
    )


if submitted:
    input_data = pd.DataFrame([{
        "Amount": amount,
        "Payment_currency": payment_currency,
        "Received_currency": received_currency,
        "Sender_bank_location": sender_bank_location,
        "Receiver_bank_location": receiver_bank_location,
        "Payment_type": payment_type
    }])

    try:
        processed_data = preprocessor.transform(input_data)

        if hasattr(processed_data, "toarray"):
            processed_data = processed_data.toarray()

        processed_data = np.asarray(processed_data, dtype=np.float32)
        prediction = np.asarray(model.predict(processed_data, verbose=0))

        # Confirmed target encoding: 0 = Not Money Laundering,
        # 1 = Money Laundering. For the tanh output, use 0.5
        # as the midpoint decision threshold for labels 0 and 1.
        output_score = float(prediction.reshape(-1)[0])
        predicted_class = 1 if output_score >= 0.5 else 0

        st.divider()
        st.subheader("Prediction Result")

        if predicted_class == 1:
            st.error("Money Laundering")
        else:
            st.success("Not Money Laundering")

    except Exception as error:
        st.error("Prediction could not be completed. Please check the input values and model files.")
        st.exception(error)
