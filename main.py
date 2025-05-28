import requests
from bs4 import BeautifulSoup
import time
import json
import csv
import argparse

class LinkedInJobsScraper:
    def __init__(self, keywords="", location=""):
        self.keywords = keywords
        self.location = location
        self.base_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        
    def build_url(self, start=0): #Build the API URL with parameters
        params = {
            'keywords': self.keywords,
            'location': self.location,
            'geoId': '',
            'trk': 'public_jobs_jobs-search-bar_search-submit',
            'start': start
        }
        return self.base_url, params
    
    def scrape_jobs_page(self, start=0): #Scrape a single page of jobs
      
        url, params = self.build_url(start)
        
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            jobs = soup.find_all('li')
            
            print(f"Num Jobs Returned: {len(jobs)}")
            
            job_list = []
            for job in jobs:
                job_data = self.extract_job_data(job)
                if job_data:
                    job_list.append(job_data)
                    
            return job_list, len(jobs)
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {start}: {e}")
            return [], 0
    
    def extract_job_data(self, job_element): #Extract job data from a job element
    
        try:
            # Job title
            title_elem = job_element.select_one('h3')
            job_title = title_elem.get_text(strip=True) if title_elem else 'not-found'
            
            # Job detail URL
            link_elem = job_element.select_one('.base-card__full-link')
            job_detail_url = link_elem.get('href', 'not-found') if link_elem else 'not-found'
            
            # Job listed time
            time_elem = job_element.select_one('time')
            job_listed = time_elem.get_text(strip=True) if time_elem else 'not-found'
            
            # Company name
            company_elem = job_element.select_one('h4 a')
            company_name = company_elem.get_text(strip=True) if company_elem else 'not-found'
            
            # Company link
            company_link = company_elem.get('href', 'not-found') if company_elem else 'not-found'
            
            # Company location
            location_elem = job_element.select_one('.job-search-card__location')
            company_location = location_elem.get_text(strip=True) if location_elem else 'not-found'
            
            return {
                'job_title': job_title,
                'job_detail_url': job_detail_url,
                'job_listed': job_listed,
                'company_name': company_name,
                'company_link': company_link,
                'company_location': company_location
            }
            
        except Exception as e:
            print(f"Error extracting job data: {e}")
            return None
    
    def scrape_all_jobs(self, max_pages=10, delay=2): #Scrape all available jobs with pagination
        all_jobs = []
        start = 0
        page_count = 0
        
        while page_count < max_pages:
            print(f"\n--- Scraping page {page_count + 1} (starting from job {start}) ---")
            
            jobs, num_jobs = self.scrape_jobs_page(start)
            
            if num_jobs == 0:
                print("No more jobs found. Stopping.")
                break
                
            all_jobs.extend(jobs)
            print(f"Scraped {len(jobs)} jobs from this page")
            
            # Move to next page
            start += 25
            page_count += 1
            
            # Add delay to be respectful to the server
            if page_count < max_pages:
                time.sleep(delay)
        
        return all_jobs
    
    def save_to_json(self, jobs, filename="linkedin_jobs.json"): #Save jobs to JSON file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(jobs, f, indent=2, ensure_ascii=False)
        print(f"\nSaved {len(jobs)} jobs to {filename}")
    
    def save_to_csv(self, jobs, filename="linkedin_jobs.csv"): #Save jobs to CSV file
        if not jobs:
            print("No jobs to save")
            return
            
        # Define CSV headers
        headers = ['job_title', 'company_name', 'company_location', 'job_listed', 
                  'job_detail_url', 'company_link']
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(jobs)
        
        print(f"\nSaved {len(jobs)} jobs to {filename}")
    
    def save_data(self, jobs, filename, format_type='csv'):  #Save jobs in specified format
        if format_type.lower() == 'json':
            self.save_to_json(jobs, filename)
        elif format_type.lower() == 'csv':
            self.save_to_csv(jobs, filename)
        else:
            print("Unsupported format. Use 'csv' or 'json'")
            self.save_to_csv(jobs, filename.replace('.json', '.csv'))


def main():
    parser = argparse.ArgumentParser(description='Scrape LinkedIn jobs')
    parser.add_argument('--keywords', '-k', default='python', help='Job keywords to search for')
    parser.add_argument('--location', '-l', default='', help='Job location')
    parser.add_argument('--pages', '-p', type=int, default=5, help='Max pages to scrape')
    parser.add_argument('--delay', '-d', type=int, default=2, help='Delay between requests (seconds)')
    parser.add_argument('--output', '-o', default='linkedin_jobs.csv', help='Output filename')
    parser.add_argument('--format', '-f', choices=['csv', 'json'], default='csv', 
                       help='Output format (csv or json)')
    
    args = parser.parse_args()
    
    print(f"Searching for: {args.keywords}")
    print(f"Location: {args.location or 'Any'}")
    print(f"Max pages: {args.pages}")
    print(f"Delay: {args.delay}s")
    print(f"Output format: {args.format}")
    print("-" * 50)
    
    # Initialize scraper
    scraper = LinkedInJobsScraper(keywords=args.keywords, location=args.location)
    
    # Scrape jobs
    jobs = scraper.scrape_all_jobs(max_pages=args.pages, delay=args.delay)
    
    # Print summary
    print(f"\nSCRAPING COMPLETE")
    print(f"Total jobs scraped: {len(jobs)}")
    
    # Save to file
    scraper.save_data(jobs, args.output, args.format)

if __name__ == "__main__":
    main()