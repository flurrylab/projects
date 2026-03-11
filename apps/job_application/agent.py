import asyncio
import os
from dotenv import load_dotenv
from llm_factory import get_llm, get_agent
# browser-use is a framework for LLMs to control the browser
from browser_use import Browser

# Look for .env in the current directory and the root directory
load_dotenv()
load_dotenv(os.path.join(os.path.dirname(__file__), '../../.env'))

async def apply_to_job(job_link, resume_path):
    """
    Uses the browser-use agent to navigate to the job link,
    fill out the application, and upload the tailored resume.
    """
    print(f"Starting agent to apply for job at: {job_link}")
    
    # Configure the LLM for the agent
    llm = get_llm(model="gpt-4o")
    
    # Load user profile from env
    name = os.getenv("APPLICANT_NAME", "John Doe")
    email = os.getenv("APPLICANT_EMAIL", "john.doe@example.com")
    phone = os.getenv("APPLICANT_PHONE", "123-456-7890")
    linkedin = os.getenv("APPLICANT_LINKEDIN", "https://linkedin.com/in/johndoe")
    
    absolute_resume_path = os.path.abspath(resume_path)
    
    # Define the task for the browser agent
    task_prompt = f"""
    You are an automated job application assistant.
    1. Navigate to this job posting: {job_link}
    2. Look for an 'Apply', 'Apply Now', or 'Submit Application' button and click it.
    3. Fill out the application form with the following details:
       - First/Last Name or Full Name: {name}
       - Email: {email}
       - Phone: {phone}
       - LinkedIn URL: {linkedin}
    4. When asked to upload a resume or CV, use the file upload input to upload the file at: {absolute_resume_path}
    5. If there are mandatory questions (like "Are you authorized to work in the US?"), answer "Yes".
    6. Review the form. If it looks correct and filled, click the submit/send application button.
    7. If you encounter a CAPTCHA or a login wall you cannot pass, stop and report the block.
    """
    
    # Configure browser
    browser = Browser()
    
    # Initialize the agent using the factory
    agent = get_agent(
        task=task_prompt,
        llm=llm,
        browser=browser
    )
    
    try:
        # Run the agent
        result = await agent.run()
        print(f"Agent finished. Result: {result}")
        return True
    except Exception as e:
        print(f"Agent failed to apply: {e}")
        return False
    finally:
        await browser.stop()

if __name__ == "__main__":
    # Test execution
    # This will actually launch a browser if run directly.
    # asyncio.run(apply_to_job("https://example.com/apply", "resume_TechCorp.docx"))
    pass
