import streamlit as st
import pdfplumber
import base64
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from PIL import Image
import io
import plotly.express as px

# Ensure stopwords are downloaded
nltk.download('stopwords')

# Function to read and extract text from the resume
def parse_resume(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ''.join(page.extract_text() for page in pdf.pages if page.extract_text() is not None)
        if not text:
            st.error("No text found in the resume.")
            return None
        return {'text': text}
    except Exception as e:
        st.error(f"An error occurred while parsing the resume: {e}")
        return None

# Function to display the PDF
def display_pdf(file):
    base64_pdf = base64.b64encode(file.getvalue()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit app
def main():
    st.title("Smart Resume Analyzer")

    pdf_file = st.file_uploader("Upload your Resume", type=["pdf"])

    if pdf_file is not None:
        # Display the PDF
        display_pdf(pdf_file)

        # Parse the resume
        resume_data = parse_resume(pdf_file)

        if resume_data:
            # Display the extracted text
            st.subheader("Extracted Text")
            st.text_area("Resume Content", resume_data['text'], height=300)

            # Simulate resume analysis and recommendations
            st.subheader("Resume Analysis")
            st.write("**Name:** Not Extracted")  # Placeholder
            st.write("**Email:** Not Extracted")  # Placeholder
            st.write("**Skills:** Not Extracted")  # Placeholder

            # Skill recommendations
            recommended_skills = ["Python", "Data Analysis", "Machine Learning", "Web Development"]
            st.subheader("Recommended Skills")
            for skill in recommended_skills:
                st.write(f"- {skill}")

            # Course recommendations based on field (simulated)
            st.subheader("Recommended Courses")
            st.write("- Data Science Bootcamp")
            st.write("- Machine Learning with Python")

            # Resume score (example logic)
            resume_score = 0
            st.write(f"**Resume Score:** {resume_score} / 20")

if __name__ == '__main__':
    main()
