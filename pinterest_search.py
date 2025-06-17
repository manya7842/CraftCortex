from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_pinterest_tutorial(query):
    search_url = f"https://www.pinterest.com/search/pins/?q={query.replace(' ', '%20')}%20origami"

    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(search_url)
    time.sleep(3)

    pins = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/pin/"]')
    results = set()

    for pin in pins:
        href = pin.get_attribute('href')
        results.add(href)
        if len(results) >= 5:
            break

    driver.quit()
    return list(results)