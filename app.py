import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("SMS Spam Detector")

# Input from user
input_sms = st.text_area("Enter your message")

if st.button('Predict'):
    # Preprocess
    transformed_sms = vectorizer.transform([input_sms])
    result = model.predict(transformed_sms)[0]

    if result == 1:
        st.header("🚫 Spam")
    else:
        st.header("✅ Not Spam (Ham)")
