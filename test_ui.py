from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_example_domain_page_loads():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://example.com")

        page_title = driver.title
        header_text = driver.find_element(By.TAG_NAME, "h1").text

        assert page_title == "Example Domain"
        assert header_text == "Example Domain"

    finally:
        driver.quit()