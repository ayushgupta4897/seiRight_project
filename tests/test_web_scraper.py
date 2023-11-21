import unittest
from unittest.mock import patch, MagicMock
from utils.web_scraper import WebScraper
from bs4 import BeautifulSoup

class TestWebScraper(unittest.TestCase):

    def setUp(self):
        self.valid_url = "https://stripe.com/docs/treasury/marketing-treasury"
        self.invalid_url = "https://www.invalidurl.com/fsdvfsvfv"
        self.scraper = WebScraper(self.valid_url)

    @patch('requests.get')
    def test_successful_scraping(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, content=b"<html><body>Test Content</body></html>")
        result = self.scraper.scrape_content()
        self.assertIsNotNone(result)
        self.assertIn("test content", result)

    @patch('requests.get')
    def test_invalid_url(self, mock_get):
        mock_get.side_effect = Exception("Connection error")
        self.scraper.url = self.invalid_url
        result = self.scraper.scrape_content()
        self.assertIsNone(result)

    def test_extract_text(self):
        html_content = "<html><head><title>Test</title></head><body>Sample <script>ignore this</script></body></html>"
        soup = BeautifulSoup(html_content, 'html.parser')
        extracted_text = self.scraper.extract_text(soup)
        self.assertIn("Sample", extracted_text)
        self.assertNotIn("ignore this", extracted_text)


    def test_clean_text(self):
        dirty_text = "  Hello \n World  \n"
        clean_text = self.scraper.clean_text(dirty_text)
        self.assertEqual(clean_text, "Hello\nWorld")

    def test_normalize_text(self):
        text = "Hello, World!"
        normalized_text = self.scraper.normalize_text(text)
        self.assertEqual(normalized_text, "hello world")

if __name__ == '__main__':
    unittest.main()
