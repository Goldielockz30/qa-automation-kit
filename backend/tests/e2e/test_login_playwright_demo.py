import os
import pathlib
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright


def _local_demo_url() -> str:
    return pathlib.Path("backend/tests/e2e/pages/login.html").resolve().as_uri()


def _is_file_url(url: str) -> bool:
    try:
        return urlparse(url).scheme == "file"
    except Exception:
        return False


def test_login_demo_headed_with_assert():
    # If E2E_URL is unset, use the bundled demo page
    url = os.getenv("E2E_URL") or _local_demo_url()

    # Demo creds (used only for the local demo page)
    username = os.getenv("E2E_USERNAME", "user")
    password = os.getenv("E2E_PASSWORD", "pass")

    with sync_playwright() as p:
        # Always show the browser for the demo (ignore HEADLESS)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        if _is_file_url(url):
            # Local demo page: fill & assert success, then pause for exploration
            page.fill("#username", username)
            page.fill("#password", password)
            page.click("#login")
            page.wait_for_selector("#msg")
            assert page.inner_text("#msg") == "Login successful"
            page.pause()
        else:
            # Real site: don't guess selectors—open and pause for manual login
            page.pause()

        browser.close()
