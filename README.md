# Meme API Testing Project
**About the Project**

This repository contains an API test automation project for a Meme service.
It demonstrates REST API testing practices including request validation, response verification, and error handling.

## Project structure:
- endpoints - API request methods
- tests/ - API test cases
- .gitignore - ignored files
- README.md - project documentation
- conftest.py - fixtures and setup
- data.py - test data generation functions for API requests
- pytest.ini - pytest configuration
- requirements.txt - dependencies
  
**What is tested**

🔐 Authorization and token validation

📥 Get all memes
 
📄 Get meme by ID
 
➕ Create meme
 
✏️ Update meme
 
❌ Delete meme

**Test scenarios**


- Positive scenarios:
  - Successful requests (200 OK)

- Negative scenarios:
  - Unauthorized access (401)
  - Forbidden access (403)
  - Resource not found (404)
  - Method not allowed (405)
  - Invalid request data (400)
  - Server error handling (500)

- Response validation:
  - Response body structure
  - Data correctness and consistency

**How to run tests**

```bash
pip install -r requirements.txt

pytest
```


Run tests with Allure report:

```bash
pytest --alluredir=allure-results

allure serve allure-results
```


**Tech stack**

- Python

- pytest

- Requests

- Allure

