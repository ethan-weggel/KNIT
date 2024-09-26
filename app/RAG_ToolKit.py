
import requests
from bs4 import BeautifulSoup
import time

class RAGToolKit:
    def __init__(self, port=9454):
        self.__port = port

    def extractTextFromHtml(self, htmlContent):
        soup = BeautifulSoup(htmlContent, 'html.parser')
        return soup.get_text()

    def isServerRunning(self):
        try:
            response = requests.get(f"http://localhost:{self.__port}/")
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def fetchArticle(self, articleTitle):
        print('entered func')
        if not self.isServerRunning():
            print("Server is not running. Unable to fetch content.")
            return

        req_url = f"http://localhost:{self.__port}/A/{articleTitle}"

        try:
            response = requests.get(req_url)
            response.raise_for_status() 

            contentsText = self.extractTextFromHtml(response.content)
            print(f"--- Article Content: {articleTitle} ---\n{contentsText}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve article '{articleTitle}': {e}")
