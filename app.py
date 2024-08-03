import streamlit as st
import google.generativeai as genai
import os 
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load all the environment variables
load_dotenv()

# Access the API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to get Gemini Pro response
def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt template
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in multiple lines string having the prettier structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

# Set page configuration
st.set_page_config(
    page_title="AI ATS SYSTEM",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for dark mode with red and black theme
st.markdown("""
    <style>
    .stApp {
        background-color: #141414; /* Dark background color */
        color: #ffffff; /* Default text color */
    }
    /* Style for headers */
    .stHeader {
        color: #ffffff !important; /* White color for header */
    }
    h1, h2, h3 {
        color: #ffffff !important; /* White color for headers */
    }
    .stSelectbox {
        margin-bottom: 20px; /* Space below the dropdown */
    }
    .stButton>button {
        background-color: #ff0000; /* Red button background */
        color: #ffffff; /* White text color for the button */
        border: 1px solid #ff0000; /* Red border */
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #e60000; /* Darker red on hover */
        border: 1px solid #e60000;
    }
    .stText {
        color: #ffffff; /* Ensure text is readable */
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app content
st.header("RESUME ATS SYSTEM")  # Header styled in white
st.text("Improve Your Resume ATS")

jd = st.text_area("Paste the job description", key="jd_input")
uploaded_file = st.file_uploader("Upload your resume", type="pdf", help="Please upload the pdf file")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))
        st.subheader(response)
