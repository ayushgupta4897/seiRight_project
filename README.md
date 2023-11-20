
---

# SeiRight Compliance Report API


## Overview

This project consists of several Python modules designed to interact with OpenAI's GPT models and perform web scraping. It includes modules for making requests to OpenAI's API, generating prompts for compliance reports, and scraping and processing web content.


## Installation and Running the Application

### Installing Dependencies

Before running the application, you need to install the required Python packages. These packages are listed in the `requirements.txt` file. To install them, follow these steps:

1. **Create a Virtual Environment** (optional, but recommended):
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Requirements**:
   
   Navigate to the directory where `requirements.txt` is located and run:

   ```bash
   pip install -r requirements.txt
   ```

This will install FastAPI, Uvicorn, and other necessary dependencies for the project.

### Running the Application

Once the dependencies are installed, you can start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```


### Testing the API

To test the API, you can use `curl` commands or tools like Postman. Here's an example `curl` request to the `/check-compliance` endpoint:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/check-compliance' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"policy_url": "https://stripe.com/docs/treasury/marketing-treasury", "website_url": "https://www.joinguava.com/"}'
```


## Modules

### 1. gpt_client.py

This module interfaces with OpenAI's GPT models. It sends a prompt to the model and retrieves the response. The `GetResponseFromLLM` function takes a model identifier and a prompt string, sends it to OpenAI's Chat Completion API, and returns the response.

### 2. prompts.py

This module contains functions for creating formatted prompts for various tasks. The `getPromptForComplianceReport` function takes text extracted from two webpages and generates a detailed prompt asking GPT to create a compliance report based on the input texts.

### 3. scraping.py

Handles the scraping of web content. This module contains functions to request webpage content, extract text using BeautifulSoup, and clean and normalize this text for further processing or analysis.

### 4. config.py

Manages configuration and environment variables. It includes settings for OpenAI API keys and model identifiers.

### 5. main.py (FastAPI Integration)
This file creates a FastAPI application.
Defines API endpoints that utilize the above modules.
Includes a /check-compliance POST endpoint for processing compliance checks.
Provides a /health GET endpoint for health checks of the service.

## Usage

Examples of how to use each module:

### gpt_client.py

```python
from gpt_client import GetResponseFromLLM
response = GetResponseFromLLM(model="gpt-4", prompt="Hello, world!")
```

### prompts.py

```python
from prompts import getPromptForComplianceReport
prompt = getPromptForComplianceReport(compliance_text, webpage_text)
```

### scraping.py

```python
from scraping import scrape_content
webpage_text = scrape_content("https://example.com")
```

