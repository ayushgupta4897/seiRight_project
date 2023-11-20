from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from utils import gpt_client, prompts, scraping
from config import OPEN_AI_GPT_4, OPEN_AI_GPT_35_TURBO, OPEN_AI_GPT_4_TURBO

app = FastAPI()

def is_valid_url(url):
    """Check if the URL is valid."""
    return url.startswith('http://') or url.startswith('https://')

@app.post('/check-compliance')
async def check_compliance(request: Request):
    data = await request.json()

    # Validate URLs
    if 'policy_url' not in data or 'website_url' not in data:
        raise HTTPException(status_code=400, detail="Missing 'policy_url' or 'website_url' in the request")

    if not is_valid_url(data['policy_url']):
        raise HTTPException(status_code=400, detail="Invalid 'policy_url'")

    if not is_valid_url(data['website_url']):
        raise HTTPException(status_code=400, detail="Invalid 'website_url'")

    try:
        policy_text = scraping.scrape_content(data['policy_url'])
        website_text = scraping.scrape_content(data['website_url'])

        if policy_text is None or website_text is None:
            return JSONResponse({"error": "Error scraping content from one of the URLs"}, status_code=500)

        formatted_prompts = prompts.getPromptForComplianceReport(policy_text, website_text)
        compliance_report = gpt_client.GetResponseFromLLM(OPEN_AI_GPT_4, formatted_prompts)

        return {"Report": compliance_report}

    except Exception as e:
        # Generic error handling for any other unexpected issues
        return JSONResponse({"error": str(e)}, status_code=500)

@app.get('/health')
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
