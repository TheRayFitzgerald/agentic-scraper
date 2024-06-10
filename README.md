
# Agentic Web Scraper

An *agentic* web scraper built using the OpenAI Assistants API, function calling, 
[Firecrawl](https://www.firecrawl.dev/), and code interpreter.

## Features
* Natural langauge input
* Scrape any website (Agent will try to infer the domain if not specified)
* Request specific information from the website and ask follow-up questions about the data
* Run code on output of scraping, such as data analysis or writing to a file.
* Built-in file downloads.

## Usage

### Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

Don't forget to add your `OPENAI_API_KEY` and `FIRECRAWL_API_KEY` to the `.env` file.

### Example Queries

* Get all the relevant details about the team members working at Intercom (https://www.intercom.com/about). Write the results to a CSV file.
* "What are the first 5 posts listed on the hacker news site for today? Write the results to a JSON file."
* How many times is Nvidia mentioned in this article https://finance.yahoo.com/news/nvidia-stock-rises-after-10-for-1-stock-split-204412528.html ? Cite the instances where it is mentioned.
