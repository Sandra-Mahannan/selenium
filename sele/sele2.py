from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Configure Chrome options and provide the path to the Chrome driver.
opt = Options()
opt.add_argument("--start-maximized")  # Maximize the browser window.
chr_drv = r'C:\Users\HP\Desktop\chromedriver-win64'

# Initialize the Chrome WebDriver.
driver = webdriver.Chrome(executable_path=chr_drv, options=opt)

url = 'https://www.nytimes.com/'

# Open the website.
driver.get(url)

# Define a WebDriverWait with a maximum wait time.
wait = WebDriverWait(driver, 20)  # Adjust the wait time as needed.

try:
    # Wait for the pop-up to appear (using the expected conditions).
    popup = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='complianceOverlay']/div")))  # Replace with the correct selector.

    # Once the pop-up is found, locate and click the "Continue" button.
    continue_button = popup.find_element(By.XPATH, "//*[@id='complianceOverlay']/div/button")  # Replace with the correct selector.
    continue_button.click()
except NoSuchElementException:
    # Handle the case where the pop-up didn't appear within the specified time.
    print("Pop-up did not appear within the given time.")

# Continue with the rest of your automation tasks.

# Close the browser when you're done.
driver.quit()





from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.NoAlertPresentException; 
# import org.openqa.selenium.Alert;
#from bs4 import BeautifulSoup 


opt = Options()
chr_drv = r'C:\Users\HP\Desktop\chromedriver-win64'

driver = webdriver.Chrome(options=opt)

url = 'https://www.nytimes.com/'

driver.get(url)


# Define a WebDriverWait with a maximum wait time.
#wait = WebDriverWait(driver, 10)  # Adjust the wait time as needed.

# try:
#     # Wait for the pop-up to appear (using the expected conditions).
#     popup = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id="complianceOverlay"]/div")))  # Replace with the correct selector.

#     # Once the pop-up is found, locate and click the "Continue" button.
#     continue_button = popup.find_element(By.XPATH, "//*[@id="complianceOverlay"]/div/button")  # Replace with the correct selector.
#     continue_button.click()
# except Exception as e:
#     # Handle the case where the pop-up didn't appear within the specified time.
#     print("Pop-up did not appear within the given time.")

# #This should look for the "X" on the pop up and close it.
# #driver.findElement(By.xpath("//*[@id="popsubform"]/a/img")).click();

# myFindElement(String xpath)
# {
#     try{
#         driver.findElement(By.xpath("//*[@id="complianceOverlay"]/div/button"))
#     }
#     catch (ElementNotFoundException e){
#         if !closethepopup(){print ('Element not found')}
#     }
#     catch (GeneralException ge){
#     }
# }

# try:
#     # Locate and click the "Continue" button (replace with the appropriate selector).
#     continue_button = driver.find_element_by_id("continue-button")  # Replace with the correct selector.
#     continue_button.click()
# except NoSuchElementException:
#     # Handle the case when the pop-up is not present.
#     print("Pop-up not found, continuing with the rest of the code.")

#driver.quit()



