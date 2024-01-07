from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_execute_js():
    with webdriver.Chrome() as session:
        session.get("https://formy-project.herokuapp.com/modal")
        wait = WebDriverWait(session, 10)

        modal_btn = session.find_element(By.ID, "modal-button")
        modal_btn.click()
        modal_close_btn = wait.until(EC.element_to_be_clickable((By.ID, "close-button")))
        session.execute_script(
            "arguments[0].click();",
            modal_close_btn
        )



        time.sleep(5)
