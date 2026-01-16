from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open login page
driver.get("http://127.0.0.1:5000")
time.sleep(1)

# Autofill username
driver.find_element(By.ID, "username").send_keys("nandhana")
time.sleep(1)

# Autofill email
driver.find_element(By.ID, "email").send_keys("nandhanaramesh1@gmail.com")
time.sleep(1)

# Click login button
driver.find_element(By.ID, "loginBtn").click()

time.sleep(3)
driver.quit()
