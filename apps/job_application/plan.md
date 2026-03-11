# Automated Job Application System Plan

## 1. Overview
This system is an end-to-end automated pipeline designed to search for engineering jobs, customize the applicant's resume to strictly match the job descriptions, and automatically apply to the postings using an AI-driven browser agent. 

## 2. Architecture & Tech Stack
*   **Language:** Python 3.10+
*   **Web Scraping & Browser Automation:** Playwright (preferred for speed and reliability) or Selenium.
*   **LLM Integration:** OpenAI API / Gemini API (via LangChain or LlamaIndex) for reasoning, form-filling, and text customization.
*   **Document Processing:** `python-docx` for reading and writing `.docx` files (converting from `.doc`). `pdfkit` or equivalent if PDF conversion is required.
*   **Database:** SQLite or simply a structured CSV/JSON file to keep track of jobs applied to, their links, and statuses.
*   **Agent Framework:** Browser-Use, AutoGPT, or a custom LangChain agent tailored to interact with web elements.

## 3. Phase 1: Job Scraping (LinkedIn & Indeed)
**Objective:** Pull the latest engineering job postings and save their metadata.
*   **Strategy:**
    *   Since LinkedIn and Indeed have strict anti-scraping mechanisms, standard requests will be blocked. We will use **Playwright** in stealth mode, or leverage third-party APIs (like Apify or RapidAPI) to fetch job listings.
    *   Search parameters (e.g., "Software Engineer", location, experience level) will be defined in a configuration file.
    *   **Data Extracted:** Job Title, Company, Job Link, Job Description.
    *   **Output:** The script saves the scraped jobs into a `jobs.json` or SQLite database.

## 4. Phase 2: Resume Customization
**Objective:** Tailor the base resume (`resume.docx`) to highlight fitness for a specific job description, ensuring it is **strictly one page**.
*   **Strategy:**
    *   **Parsing:** Read the base `resume.doc`/`resume.docx` using `python-docx` to extract text, skills, and experience blocks.
    *   **LLM Processing:** Pass the job description and the parsed base resume to an LLM with a strong system prompt.
        *   *System Prompt Instruction:* "You are an expert career coach. Re-write the bullet points of this resume to perfectly align with the following job description. Emphasize matching skills and boldly brag about the candidate's fitness for the role, while keeping the facts accurate to the original resume. **Crucially, ensure the output fits within a single page, prioritizing the most relevant experiences and using concise, high-impact language.**"
    *   **Re-assembly:** Take the LLM's tailored output and write it back to a cleanly formatted `.docx` file (e.g., `resume_Company_JobTitle.docx`). 
        *   **Dynamic Formatting:** Implement logic to adjust font size (within 10-12pt) and margins if the content is slightly over or under one page.
        *   **PDF Conversion:** Optionally convert to PDF as most portals prefer PDFs.

## 5. Phase 3: Automated Application (Bonus - Agentic Approach)
**Objective:** Autonomously navigate to the job link, fill out the application form, upload the tailored resume, and submit.
*   **Strategy:**
    *   We will use a **Browser Agent** (e.g., using LangChain's Playwright Toolkit or an open-source framework like `browser-use`).
    *   **Agent Workflow:**
        1.  **Navigate:** Open the saved job link.
        2.  **Analyze:** The agent visually/structurally parses the DOM to find the "Apply Now" button and clicks it.
        3.  **Form Filling:** The agent reads form fields (Name, Email, Phone, LinkedIn profile, Questionnaire). It uses the LLM and the candidate's base profile to accurately fill in inputs and dropdowns.
        4.  **Upload:** Locate the file upload input element and upload the customized `resume_Company_JobTitle.docx` (or PDF).
        5.  **Submit:** Click the submit button.
    *   **Handling Edge Cases:**
        *   *Complex portals (Workday, Greenhouse, Lever):* The agent will be trained on the common DOM structures of these ATS (Applicant Tracking Systems).
        *   *CAPTCHAs:* If encountered, the agent will pause and alert the user, or attempt to use a 2Captcha-style service.

## 6. Execution Roadmap
*   **Step 1:** Setup Python virtual environment and basic folder structure.
*   **Step 2:** Write the scraping module for LinkedIn/Indeed. Test and output to JSON.
*   **Step 3:** Write the document parsing and LLM generation module. Test the creation of a tailored resume from a sample job description.
*   **Step 4:** Develop the browser agent using Playwright to handle a simple form (e.g., Greenhouse or Lever).
*   **Step 5:** Integrate all modules into a single pipeline (`main.py`) where it loops over scraped jobs, tailors the resume, and delegates the application to the browser agent.