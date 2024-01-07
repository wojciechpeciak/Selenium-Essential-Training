from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_keyboard_and_mouse_input():
    with webdriver.Chrome() as session:
        session.get("https://formy-project.herokuapp.com/keypress")

        full_name_field = session.find_element(By.ID, 'name')
        full_name_field.click()
        full_name_field.send_keys("Wojciech Peciak")

        submit_btn = session.find_element(By.ID, "button")
        submit_btn.click()

        time.sleep(5)
