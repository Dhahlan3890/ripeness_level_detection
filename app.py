import streamlit as st
from PIL import Image
from google import genai
import io
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the page
st.title("Fruit Ripeness Detector")
st.write("Upload an image of a fruit to determine its ripeness level")

# Initialize the Google AI client
client = genai.Client(api_key=os.getenv("GEMINI_API"))

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Add a button to analyze the image
    if st.button("Analyze Ripeness"):
        with st.spinner("Analyzing..."):
            try:
                # Get the prediction
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[image, "Tell me the ripeness level as unripe, ripe, over ripe, rotten. only return the ripeness level"]
                )
                
                # Display the result
                st.success("Analysis Complete!")
                st.subheader(f"Ripeness Level: {response.text}")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")