import pathlib
import os

from playwright.sync_api import sync_playwright


def test_login_local_page() -> None:
    html_path = pathlib.Path("backend/tests/e2e/pages/login.html").resolve().as_uri()
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(html_path)
        page.fill("#username", "user")
        page.fill("#password", "pass")
        page.click("#login")
        assert "Login successful" in page.text_content("#msg")
        page.screenshot(path="playwright-report/login_success.png")
        browser.close()
