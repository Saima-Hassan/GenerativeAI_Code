import streamlit as st
import google.generativeai as genai

# Configure the API key for Google Gemini
api_key = "AIzaSyDvlTh_IP1l7b-9bv8ev0i5g50WHCgb2zs"
genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit app interface
st.title("Text Generation App")
st.write("This app generates text using the Google Gemini model.")

# Input field for user prompt
user_input = st.text_input("Enter your prompt:", "Write a story about a magic backpack.")

# Generate response button
if st.button("Generate Text"):
    if user_input:
        # Generate text using the model
        response = model.generate_content(user_input)
        
        # Display the generated text
        st.subheader("Generated Text:")
        st.write(response.text)
    else:
        st.error("Please enter a prompt to generate text.")

# Optionally, add a footer or more features
st.write("This app uses the Google Gemini model to generate creative content.")