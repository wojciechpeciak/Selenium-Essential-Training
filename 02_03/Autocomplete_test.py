from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_autocomplete():
    with webdriver.Chrome() as session:
        session.get("https://formy-project.herokuapp.com/autocomplete")

        full_address_field = session.find_element(By.ID, 'autocomplete')
        full_address_field.click()
        full_address_field.send_keys("1555 Park Blvd, Palo Alto, CA")

        autocomplete_result = session.find_element(By.CSS_SELECTOR, "pac-item")
        autocomplete_result.click()

        time.sleep(5)
