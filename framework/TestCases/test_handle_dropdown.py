import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Test_Dropdown:
    url = "https://demoqa.com/select-menu"

    def test_dropdown_andle(self,setup):
        driver = setup
        driver.get(self.url)
        wait = WebDriverWait(driver,20)
        ele = wait.until(EC.visibility_of_element_located((By.ID,'oldSelectMenu')))
        drop_down = Select(ele)

        # drop_down.select_by_visible_text("Indigo")
        # time.sleep(30)

        # drop_down.select_by_index(3)
        # time.sleep(30)

        # drop_down.select_by_value("4")
        # time.sleep(30)

        # all_options = drop_down.options

        # for option in all_options:
        #     print(option.text)