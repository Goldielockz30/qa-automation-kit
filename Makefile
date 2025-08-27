.PHONY: init lint fmt test-unit test-api test-e2e test-all help e2e-headed e2e-trace demo-e2e

PY := $(shell command -v python3 >/dev/null 2>&1 && echo "python3 -m" || echo "python -m")
PIP := $(shell command -v pip3 >/dev/null 2>&1 && echo "pip3" || echo "pip")

COVERAGE_MIN ?= 70

REQ_FILE := $(if $(wildcard requirements.lock),requirements.lock,requirements.txt)

init:
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQ_FILE)
	$(PIP) install pre-commit
	pre-commit install
	$(PY) playwright install --with-deps

lint:
	ruff check .
	black --check .

fmt:
	black .
	ruff check . --fix
	pre-commit run --all-files || true

test-unit:
	pytest -q backend/tests/unit --cov=backend --cov-report=term-missing --cov-report=html --cov-fail-under=$(COVERAGE_MIN)

test-api:
	pytest -q backend/tests/api --maxfail=1

e2e-headed:
	PW_HEADLESS=0 pytest -q backend/tests/e2e --maxfail=1

e2e-trace:
	PWTRACE=1 pytest -q backend/tests/e2e --maxfail=1

test-all: lint test-unit test-api test-e2e

help:
	@echo "make init     - deps + hooks + Playwright browsers"
	@echo "make fmt      - format + fix + run hooks on all files"
	@echo "make lint     - ruff + black --check"
	@echo "make test-all - lint + unit + api + e2e (coverage gate $(COVERAGE_MIN)%)"

test-e2e:
	pytest -q backend/tests/e2e/test_login_playwright.py --maxfail=1

demo-e2e:
	pytest -q backend/tests/e2e/test_login_playwright_demo.py

test-e2e-all:
	pytest -q backend/tests/e2e --maxfail=1

