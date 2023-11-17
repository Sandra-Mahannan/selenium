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
driver.get("https://edition.cnn.com/")






# Continue with the rest of your script or close the browser
# driver.quit()