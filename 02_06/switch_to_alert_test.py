from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_switch_to_alert():
    with webdriver.Chrome() as session:
        session.get("https://formy-project.herokuapp.com/switch-window")

        new_alert_btn = session.find_element(By.ID, "alert-button")
        new_alert_btn.click()
        alert = session.switch_to.alert
        time.sleep(5)

        alert.accept()

        time.sleep(5)
