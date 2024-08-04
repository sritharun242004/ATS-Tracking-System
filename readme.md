# AI ATS SYSTEM

This project is an AI-powered Applicant Tracking System (ATS) that evaluates resumes based on job descriptions using advanced generative models. It helps users improve their resumes by identifying the matching percentage, missing keywords, and providing a profile summary.

## Why is an ATS Important?

In today's competitive job market, many companies use Applicant Tracking Systems (ATS) to filter and rank candidates' resumes before they reach a human recruiter. An ATS scans resumes for keywords and phrases relevant to the job description, ensuring that only the most qualified candidates are considered. This project aims to help job seekers optimize their resumes to increase their chances of passing through these automated filters.

## Features

- Extracts text from uploaded PDF resumes.
- Evaluates resumes against provided job descriptions.
- Generates a detailed response with the matching percentage, missing keywords, and profile summary.
- User-friendly interface with a dark mode theme.
- Customizable prompt for generating responses from Gemini Pro.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your_username/your_repo_name.git
   cd your_repo_name
 
2. **Install the required dependencies:**
   ```sh
   pip3 install -r requirements.txt

3. **Set up environment variables::**

   1.Create a .env file in the root directory.
   2.Add your Google API key to the .env file:

      ```sh
      GOOGLE_API_KEY=your_google_api_key

# Code Overview
● app.py: The main application file that runs the Streamlit app.
● requirements.txt: Lists all the dependencies required to run the project.
● .env: Contains environment variables (not included in the repository for security reasons).
