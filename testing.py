from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"C:\Users\Rehaan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

import random
username = "rehan" + str(random.randint(1000, 9999))
password = "rehanpass999"
file_path = r"C:\Users\Rehaan\Downloads\gw.jpeg"

driver.get("http://127.0.0.1:8000/signup/")
time.sleep(1)

driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "email").send_keys("testuser@gmail.com")
driver.find_element(By.NAME, "password1").send_keys(password)
driver.find_element(By.NAME, "password2").send_keys(password)
driver.find_element(By.NAME, "role").send_keys("user")
driver.find_element(By.TAG_NAME, "form").submit()
time.sleep(2)

driver.get("http://127.0.0.1:8000/login/")
time.sleep(1)

driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.TAG_NAME, "form").submit()
time.sleep(2)

if driver.current_url == "http://127.0.0.1:8000/upload/":
    print("✅ Login successful, now uploading file...")
else:
    print("❌ Login failed or wrong redirect. Current URL:", driver.current_url)
    driver.quit()
    exit()

driver.find_element(By.NAME, "file").send_keys(file_path)
driver.find_element(By.TAG_NAME, "form").submit()
time.sleep(2)

if driver.current_url == "http://127.0.0.1:8000/upload/":
    print("✅ File uploaded successfully!")
else:
    print("❌ File upload failed. Current URL:", driver.current_url)

driver.quit()


