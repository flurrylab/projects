import asyncio
import os
from scraper import scrape_jobs
from resume_tailor import process_resume
from agent import apply_to_job

async def main():
    print("=== Automated Job Application System ===")
    
    # Phase 1: Scrape Jobs
    print("\n--- Phase 1: Scraping Jobs ---")
    jobs = await scrape_jobs(keyword="Software Engineer", location="Remote", max_jobs=2)
    
    if not jobs:
        print("No jobs found. Exiting.")
        return

    # Phase 2 & 3: Tailor Resume and Apply for each job
    for i, job in enumerate(jobs):
        print(f"\n--- Processing Job {i+1}: {job['title']} at {job['company']} ---")
        
        # Phase 2: Tailor Resume
        print("Tailoring resume...")
        tailored_resume_path = process_resume(job)
        
        if not tailored_resume_path:
            print("Failed to tailor resume. Skipping application.")
            continue
            
        print(f"Resume tailored and saved to: {tailored_resume_path}")
        
        # Phase 3: Apply using Agent
        print("Initiating automated application...")
        # Note: Uncomment the line below to actually trigger the browser automation
        # Be aware it requires OPENAI_API_KEY and actual valid application URLs to work fully.
        
        # success = await apply_to_job(job['link'], tailored_resume_path)
        # if success:
        #     print(f"Successfully applied to {job['company']}!")
        # else:
        #     print(f"Failed to apply to {job['company']}.")
            
        print(f"Simulated application to {job['company']} completed.")

if __name__ == "__main__":
    asyncio.run(main())
