import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorect_username():
    driver = webdriver.Chrome(service=Service(r"C:\\Users\\User\\Valentyn_QA_AUTO\\chromedriver.exe"))

    driver.get('https://github.com/login')

    login_elem = driver.find_element(By.ID, 'login_field')
    login_elem.send_keys("valentiniisus")

    password_elem = driver.find_element(By.ID, 'password')
    password_elem.send_keys("wrong password")

    button = driver.find_element(By.NAME, 'commit')
    button.click()

    assert driver.title == 'Sign in to GitHub · GitHub'
    

    time.sleep(3)



    # driver.close()






