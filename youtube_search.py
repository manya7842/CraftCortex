from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_youtube_tutorial(query):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}+craft+tutorial"
        driver.get(search_url)
        time.sleep(3)

        video_links = []
        elements = driver.find_elements(By.CSS_SELECTOR, 'a#video-title') 
        for el in elements[:5]:
            link = el.get_attribute('href')
            if link and 'watch?v=' in link:
                video_links.append(link)
            if len(video_links) >= 5:
                break
        return video_links

    finally:
        driver.quit()