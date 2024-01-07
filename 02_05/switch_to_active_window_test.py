from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_switch_to_active_window():
    with webdriver.Chrome() as session:
        session.get("https://formy-project.herokuapp.com/switch-window")

        new_tab_btn = session.find_element(By.ID, "new-tab-button")
        new_tab_btn.click()
        origin_handle = session.current_window_handle

        for handle in session.window_handles:
            session.switch_to.window(handle)
            time.sleep(5)
        session.switch_to.window(origin_handle)
        time.sleep(5)
