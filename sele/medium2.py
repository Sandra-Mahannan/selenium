import os
from selenium import webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

pd.set_option("display.max_columns", None)
driver = webdriver.Chrome(options=chrome_options)

os.environ["PATH"] += r"C:/SeleniumDrivers"

#url = "https://nike.com"
url = "https://edition.cnn.com/"
driver = webdriver.Chrome()
driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(15)


# for nav_link in nav_links: 
#     driver.find_elements(By.CLASS_NAME, "header__inner")
# nav_link.click()

# for nav_link in driver.find_elements(By.CLASS_NAME, "header__inner"):
#     nav_link.click()

nav_links = driver.find_elements(By.CLASS_NAME, "header__inner")

# Iterate through the links and click on each one
for nav_link in nav_links:
    nav_link.click()
    print(nav_link.text)




# # Wait for the "Next" button to be clickable
# wait = WebDriverWait(driver, 15)
# next_button = wait.until(EC.element_to_be_clickable((By.XPATH,'.//a[@class="fright fs14 btn-secondary br2"]')))

# # Click the "Next" button
# next_button.click()

# # Wait for the page to load (sleep for 15 seconds)
# time.sleep(15)

# story_link = driver.find_element(By.CLASS_NAME, "container__headline-text")
# story_link.click()
# review_button_element = driver.find_element(By.CSS_SELECTOR, '[data-test="reviewsAccordionClick"]')
# review_button_element.click()

# more_review_button_element = driver.find_element(By.CSS_SELECTOR,'[for="More Reviews"]')
# more_review_button_element.click()

# count = int(driver.find_element(by=By.CSS_SELECTOR,
#                             value='[aria-level="2"]'
#                            ).get_attribute("innerText")[:2])

# content2 = []

# for i  in range(mt.ceil(count/16)):
    
#     review_element  = driver.find_element(By.ID, "tt-reviews-list")
#     reviews = review_element.find_elements(By.CLASS_NAME, "tt-c-review")

#     for review in reviews:
#         try:
#             inner = review.get_attribute("innerText")
#             outer = review.get_attribute("OuterText")
#             content2.append([inner, outer])
#         except:
#             content2.append(["Null", "Null"])

#         more_review_button_element2 = driver.find_element(By.CSS_SELECTOR,'[aria-label="Go to next reviews"]')
#         more_review_button_element2.click()
# review_button_element = driver.find_element(By.CSS_SELECTOR, '[data-test="reviewsAccordionClick"]')
# review_button_element.click()

# more_review_button_element = driver.find_element(By.CSS_SELECTOR,'[for="More Reviews"]')
# more_review_button_element.click()

# count = int(driver.find_element(by=By.CSS_SELECTOR,
#                             value='[aria-level="2"]'
#                            ).get_attribute("innerText")[:2])

# content2 = []

# for i  in range(mt.ceil(count/16)):
    
#     review_element  = driver.find_element(By.ID, "tt-reviews-list")
#     reviews = review_element.find_elements(By.CLASS_NAME, "tt-c-review")

#     for review in reviews:
#         try:
#             inner = review.get_attribute("innerText")
#             outer = review.get_attribute("OuterText")
#             content2.append([inner, outer])
#         except:
#             content2.append(["Null", "Null"])

#         more_review_button_element2 = driver.find_element(By.CSS_SELECTOR,'[aria-label="Go to next reviews"]')
#         more_review_button_element2.click()

# #The function performs all the procedures mentioned above.
# def fetch_reviews(product_number):
#     """
#     The function fetches users comment from nike.com
#     -Arguments:
#         product_number: This selects the product number on the search_list

#     -Returns:
#         Customer Reviews
#     """
    
#     url = "https://www.nike.com"
#     driver = webdriver.Chrome()
#     driver.get(url=url)
#     driver.maximize_window()
#     driver.implicitly_wait(15)


#     #click the terms and conditions button
#     try:
#         confirm_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Accept All']")
#         confirm_button.click()
#     except:
#         print(f"No confirm button")

#     #click the geomix match dismiss button
#     try:
#         button = driver.find_element(By.CSS_SELECTOR, 'button[data-type="click_geoMismatchDismiss"]')
#         button.click()
#     except:
#          print("Geo-dismiss button didn't pop up")

#     search = driver.find_element(by=By.ID, value="VisualSearchInput")
#     search.send_keys("shoe")
#     search.send_keys(Keys.ENTER)

#     #click the terms and conditions button
#     try:
#         confirm_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Accept All']")
#         confirm_button.click()
#     except:
#         print(f"No confirm button")

#     #click possible pop up button
#     try:
#         close_button = driver.find_elements(by=By.CSS_SELECTOR, value="button[data-var= 'closeButton']")
#         close_button.click()
#     except:
#         print("No pop up icon to close")

#     #click the geomix match dismiss button
#     try:
#         button = driver.find_element(By.CSS_SELECTOR, 'button[data-type="click_geoMismatchDismiss"]')
#         button.click()
#     except:
#          print("Geo-dismiss button didn't pop up")
            
#     xpath = f'//*[@id="skip-to-products"]/div[{product_number}]'
#     product = driver.find_element(By.XPATH, xpath)
#     product.click()

#     review_button_element = driver.find_element(By.CSS_SELECTOR, '[data-test="reviewsAccordionClick"]')
#     review_button_element.click()

#     more_review_button_element = driver.find_element(By.CSS_SELECTOR,'[for="More Reviews"]')
#     more_review_button_element.click()

#     count = int(driver.find_element(by=By.CSS_SELECTOR, value='[aria-level="2"]').get_attribute("innerText")[:2])

#     content = []

#     for i  in range(mt.ceil(count/16)):

#         review_element  = driver.find_element(By.ID, "tt-reviews-list")
#         reviews = review_element.find_elements(By.CLASS_NAME, "tt-c-review")

#         for review in reviews:
#             try:
#                 inner = review.get_attribute("innerText")
#                 outer = review.get_attribute("OuterText")
#                 content.append([inner, outer])
#             except:
#                 content.append(["Null", "Null"])

#             more_review_button_element2 = driver.find_element(By.CSS_SELECTOR,'[aria-label="Go to next reviews"]')
#             more_review_button_element2.click()
            
#     return len(content), content

