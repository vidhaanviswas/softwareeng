from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.pesuacademy.com/Academy/")

time.sleep(2)

username_input = driver.find_element(By.XPATH, '//*[@id="j_scriptusername"]')
password_input = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/form/fieldset/div[2]/input') 

username_input.send_keys("test_username") 
password_input.send_keys("test_password") 

login_button = driver.find_element(By.XPATH, '//*[@id="postloginform#/Academy/j_spring_security_check"]') 
login_button.click()

time.sleep(5)

if "studentProfilePESU" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed or credentials invalid.")

driver.quit()