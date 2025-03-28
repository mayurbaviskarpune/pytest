import pytest
from conftest import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testalert:
    url = "https://demoqa.com/alerts"

    # def test_handle_alert_popup(self,setup):
    #     driver = setup
    #     driver.get(self.url)
    #     driver.maximize_window()
    #     alert_butn = driver.find_element(By.XPATH,'//*[@id="alertButton"]')
    #     alert_butn.click()
    #     time.sleep(20)
    #     alert = driver.switch_to.alert
    #     alert.accept()

    # def test_handle_prompt_alert_popup(self,setup):
    #     driver = setup
    #     driver.get(self.url)
    #     driver.maximize_window()
    #     wait = WebDriverWait(driver,10)
    #     ele = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="promtButton"]')))
    #     ele.click()
    #     alert = driver.switch_to.alert
    #     alert.send_keys("mayur")
    #     time.sleep(20)
    #     alert.accept()
    #     time.sleep(20)
        
    