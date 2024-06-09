from firecrawl import FirecrawlApp
import os
from dotenv import load_dotenv

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")


def scrape_url(url: str) -> dict:
    """
    Call this tool when the user wants to scrape a URL.

    Args:
        url (str): The URL to scrape.

    Returns:
        dict: The scraped data.
    """
    print("== scrape_url ==> tool called")
    print(f"Scraping the URL: {url}")
    app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

    try:
        scraped_data = app.scrape_url(url)
    except Exception as e:
        print(f"Unable to scrape the URL: {url}")
        print(e)
        return e
    markdown_data = scraped_data.get("markdown")
    return markdown_data
