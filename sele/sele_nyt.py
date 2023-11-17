from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

opt = Options()
chr_drv = r'C:\Users\HP\Desktop\chromedriver-win64'

driver = webdriver.Chrome(options=opt)

# Set up the webdriver (for this example, I'm using Chrome)
driver = webdriver.Chrome()  # Replace 'path_to_chromedriver' with the path to your chromedriver

# Open the New York Times website
driver.get("https://www.nytimes.com/")

# Wait for up to 20 seconds for the 'Continue' button to appear, then click it
try:
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.css-1fzhd9j"))
    )
    continue_button.click()
    print('Button Clicked now waiting for the browser')
    time.sleep(10)
except:
    print("The 'Continue' button was not found within 20 seconds!")




# Continue with the rest of your script or close the browser
# driver.quit()