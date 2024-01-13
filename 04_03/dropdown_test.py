import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dropdown():
    with webdriver.Chrome() as session:
        session.get('https://formy-project.herokuapp.com/dropdown')
        wait = WebDriverWait(session, 5)

        dropdown_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#dropdownMenuButton')
        ))
        dropdown_btn.click()
        scroll_option = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a.dropdown-item[href="/scroll"]')
        ))
        session.execute_script("arguments[0].click()", scroll_option)

        time.sleep(3)



