
import requests
from bs4 import BeautifulSoup
import time

class RAG_MANAGER:
    def __init__(self, port=9454):
        self.__port = port

    def extract_text_from_html(self, html_content):
        """Extract plain text from the provided HTML content."""
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()

    def is_server_running(self):
        """Check if the ZIMServer is running by making a request to its root."""
        try:
            response = requests.get(f"http://localhost:{self.__port}/")
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def fetch_article(self, article_title):
        """Fetches an article from the server in a separate thread."""
        if not self.is_server_running():
            print("Server is not running. Unable to fetch content.")
            return

        req_url = f"http://localhost:{self.__port}/A/{article_title}"

        try:

            response = requests.get(req_url)
            response.raise_for_status() 

            contents_text = self.extract_text_from_html(response.content)
            print(f"--- Article Content: {article_title} ---\n{contents_text}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve article '{article_title}': {e}")


    def kill_server(self):
        """Stop the ZIMServer and wait for all threads to terminate."""
        if self.__server:
            self.__server.kill_server()
            print("__server stopped__")

rag_manager = RAG_MANAGER()
rag_manager.fetch_article('Dracula')