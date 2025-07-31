import streamlit as st
import joblib

# Load the trained model and vectorizer
svm_model = joblib.load('svm_email_classifier.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Title
st.set_page_config(page_title="📧 Email Classifier", layout="centered")
st.title("📧 Email Spam Classifier")
st.markdown("Enter an email below to predict whether it's **Spam** or **Not Spam (Ham)**.")

# Input form
email_input = st.text_area("✉️ Paste email content here:", height=200)

# Predict button
if st.button("🔍 Predict"):
    if email_input.strip() == "":
        st.warning("⚠️ Please enter some email content.")
    else:
        # Vectorize and predict
        email_vector = vectorizer.transform([email_input])
        prediction = svm_model.predict(email_vector)[0]

        # Display result
        if int(prediction)==1:
            st.error("🚨 Prediction: SPAM")
        else:
            st.success("✅ Prediction: NOT SPAM (HAM)")
