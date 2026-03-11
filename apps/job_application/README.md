# Automated Job Application System

This system is an end-to-end automated pipeline designed to search for engineering jobs, customize your resume to match the job descriptions, and automatically apply to the postings using an AI-driven browser agent.

## Features

- **Job Scraping:** Pulls the latest engineering job postings from LinkedIn and Indeed.
- **Resume Customization:** Tailors your base `resume.docx` to strictly fit a 1-page format while highlighting your fit for the specific job description.
- **Automated Application:** Uses an AI-driven browser agent to navigate to job links, fill out forms, and upload your tailored resume.

## Prerequisites

- **Python 3.10+**
- **OpenAI API Key:** For resume tailoring and the browser agent.
- **Base Resume:** A `resume.docx` file in the root directory.

## Setup

1.  **Clone the Repository:**
    ```powershell
    cd C:\Users\hezix\code\projects\apps\job_application
    ```

2.  **Install Dependencies:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    playwright install chromium
    ```

3.  **Configure Environment Variables:**
    - Create a `.env` file in the root directory (one has been created for you).
    - Add your **OpenAI API Key** and your **personal application details** (name, email, phone, etc.).
    - **Note:** Ensure your API key is secure. Do not share your `.env` file.

## Usage

1.  **Place your base resume:** Ensure your `resume.docx` is in the `job_application` folder.
2.  **Run the orchestrator:**
    ```powershell
    .\venv\Scripts\python.exe main.py
    ```

## Important Security Note

If you have shared your OpenAI API key in a public or shared environment (like a chat history), **REVOKE IT IMMEDIATELY** and generate a new one. The `.env` file and PowerShell profile have been pre-configured with the key you provided, but it should be replaced with a fresh, secure key.

## Project Structure

- `scraper.py`: Handles job board scraping.
- `resume_tailor.py`: Tailors your resume using AI.
- `agent.py`: Manages the automated browser application process.
- `main.py`: The main script that orchestrates the entire pipeline.
- `requirements.txt`: Lists all required Python packages.
- `.env`: Stores sensitive API keys and personal information.
