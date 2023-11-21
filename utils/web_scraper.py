import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url: str):
        self.url = url

    def scrape_content(self) -> str:
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = self.extract_text(soup)
            cleaned_text = self.clean_text(text)
            normalized_text = self.normalize_text(cleaned_text)
            return normalized_text
        except Exception as e:
            print(f"Error scraping {self.url}: {e}")
            return None

    def extract_text(self,soup):
        """
        Extracts text from a BeautifulSoup object.
        """
        for script in soup(["script", "style"]):
            script.extract()  # Remove script and style elements

        text = soup.get_text()
        return text

    def clean_text(self, text):
        """
        Cleans the text by removing unnecessary whitespaces and line breaks.
        """
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    def normalize_text(self, text):
        import string
        text = text.lower()  # Convert to lowercase
        text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
        return text
