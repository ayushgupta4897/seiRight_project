import requests
from bs4 import BeautifulSoup

def extract_text(soup):
    """
    Extracts text from a BeautifulSoup object.
    """
    for script in soup(["script", "style"]):
        script.extract()  # Remove script and style elements

    text = soup.get_text()
    return text

def clean_text(text):
    """
    Cleans the text by removing unnecessary whitespaces and line breaks.
    """
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def normalize_text(text):
    import string
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text


def scrape_content(url : str) -> str:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = extract_text(soup)
        cleaned_text = clean_text(text)
        normalized_text = normalize_text(cleaned_text)

        return normalized_text
    # Extract relevant content
    except Exception as e:
        print(e)
        return None