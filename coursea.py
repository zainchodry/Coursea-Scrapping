import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=options)

data = {
    "title": [],
    "description": [],
    "rating": [],
    "time_period": []
}

try:
    url = "https://www.coursera.org/search?page=2&query=python"
    print("Opening Coursera...")

    driver.get(url)
    time.sleep(random.uniform(2, 5))

    soup = BeautifulSoup(driver.page_source, "html.parser")
    instructions = soup.select("div.css-1whl2ol")

    for instruction in instructions:
        
        title_el = instruction.select_one('[id^="cds-react-aria-"][id$="-product-card-title"]')
        description_el = instruction.select_one("div.cds-ProductCard-body")
        rating_el = instruction.select_one("div.cds-RatingStat-sizeLabel.css-1i7bybc")
        time_period_el = instruction.select_one("div.cds-CommonCard-metadata")

        
        title = title_el.get_text(strip=True) if title_el else ""
        description = description_el.get_text(strip=True) if description_el else ""
        rating = rating_el.get_text(strip=True) if rating_el else ""
        time_period = time_period_el.get_text(strip=True) if time_period_el else ""

        
        data["title"].append(title)
        data["description"].append(description)
        data["rating"].append(rating)
        data["time_period"].append(time_period)

        
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Rating: {rating}")
        print(f"Time-Period: {time_period}")
        print("*" * 40)

    
    df = pd.DataFrame(data)
    df.to_csv("coursera.csv", index=False)
    df.to_excel("coursera.xlsx", index=False)

except Exception as e:
    print(f"An Exception occurred: {e}")

finally:
    driver.quit()
    print("Scraping Successfully Completed")
