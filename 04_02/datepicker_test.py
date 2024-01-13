import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_deatepicker():
    with webdriver.Chrome() as session:
        session.get('https://formy-project.herokuapp.com/datepicker')

        date_field = session.find_element(By.CSS_SELECTOR, '#datepicker')
        date_field.click()

        datepicker_day = session.find_element(By.XPATH, '//td[ @class="day" and text() = "20" ]')
        date_val_ms = int(datepicker_day.get_attribute('data-date'))
        datepicker_day.click()

        visible_date = date_field.get_attribute('value')
        selected_date = datetime.datetime.fromtimestamp(date_val_ms / 1000.0)
        selected_date = selected_date.strftime("%m/%d/%Y")

        assert visible_date == selected_date
        time.sleep(3)
