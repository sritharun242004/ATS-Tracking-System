import streamlit as st
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import base64
import time
import datetime
from pdfminer.high_level import extract_text
from pyresparser import ResumeParser
from PIL import Image
import io
import plotly.express as px

# Function to read and parse the resume
def parse_resume(pdf_file):
    text = extract_text(pdf_file)
    with open("temp_resume.pdf", "wb") as f:
        f.write(pdf_file.getbuffer())
    resume_data = ResumeParser('temp_resume.pdf').get_extracted_data()
    return resume_data

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
            # Display the parsed information
            st.subheader("Resume Analysis")
            st.write(f"**Name:** {resume_data.get('name')}")
            st.write(f"**Email:** {resume_data.get('email')}")
            st.write(f"**Skills:** {', '.join(resume_data.get('skills', []))}")
            
            # Skill recommendations
            recommended_skills = ["Python", "Data Analysis", "Machine Learning", "Web Development"]
            st.subheader("Recommended Skills")
            for skill in recommended_skills:
                if skill not in resume_data.get('skills', []):
                    st.write(f"- {skill}")

            # Course recommendations based on field
            field = resume_data.get('designition', '').lower()
            st.subheader("Recommended Courses")
            if "data" in field:
                st.write("- Data Science Bootcamp")
                st.write("- Machine Learning with Python")
            elif "web" in field:
                st.write("- Full-Stack Web Development")
                st.write("- JavaScript for Beginners")
            else:
                st.write("- No specific courses found for this field.")
            
            # Resume score (example logic)
            resume_score = 0
            if resume_data.get('objective'):
                resume_score += 10
            if resume_data.get('declaration'):
                resume_score += 10
            st.write(f"**Resume Score:** {resume_score} / 20")

if __name__ == '__main__':
    main()
