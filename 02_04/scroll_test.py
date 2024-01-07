from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def test_scroll():
    with webdriver.Chrome() as session:
        session.get("https://formy-project.herokuapp.com/scroll")

        name_input = session.find_element(By.ID, "name")
        ActionChains(session)\
            .move_to_element(name_input)\
            .perform()
        name_input.send_keys("Wojciech Peciak")
        time.sleep(5)
