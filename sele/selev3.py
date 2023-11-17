from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
chr_drv = r'C:\Users\HP\Desktop\chromedriver-win64'

driver = webdriver.Chrome(options=opt)
url = 'https://www.nytimes.com/'
driver.get(url)

# Wait for the popup to appear, then click the continue button (or whatever the button might be labeled)
try:
    # Adjust the CSS selector according to the actual element you want to click.
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1fzhd9j"))
    )
    continue_button.click()
except Exception as e:
    print(f"Error: {e}")
    # If there's no popup, the script will just continue

# Additional code for further interactions or scraping goes here...

#driver.quit()