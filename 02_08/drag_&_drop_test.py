from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


def test_execute_js():
    with webdriver.Chrome() as session:
        session.get("https://formy-project.herokuapp.com/dragdrop")
        wait = WebDriverWait(session, 10)

        img = session.find_element(By.ID, "image")
        target_box = session.find_element(By.ID, "box")

        ActionChains(session).drag_and_drop(img, target_box).perform()

        time.sleep(5)
