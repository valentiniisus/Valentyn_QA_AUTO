from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class Order(BasePage):
    URL = 'https://all4terr.com.ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to_the_order(self, product_name, quantity):
        self.driver.get(Order.URL)

        button = self.driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/header/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/nav/ul/li[2]/span/a')
        button.click()

        found = self.driver.find_element(By.NAME, 'value')
        found.send_keys(product_name)

        svg_search_button = self.driver.find_element(By.CSS_SELECTOR, '[data-component="store-search-form-trigger"]')
        svg_search_button.click()
        
        order_button = self.driver.find_element(By.CLASS_NAME, 'name_zKO')
        order_button.click()

        quatity = self.driver.find_element(By.CLASS_NAME, 'quantity-input_2vS')
        quatity.send_keys(quantity)

        order_box = self.driver.find_element(By.CSS_SELECTOR, 'a.js-buy-button.buy-button_1Xp.button_2W3.ui-button.ui-button--primary-light.ui-button--size-md[data-test="buy-button"][data-component="button')
        order_box.click()

        basket = self.driver.find_element(By.CSS_SELECTOR, 'div.wrapper_1mY.js-cart-widget.w-icon-panel.w-icon-panel--md.position-horizontal-right_1fr.position-vertical-top_1nn.shape-circle_2Qo[data-always-show="false"][data-test="cart-widget"]')
        basket.click()

        time.sleep(0.5)

    def order_info(self, enter_name, enter_number_of_phone, enter_comment):
        name = self.driver.find_element(By.XPATH, '//input[@name="41b00716-cd8c-4ca5-aa6e-bcf5f72e39e5"]')
        name.send_keys(enter_name)

        
        number_of_phone = self.driver.find_element(By.CSS_SELECTOR, 'input[type="phone"][name="7a4bc839-2535-40c0-9d31-fd319d63fe38"]')
        number_of_phone.send_keys(enter_number_of_phone)
        time.sleep(0.5)
        
        accept_type = self.driver.find_element(By.CLASS_NAME, 'dropdown-wrapper_2i-')
        accept_type.click()
        time.sleep(0.5)
        
        accept_type_button = self.driver.find_element(By.XPATH, '//*[@id="blockId-608816e3ad820d002168fc01"]/section/div[1]/div/div/div/div/div/div[3]/div/form/div[3]/div[2]/div/div/div[2]/div[3]/span')
        accept_type_button.click()
        time.sleep(0.5)
        
        comment = self.driver.find_element(By.NAME, '10d1f695-b733-434b-b78c-58d3e19c4d74')
        comment.send_keys(enter_comment)
        time.sleep(0.5)
        
        post = self.driver.find_element(By.XPATH, '/html/body/div/div/div[5]/div[1]/div[3]/section/div[1]/div/div/div/div/div/div[4]/div[5]')
        post.click()    
        time.sleep(0.5)

        post_index = self.driver.find_element(By.XPATH, '//*[@id="blockId-608816e3ad820d002168fc01"]/section/div[1]/div/div/div/div/div/div[4]/div[4]')
        post_index.click()
        time.sleep(0.5)
    
        buy_button = self.driver.find_element(By.CSS_SELECTOR, 'a.js-order-button.w-btns-group__item.button_2W3.w-button.ui-button.ui-button--primary-light.ui-button--size-lg[data-test="order-button"]')
        buy_button.click()

    def check_title(self, enter_title):
        return self.driver.title == enter_title

    

    

    


    

    



