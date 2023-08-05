from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pytest



@pytest.mark.test
def test_rept_shot():
    driver = webdriver.Chrome(service=Service(r"C:\\Users\\User\\Valentyn_QA_AUTO\\chromedriver.exe"))
    driver.get('https://all4terr.com.ua/')


    button = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/header/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/nav/ul/li[2]/span/a')
    button.click()


    found = driver.find_element(By.NAME, 'value')
    found.send_keys('Термокилимок')


    svg_search_button = driver.find_element(By.CSS_SELECTOR, '[data-component="store-search-form-trigger"]')
    svg_search_button.click()
    

    order_button = driver.find_element(By.CLASS_NAME, 'name_zKO')
    order_button.click()


    quatity = driver.find_element(By.CLASS_NAME, 'quantity-input_2vS')
    quatity.send_keys(999)


    order_box = driver.find_element(By.CSS_SELECTOR, 'a.js-buy-button.buy-button_1Xp.button_2W3.ui-button.ui-button--primary-light.ui-button--size-md[data-test="buy-button"][data-component="button')
    order_box.click()


    basket = driver.find_element(By.CSS_SELECTOR, 'div.wrapper_1mY.js-cart-widget.w-icon-panel.w-icon-panel--md.position-horizontal-right_1fr.position-vertical-top_1nn.shape-circle_2Qo[data-always-show="false"][data-test="cart-widget"]')
    basket.click()
    time.sleep(0.5)
    
    name = driver.find_element(By.CSS_SELECTOR, 'input.form__input_38Y.ui-input.ui-input--size-md.w-form__input[name="41b00716-cd8c-4ca5-aa6e-bcf5f72e39e5"]')
    name.send_keys('Валентиииииииииииииииииииииииин')
    time.sleep(0.5)
    
    number_of_phone = driver.find_element(By.CSS_SELECTOR, 'input[type="phone"][name="7a4bc839-2535-40c0-9d31-fd319d63fe38"]')
    number_of_phone.send_keys(+3809666666)
    time.sleep(0.5)
    
    accept_type = driver.find_element(By.CLASS_NAME, 'dropdown-wrapper_2i-')
    accept_type.click()
    time.sleep(0.5)
    
    accept_type_button = driver.find_element(By.XPATH, '//*[@id="blockId-608816e3ad820d002168fc01"]/section/div[1]/div/div/div/div/div/div[3]/div/form/div[3]/div[2]/div/div/div[2]/div[3]/span')
    accept_type_button.click()
    time.sleep(0.5)
    
    comment = driver.find_element(By.NAME, '10d1f695-b733-434b-b78c-58d3e19c4d74')
    comment.send_keys('Вибачте будь ласка, пишу автотести =(')
    time.sleep(0.5)
    
    post = driver.find_element(By.XPATH, '/html/body/div/div/div[5]/div[1]/div[3]/section/div[1]/div/div/div/div/div/div[4]/div[5]')
    post.click()    
    time.sleep(0.5)

    post_index = driver.find_element(By.XPATH, '//*[@id="blockId-608816e3ad820d002168fc01"]/section/div[1]/div/div/div/div/div/div[4]/div[4]')
    post_index.click()
    time.sleep(0.5)
    
    buy_button = driver.find_element(By.CSS_SELECTOR, 'a.js-order-button.w-btns-group__item.button_2W3.w-button.ui-button.ui-button--primary-light.ui-button--size-lg[data-test="order-button"]')
    buy_button.click()




    time.sleep(5)
    assert driver.title == 'monobank'
    
    
    driver.close()

    

