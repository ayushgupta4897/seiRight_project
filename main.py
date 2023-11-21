import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from utils.web_scraper import WebScraper
from utils.gpt_client import GPTClient
from utils.prompts import Prompts
from config import OPEN_AI_GPT_4, OPEN_AI_GPT_4_TURBO
from utils.error_messages import ErrorMessages

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
gpt_client = GPTClient()

def is_valid_url(url):
    """Check if the URL is valid."""
    return url.startswith('http://') or url.startswith('https://')

def scrape_content(url: str) -> str:
    scraper = WebScraper(url)
    content = scraper.scrape_content()
    if content is None:
        logger.error(f"Failed to scrape content from {url}")
    return content

@app.post('/check-compliance')
async def check_compliance(request: Request):
    data = await request.json()

    # Validate URLs
    if 'policy_url' not in data or 'website_url' not in data:
        raise HTTPException(status_code=400,
                            detail=ErrorMessages.MISSING_URLS)

    if not is_valid_url(data['policy_url']):
        raise HTTPException(status_code=400,
                            detail=ErrorMessages.INVALID_POLICY_URL)

    if not is_valid_url(data['website_url']):
        raise HTTPException(status_code=400,
                            detail=ErrorMessages.INVALID_WEBSITE_URL)

    try:
        policy_text = scrape_content(data['policy_url'])
        website_text = scrape_content(data['website_url'])

        if policy_text is None or website_text is None:
            logger.error(ErrorMessages.SCRAPE_ERROR)
            return JSONResponse({"error": ErrorMessages.INTERNAL_SERVER_ERROR}, status_code=500)

        formatted_prompts = Prompts.get_prompt_for_compliance_report(policy_text, website_text)
        compliance_report = gpt_client.get_response_from_llm(OPEN_AI_GPT_4, formatted_prompts)

        return {"Report": compliance_report}

    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JSONResponse({"error": ErrorMessages.INTERNAL_SERVER_ERROR}, status_code=500)

@app.get('/health')
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
