# 🔍 LinkedIn Jobs Scraper

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

A powerful Python web scraper for extracting job listings from LinkedIn's public job search pages. Search for jobs by keywords and location, then export results to CSV or JSON format with built-in pagination and rate limiting.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/linkedin-jobs-scraper.git
cd linkedin-jobs-scraper

# Install dependencies
pip install -r requirements.txt

# Run with default settings (searches for "python" jobs)
python linkedin_scraper.py

# Search for specific jobs
python linkedin_scraper.py --keywords "data scientist" --location "New York" --pages 5
```

## ✨ Features

- 🎯 **Targeted Search** - Search jobs by keywords and location
- 📄 **Pagination Support** - Scrape multiple pages automatically  
- 💾 **Multiple Export Formats** - Save to CSV or JSON
- ⏱️ **Rate Limiting** - Configurable delays to respect server limits
- 🛡️ **Error Handling** - Robust error handling and retry logic
- 📊 **Progress Tracking** - Real-time scraping progress updates
- 🖥️ **CLI Interface** - Easy-to-use command line interface

## 📋 Table of Contents

- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Output Format](#-output-format)
- [Examples](#-examples)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Dependencies

Create a `requirements.txt` file:

```txt
requests>=2.25.1
beautifulsoup4>=4.9.3
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
# Default search (python jobs, any location, 5 pages)
python linkedin_scraper.py
```

### Advanced Usage

```bash
python linkedin_scraper.py \
  --keywords "machine learning engineer" \
  --location "San Francisco Bay Area" \
  --pages 10 \
  --delay 3 \
  --format json \
  --output ml_jobs.json
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

### Environment Variables

You can also set default values using environment variables:

```bash
export LINKEDIN_KEYWORDS="data science"
export LINKEDIN_LOCATION="Remote"
export LINKEDIN_DELAY=3
```

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

## 💡 Examples

<details>
<summary>Click to expand examples</summary>

### 1. Remote Job Search
```bash
python linkedin_scraper.py \
  --keywords "python remote" \
  --location "United States" \
  --pages 3 \
  --output remote_python_jobs.csv
```

### 2. Data Science Jobs in Tech Hubs
```bash
python linkedin_scraper.py \
  --keywords "data scientist" \
  --location "San Francisco" \
  --format json \
  --output sf_data_science.json \
  --pages 8
```

### 3. Entry Level Positions
```bash
python linkedin_scraper.py \
  --keywords "entry level software engineer" \
  --pages 5 \
  --delay 4 \
  --output entry_level_jobs.csv
```

### 4. Specific Company Search
```bash
python linkedin_scraper.py \
  --keywords "google software engineer" \
  --location "Mountain View" \
  --pages 2
```

</details>

## 🏗️ Architecture

```
linkedin_scraper.py
├── LinkedInJobsScraper
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

## ⚠️ Important Notes

### Rate Limiting
- **Default delay**: 2 seconds between requests
- **Recommended**: Increase delay for large scraping jobs
- **Best practice**: Monitor your request rate

### Legal Considerations

> ⚖️ **Disclaimer**: This tool accesses only publicly available data. Users must comply with LinkedIn's Terms of Service and applicable laws.

- ✅ Only scrapes public job listings
- ✅ No authentication required
- ⚠️ Review LinkedIn's robots.txt and ToS
- 🚫 Don't use for commercial purposes without proper authorization

### Limitations

- Limited to LinkedIn's guest job search results
- May break if LinkedIn updates their HTML structure
- Some fields may show 'not-found' if elements are missing
- No access to premium job details

## 🐛 Troubleshooting

<details>
<summary>Common Issues and Solutions</summary>

### Issue: No jobs found
**Possible causes:**
- Invalid keywords or location
- LinkedIn structure changes
- Network connectivity issues

**Solutions:**
```bash
# Try different keywords
python linkedin_scraper.py -k "software developer" -l "California"

# Check connectivity
python -c "import requests; print(requests.get('https://linkedin.com').status_code)"
```

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

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Fork and clone the repo
git clone https://github.com/yourusername/linkedin-jobs-scraper.git
cd linkedin-jobs-scraper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

### Submitting Changes

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Make your changes
4. ✅ Add tests for new functionality
5. 📝 Update documentation if needed
6. 🚀 Commit your changes (`git commit -m 'Add amazing feature'`)
7. 📤 Push to the branch (`git push origin feature/amazing-feature`)
8. 🔄 Open a Pull Request

## 📝 Changelog

### v1.0.0 (2024-01-15)
- Initial release
- Basic job scraping functionality
- CSV and JSON export support
- Command line interface

See [CHANGELOG.md](CHANGELOG.md) for full version history.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [requests](https://requests.readthedocs.io/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- Inspired by the need for accessible job market data
- Thanks to all contributors

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yourusername/linkedin-jobs-scraper/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/yourusername/linkedin-jobs-scraper/discussions)
- 📧 **Contact**: your.email@example.com

---

<div align="center">

**⭐ Star this repo if you find it helpful! ⭐**

Made with ❤️ by [Your Name](https://github.com/yourusername)

</div>
