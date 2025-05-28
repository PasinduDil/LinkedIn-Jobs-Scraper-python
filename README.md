# 🔍 LinkedIn Jobs Scraper

A powerful Python web scraper for extracting job listings from LinkedIn's public job search pages. Search for jobs by keywords and location, then export results to CSV or JSON format with built-in pagination and rate limiting.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/linkedin-jobs-scraper.git](https://github.com/PasinduDil/LinkedIn-Jobs-Scraper-python.git
cd linkedin-jobs-scraper

# Install dependencies
pip install -r requirements.txt

# Run with default settings (searches for "python" jobs)
python main.py

# Search for specific jobs
python linkedin_scraper.py --keywords "data scientist" --location "New York" --pages 5
```

## ✨ Features

- **Targeted Search** - Search jobs by keywords and location
- **Pagination Support** - Scrape multiple pages automatically  
- **Multiple Export Formats** - Save to CSV or JSON
- **Rate Limiting** - Configurable delays to respect server limits
- **Error Handling** - Robust error handling and retry logic
- **Progress Tracking** - Real-time scraping progress updates
- **CLI Interface** - Easy-to-use command line interface


## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Dependencies

Create a `requirements.txt` file:

```txt
requests
beautifulsoup4
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Alternative Installation

```bash
pip install requests beautifulsoup4
```

## 🚀 Usage

### Basic Usage

```bash
python main.py
```

### Advanced Usage

```bash
python main.py \
  --keywords "machine learning engineer" \
  --location "Sri lanka" \
  --pages 10 \
  --delay 3 \
  --format json \
  --output ml_jobs.csv
```

## ⚙️ Configuration

### Command Line Arguments

| Parameter | Short | Description | Default | Type |
|-----------|-------|-------------|---------|------|
| `--keywords` | `-k` | Job search keywords | `python` | string |
| `--location` | `-l` | Job location filter | `""` (any) | string |
| `--pages` | `-p` | Maximum pages to scrape | `5` | int |
| `--delay` | `-d` | Delay between requests (seconds) | `2` | int |
| `--output` | `-o` | Output filename | `linkedin_jobs.csv` | string |
| `--format` | `-f` | Output format | `csv` | csv/json |


## 📊 Output Format

### CSV Format

| Column | Description | Example |
|--------|-------------|---------|
| `job_title` | Job title | "Senior Python Developer" |
| `company_name` | Company name | "Tech Corp Inc" |
| `company_location` | Job location | "New York, NY" |
| `job_listed` | Posted date | "2 days ago" |
| `job_detail_url` | Direct job link | "https://linkedin.com/jobs/..." |
| `company_link` | Company profile link | "https://linkedin.com/company/..." |

### JSON Format

```json
[
  {
    "job_title": "Senior Python Developer",
    "company_name": "Tech Corp Inc",
    "company_location": "New York, NY",
    "job_listed": "2 days ago",
    "job_detail_url": "https://linkedin.com/jobs/view/12345",
    "company_link": "https://linkedin.com/company/techcorp"
  }
]
```


## 🏗️ Architecture

```
LinkedIn Jobs Scraper
├── Main,py
│   ├── __init__(keywords, location)
│   ├── build_url(start) → (url, params)
│   ├── scrape_jobs_page(start) → (jobs, count)
│   ├── extract_job_data(job_element) → job_dict
│   ├── scrape_all_jobs(max_pages, delay) → jobs_list
│   ├── save_to_json(jobs, filename)
│   ├── save_to_csv(jobs, filename)
│   └── save_data(jobs, filename, format)
└── main() # CLI interface
```

## 🔧 API Reference

### LinkedInJobsScraper Class

#### Constructor
```python
scraper = LinkedInJobsScraper(keywords="python", location="New York")
```

#### Methods

**`scrape_all_jobs(max_pages=10, delay=2)`**
- Scrapes jobs with pagination
- Returns: List of job dictionaries
- Parameters:
  - `max_pages`: Maximum pages to scrape
  - `delay`: Seconds between requests

**`save_data(jobs, filename, format_type='csv')`**
- Saves job data to file
- Parameters:
  - `jobs`: List of job dictionaries
  - `filename`: Output filename
  - `format_type`: 'csv' or 'json'


### Limitations

- Limited to LinkedIn's guest job search results
- May break if LinkedIn updates their HTML structure
- Some fields may show 'not-found' if elements are missing
- No access to premium job details



<details>
### Issue: Request errors (429, 403)
**Solutions:**
```bash
# Increase delay between requests
python linkedin_scraper.py --delay 5

# Reduce pages
python linkedin_scraper.py --pages 2
```

### Issue: Parsing errors
**Possible causes:**
- LinkedIn HTML structure changed
- Network timeouts

**Solutions:**
- Check the CSS selectors in `extract_job_data()`
- Update the scraper code if needed

</details>



### Development Setup

```bash
# Fork and clone the repo
https://github.com/PasinduDil/LinkedIn-Jobs-Scraper-python.git


# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python main.py/
```

<div align="center">

**⭐ Star this repo if you find it helpful! ⭐**

Made with ❤️ by [Your Name](https://github.com/yourusername)

</div>
