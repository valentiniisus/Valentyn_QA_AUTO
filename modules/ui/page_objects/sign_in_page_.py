from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class Sign_In(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Sign_In.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, 'login_field')
        login_elem.send_keys(username)

        password_elem = self.driver.find_element(By.ID, 'password')
        password_elem.send_keys(password)

        button = self.driver.find_element(By.NAME, 'commit')

        button.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title




    