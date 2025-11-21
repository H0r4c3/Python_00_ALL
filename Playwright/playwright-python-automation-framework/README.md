# Playwright Framework Template (Python)

## Setup

```bash
python -m venv venv-playwright
venv-playwright\Scripts\activate  # Windows
# source venv-playwright/bin/activate  # Linux/Mac

pip install -r requirements.txt
playwright install
```

## One-time login (optional but recommended)

```bash
python tests/save_auth_state.py
```

This generates `auth_state.json` so all tests start already logged in.
Make sure in `config/config.json` you have:

```json
"auth_state": "auth_state.json"
```

## Run tests

```bash
pytest
pytest -m smoke
pytest -m regression
pytest -n 4
pytest --html=reports/report.html --self-contained-html
```

## Debugging

```bash
PWDEBUG=1 pytest -s
pytest --tracing=on
```

## Structure

- `pages/` – Page Object Model classes
- `tests/` – Test files + `conftest.py` with fixtures
- `config/` – Base config, environments, test data
- `utils/` – Helpers (config, API client, data reader, performance, network, a11y)
- `reports/` – HTML reports
- `screenshots/` – Screenshots on failure
- `traces/`, `videos/` – For recorded runs
```
