import streamlit as st
import joblib

# Load the trained model
model = joblib.load("news-classification-model.pkl")

# Define News labels
news_labels = {'0': 'Technical', '1': 'Business', '2': 'Sports', '3': 'Entertainment', '4': 'Politics'}

# Create Streamlit app
st.title("News Classification")

# Input text area
user_input = st.text_area("Enter News Here:")

# Prediction button
if st.button("Predict"):
    predicted_label= model.predict([user_input])[0]
    predicted_news_label = news_labels[str(predicted_label)]

    # Display predicted Label
    st.info(f"Predicted Label: {predicted_news_label}")