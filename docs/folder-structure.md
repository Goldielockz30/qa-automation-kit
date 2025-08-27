```
qa-automation-kit/
├── backend/
│   ├── src/
│   │   ├── app.py
│   │   └── utils.py
│   └── tests/
│       ├── unit/
│       │   ├── __init__.py
│       │   ├── test_utils.py
│       │   └── test_app.py
│       ├── api/
│       │   ├── __init__.py
│       │   └── test_health.py
│       └── e2e/
│           ├── __init__.py
│           ├── pages/
│           │   └── login.html
│           ├── test_login_playwright.py
│           └── test_login_playwright_demo.py
├── docs/
│   ├── prerequisites.md
│   └── folder-structure.md
├── .coveragerc
├── .dockerignore
├── .editorconfig
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── Makefile
├── pytest.ini
├── README.md
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml
```