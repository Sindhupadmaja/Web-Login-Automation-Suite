# Project 1 — Web Login Automation Suite

Foundation SDET/QA automation project.

## Scope
Automates positive, negative, boundary, and validation scenarios for a sample login application.

## Stack
Python, Pytest, Selenium WebDriver, pytest-html, python-dotenv.

## Engineering practices
- Page Object Model
- Fixtures
- Parameterization
- Explicit waits
- Assertions
- Failure screenshots
- HTML reporting
- Smoke/regression markers
- Headless execution
- Basic GitHub Actions CI

Default application: `https://www.saucedemo.com/`

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
pytest -m smoke
pytest --html=reports/report.html --self-contained-html
```

This project intentionally stays focused on UI automation fundamentals. API, database, advanced CI/CD, contract testing and service virtualization are introduced in Projects 2–4.
