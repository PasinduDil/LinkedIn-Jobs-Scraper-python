LinkedIn Jobs Scraper
   A Python web scraper for extracting job listings from LinkedIn's public job search pages. This tool allows you to search for jobs by keywords and location, then export the results to CSV or JSON format.

Features

🔍 Search jobs by keywords and location
📄 Pagination support to scrape multiple pages
💾 Export data to CSV or JSON formats
⏱️ Configurable delay between requests to be respectful to servers
🛡️ Built-in error handling and retry logic
📊 Real-time progress tracking

## Installation

Python 3.6+
   Prerequisites
   pip (Python package installer)

Dependencies
   Install the required packages:
   ## pip install requests beautifulsoup4

Or create a requirements.txt file: ## pip install -r requirements.txt
   requests
   beautifulsoup4

## Usage

Basic Usage
 ## python linkedin_scraper.py

Advanced Usage
## python linkedin_scraper.py --keywords "data scientist" --location "New York" --pages 10 --format json --output my_jobs.json

## Output Format
CSV Output
  The CSV file contains the following columns:

    job_title: The job title
    company_name: Company offering the job
    company_location: Job location
    job_listed: When the job was posted
    job_detail_url: Direct link to the job posting
    company_link: Link to the company's LinkedIn page


## Code Structure

linkedin_scraper.py
├── LinkedInJobsScraper (Main class)
│   ├── __init__()           # Initialize scraper with keywords and location
│   ├── build_url()          # Build API URL with parameters
│   ├── scrape_jobs_page()   # Scrape a single page of jobs
│   ├── extract_job_data()   # Extract job data from HTML elements
│   ├── scrape_all_jobs()    # Main scraping function with pagination
│   ├── save_to_json()       # Save results to JSON file
│   ├── save_to_csv()        # Save results to CSV file
│   └── save_data()          # Generic save function
└── main()                   # Command line interface