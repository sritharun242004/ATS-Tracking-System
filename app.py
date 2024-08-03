import streamlit as st
import google.generativeai as genai
import os 
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv() #load all the environment variables

# access the api key
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))


## Gemini Pro Response
def get_gemini_response(input):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(input)
    return  response.text

## extact the pdf 

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    # for multiple page read
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text +=str(page.extract_text())

    return text 
 
# prompt template is something to design your own response as you like
#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in multipe lines string having the prettier structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""


## streamlit app
st.title(" AI ATS SYSTEM ")
st.text("Improve Your Reaume ATS")
jd=st.text_area("Paste the job discription")
uploaded_file=st.file_uploader("Upload your resume",type="pdf", help="Please upload the pdf file")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)