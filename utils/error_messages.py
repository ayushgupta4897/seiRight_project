# error_messages.py
class ErrorMessages:
    MISSING_URLS = "Missing 'policy_url' or 'website_url' in the request."
    INVALID_POLICY_URL = "Invalid 'policy_url'."
    INVALID_WEBSITE_URL = "Invalid 'website_url'."
    SCRAPE_ERROR = "Error scraping content from one of the URLs."
    INTERNAL_SERVER_ERROR = "Internal server error. Please try again later."
