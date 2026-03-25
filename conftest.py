# In this file, we define fixtures that can be used across multiple test files.
# This allows us to set up common test data or configurations that can be
# reused in different test cases.
#from email.policy import default

import pytest
import allure
from pathlib import *
from playwright.sync_api import *



#================================================================================
# PYTEST + PLAYWRIGHT TEST CONFIGURATION FILE
#================================================================================
# This file provides the below:
# 1. Command Line options (browser, base URL,video, screenshot)
# 2. Hooks to keep track on test results
# 3. Fixtures to set up and teardown
# 4. Screenshot , video and trace attachment in Allure Report
#================================================================================



#================================================================================
# STEP: 1 - Define Command Line Options
#================================================================================

def pytest_addoption(parser):
    parser.addoption("--browser", default="chromium", help="Browser to run tests on: chromium, firefox, webkit")
    parser.addoption("--headed", action="store_true", help="Run tests in headed mode")
    parser.addoption("--base-url", default="https://pd.kantimehealth.net/kantime/login.aspx", help="Base URL for the application under test")
    parser.addoption("--video", default="retain-on-failure", help="Video recording option: on, off, retain-on-failure")
    parser.addoption("--screenshot", default="only-on-failure", help="Screenshot option: on, off, only-on-failure")
    parser.addoption("--tracing", default="retain-on-failure", help="Tracing option: on, off, retain-on-failure")
    parser.addoption("--maximize", action="store_true", help="Maximize browser window")

#================================================================================
# STEP:2 Helper Function to Get Configuration Values
#================================================================================
def get_config_value(config, option_name):
    # Convert hyphen to underscore for attribute access (e.g., "base-url" -> "base_url")
    attr_name = option_name.replace('-', '_')
    # Try command line first - use the attribute name (with underscores)
    try:
        # For boolean flags like 'headed' that use store_true
        if option_name == "headed":
            cmd_value = getattr(config.option, attr_name, False)
        else:
            cmd_value = getattr(config.option, attr_name, None)

        if cmd_value is not None:
            return cmd_value
    except AttributeError:
        pass

    # Fall back to pytest.ini
    try:
        if option_name == 'headed':
            # For boolean values in ini file
            ini_value = config.getini(option_name)
            if isinstance(ini_value, str):
                return ini_value.lower() == "true"
            return bool(ini_value)
        else:
            ini_value = config.getini(option_name)
            if ini_value:
                return ini_value
    except ValueError:
        # Option not found in ini file
        pass


#================================================================================
# STEP:3  Hook to Track Test Results
#================================================================================
"""
hookwrapper = True -> this allows the hook to, run the code before the original hook

"""
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    """
    Captures the test result after each test execution.
    THis is used later to determine whether to take screenshot, Video or save traces.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)





#================================================================================
# STEP:4  Browser Context Fixture
#================================================================================
"""
Hirearchy of fixtures:
1. Playwright Fixture
2. Browser 
3. context 
4. page
"""
@pytest.fixture(scope='function')
def browser_context(request):
    # read configuration values

    browser_name = get_config_value(request.config, "browser")
    headed_flag = get_config_value(request.config, "headed")
    video_option = get_config_value(request.config, "video")


    #start playwright
    playwright = sync_playwright().start()

    #launch browser based on configuration
    if browser_name.lower() == "chromium":
        browser = playwright.chromium.launch(headless=not headed_flag)
    elif browser_name.lower() == "firefox":
        browser = playwright.firefox.launch(headless=not headed_flag)
    elif browser_name.lower() == "webkit":
        browser = playwright.webkit.launch(headless=not headed_flag)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # create context with video recording option
    if video_option in ["on", "retain-on-failure"]:
        context = browser.new_context(record_video_dir="C:/Pycharm/PythonProject/PythonProject1/PDProjectWithFW/reports")
    else:
        context = browser.new_context()

    #yield here is used to return the context to the test function and then resume here for cleanup after test execution
    yield context

    context.close()
    browser.close()
    playwright.stop()

#================================================================================
# STEP:5 Page Fixture
#================================================================================

@pytest.fixture(scope='function')
def page(request, browser_context):
    """
    1. Read the configuration file

    """

    # read configuration values
    base_url = get_config_value(request.config, "base-url")
    screenshot_option = get_config_value(request.config, "screenshot")
    tracing_option = get_config_value(request.config, "tracing")
    video_option = get_config_value(request.config, "video")
    maximize_flag = get_config_value(request.config, "maximize")


    print(f"Navigating to base URL: {base_url}")

    #start tracing if enabled
    if tracing_option in ["on", "retain-on-failure"]:
        browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)

    #create and navigate to base URL
    page = browser_context.new_page()

    # MAXIMIZE WINDOW IF REQUESTED - ADD THIS BLOCK
    if maximize_flag:
        # Get screen dimensions (you can adjust these values)
        page.set_viewport_size({"width": 1920, "height": 1080})
        print("🖥️ Browser window maximized to 1920x1080")

    page.goto(base_url, timeout=600000)

    #yield is used to return the page object to the test function
    yield page

    #=================================================================================
    # After the test:
    #=================================================================================

    test_name= request.node.name
    test_failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed

    # attach screenshot if test failed
    if test_failed and screenshot_option in ["on", "only-on-failure"]:
        screenshot_path = Path(f"C:/Pycharm/PythonProject/PythonProject1/PDProjectWithFW/reports/screenshots/{test_name}.png")
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name=f"{test_name}_screenshot", attachment_type=allure.attachment_type.PNG)

    # attach video if test failed
    if test_failed and video_option in ["on", "retain-on-failure"]:
        video_path = Path(f"C:/Pycharm/PythonProject/PythonProject1/PDProjectWithFW/reports/{test_name}.webm")
        if video_path.exists():
            allure.attach.file(video_path, name=f"{test_name}_video", attachment_type=allure.attachment_type.WEBM)

