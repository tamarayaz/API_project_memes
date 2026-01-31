# Meme API Testing Project
**About the Project**

This repository contains an **API test automation project** for a Meme service, created as a practical learning project.
It demonstrates core approaches to **REST API testing with Python** using pytest and Allure.

**What Is Tested**

🔐 Authorization and token validation

📥 Get all memes

📄 Get meme by ID

➕ Create meme

✏️ Update meme

❌ Delete meme

**Test Scenarios**


- Positive cases (200 OK)

- Unauthorized access (401)

- Forbidden access (403)

- Not found (404)

- Method not allowed (405)

- Bad requests (400)

- Server errors (500)

- Response body structure and data validation

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


**Tech Stack**

- Python

- pytest

- Requests

- Allure

