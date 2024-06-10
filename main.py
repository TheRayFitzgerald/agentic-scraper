from agent import Agent
from tools import scrape_url

agent = Agent(
    instructions="""
        You are an expert Agentic Web Scraper. You can scrape the web for requested information.
        You have access to a tool `scrape_url` which can be used to scrape specific URLs.
        You must try, where possible, to infer the url that the user wants to scrape.
        If you cannot infer the URL, you should ask the user for the URL, or explain that you cannot scrape the web without a URL.
        
        If you ever create a file, you should do it as normal. 
        However, in your response, you should always say the file was downloaded to the `output` directory, with the same filename as the original file.
    """,
    tools={
        scrape_url.__name__: scrape_url,
    },
)

agent.create_thread()


def chat():
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Exiting the agent...")
            break
        agent.add_message(user_input)
        answer = agent.run_agent()
        print(f"Assistant: {answer}")


def single_run():
    # user_input = input("User: ")
    # user_input = "Can you scrape the URL: https://www.wikipedia.org?"
    user_input = (
        "['Apple', 'Banana', 'Cherry', 'Date', 'Fig']` write these to a csv file"
    )
    # user_input = "what are the first 5 posts listed on the hacker news site for today (https://news.ycombinator.com/)?"
    agent.add_message(user_input)
    answer = agent.run_agent()
    print(f"Assistant: {answer}")


if __name__ == "__main__":
    pass
    chat()
    # single_run()
