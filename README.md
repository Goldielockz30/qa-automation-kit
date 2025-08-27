# 🧪 QA Automation Kit

<!-- === CORE BADGES (Kit, Pro, Master) === -->
![CI](https://github.com/Goldielockz30/qa-automation-kit/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

<!-- === EXTRA BADGES (Pro & Master only) === -->
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker&logoColor=white)
![Playwright](https://img.shields.io/badge/tested%20with-Playwright-45ba4b?logo=playwright)


A **plug-and-play QA Automation Kit** with FastAPI, pytest, and Playwright.  
Built for **job‑ready automation skills** and smooth local/CI workflows.

---

## ⚙️ Prerequisites

- 🖥 VS Code — Python & Docker extensions recommended  
- 🐍 Python 3.10+  
- 🔧 Git for version control  
- 🐙 GitHub account (optional for CI)  
- 🪟 WSL2 (Windows) — run Linux commands inside Windows easily  
- 🐳 Docker (Optional) — CLI preferred for lightweight use, Desktop for GUI  

➡️ See [docs/prerequisites.md](docs/prerequisites.md) for full setup details.

---

## 🚀 Quickstart

```bash
# 1. Create project
git clone https://github.com/Goldielockz30/qa-automation-kit.git

# 2. Go inside
cd qa-automation-kit

# 3. Install & init
make init

# 4. Format & test
make fmt && make test-all

# 5. Demo (headed browser, always visible)
make demo-e2e
```

---

## 🧪 Running Tests

- **Lint & format**  
  ```bash
  make fmt
  make lint
  ```

- **Unit tests (with coverage)**  
  ```bash
  make test-unit
  ```

- **API tests**  
  ```bash
  make test-api
  ```

- **E2E tests (CI-safe, headless)**  
  ```bash
  make test-e2e
  ```

- **E2E Demo (always headed, interactive)**  
  ```bash
  make demo-e2e
  ```

---

## 🔑 Demo Instructions

- By default, `make demo-e2e` runs against the **bundled demo login page** (`backend/tests/e2e/pages/login.html`).  
  - Credentials: `user` / `pass`  
  - Demo asserts `"Login successful"` and pauses for inspection.

- To test a **real login page** (e.g. Facebook):  
  1. Edit `.env` and **uncomment `E2E_URL`**, set it to your target login page:  
     ```env
     E2E_URL=https://www.facebook.com/login
     ```
  2. Run:  
     ```bash
     make demo-e2e
     ```
  3. Browser opens, test **pauses for manual login**.

- **Headless toggle**:  
  - Demo ignores `HEADLESS` and always shows the browser.  
  - CI tests (`make test-e2e`) respect `HEADLESS` in `.env`.

---

## 📂 Project Structure

➡️ See [docs/folder-structure.md](docs/folder-structure.md) for the complete layout.

---

## ✅ Notes

- **Demo always opens a visible browser.**  
- For CI or headless runs, use `make test-e2e`.  
- Switch between demo and real apps just by editing `.env`.  
