from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_radio_button():
    with webdriver.Chrome() as session:
        session.get('https://formy-project.herokuapp.com/radiobutton')

        radio_btn_1 = session.find_element(By.CSS_SELECTOR, '#radio-button-1')
        radio_btn_1.click()
        sleep(5)
        radio_btn_2 = session.find_element(By.CSS_SELECTOR, 'input.form-check-input[value="option2"]')
        radio_btn_2.click()
        sleep(5)
        radio_btn_3 = session.find_element(By.XPATH, '/html/body/div/div[3]/input')
        radio_btn_3.click()

        sleep(5)

