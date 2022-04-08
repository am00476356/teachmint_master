import pytest
from library.config import Config
from selenium import webdriver

@pytest.fixture(autouse=True, scope="class")
def _driver():
    global driver
    if Config.BROWSER_NAME.upper() == 'CHROME':
        driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
    elif Config.BROWSER_NAME.upper() == 'FIREFOX':
        driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH)
    else:
        driver = webdriver.Ie(Config.IE_DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    driver.quit()

#
# def _capture_screenshot():
#     return driver.get_screenshot_as_base64()


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         xfail = hasattr(report, "wasfail")
#         # if report: # attaches screenshots for all steps
#         if (report.skipped and report.fail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.image(_capture_screenshot()))
#         report.extra = extra