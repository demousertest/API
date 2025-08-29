from selenium import webdriver
import pytest

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver
@pytest.fixture()
def setup():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=http://<PROXY_SERVER>:<PORT>')
    # Add options to prevent Chrome from detecting automation
    # options.add_argument(
    #     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    #
    # options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation detection
    # options.add_argument("--headless")  # Run Chrome in headless mode (optional)
    # options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    # options.add_argument("--no-sandbox")  # Needed for CI environments
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--incognito')
    # options.set_preference("dom.webdriver.enabled", False)

    # Create the driver with the options
    driver = webdriver.Chrome(options=options)

    # Return the driver instance
    yield driver

    # Cleanup after the test (close the driver)
    driver.quit()