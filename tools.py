from firecrawl import FirecrawlApp
import os
from dotenv import load_dotenv

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")


def scrape_url(url: str) -> str:
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


def download_generated_file(file_id: str) -> str:
    """
    Only call this tool when the user explicitly asks to download a generated file, after being prompted by the agent.
    For now, this tool just prints the file_id.

    Args:
        file_id (str): The file_id of the generated file.

    Returns:
        str: The downloaded file.
    """
    print("== download_generated_file ==> tool called")
    print(f"Downloading the file with file_id: {file_id}")
    return file_id
