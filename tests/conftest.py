import base64
import datetime
import pytest
from playwright.sync_api import sync_playwright
from utils.config import BROWSER, HEADLESS, SLOW_MO
from utils.logger import logger

pytest_plugins = [
    "steps.practice_login_steps",
    "steps.checkboxes_steps",
    "steps.dropdown_steps",
    "steps.form_validation_steps",
    "steps.radio_buttons_steps",
]


@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as pw:
        browser_map = {
            "chromium": pw.chromium,
            "firefox": pw.firefox,
            "webkit": pw.webkit,
        }
        browser = browser_map.get(BROWSER, pw.chromium).launch(
            headless=HEADLESS, slow_mo=SLOW_MO
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser_instance):
    ctx = browser_instance.new_context(
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True,
    )
    yield ctx
    ctx.close()


@pytest.fixture(scope="function")
def page(context, request):
    pg = context.new_page()
    yield pg

    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        screenshot_bytes = pg.screenshot(full_page=True)
        encoded = base64.b64encode(screenshot_bytes).decode("utf-8")
        img_html = (
            f'<div style="margin-top:10px">'
            f'<b>Screenshot on failure:</b><br>'
            f'<img src="data:image/png;base64,{encoded}" '
            f'style="max-width:100%;border:1px solid #ccc;border-radius:4px;" />'
            f'</div>'
        )
        request.node._report_sections.append(("call", "Screenshot", img_html))
        logger.error(f"Screenshot captured for failed test: {request.node.name}")

    pg.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # noqa: ARG001
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def pytest_html_report_title(report):
    report.title = "Sample App — BDD Test Report"


def pytest_configure(config):
    config._metadata = {
        "Project":     "Sample App BDD Suite",
        "Browser":     BROWSER.capitalize(),
        "Headless":    str(HEADLESS),
        "Environment": "CI",
        "Executed at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
