import pytest
from conftest import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Login:
    url = "https://demoqa.com/automation-practice-form"

    # def test_url(self,setup):
    #     driver = setup
    #     driver.get(self.url)
    #     print(driver.title)
    #     assert True


    # def test_enter_name_lname(self,setup):
    #     driver = setup
    #     driver.get(self.url)
    #     driver.maximize_window()
    #     fname = driver.find_element(By.ID,"firstName")
    #     fname.send_keys("mayur")
    #     fname.send_keys(Keys.TAB)
    #     lname = driver.find_element(By.XPATH,'//*[@id="lastName"]')
    #     for i in "baviskar":
    #         lname.send_keys(i)
    #     time.sleep(30)

    # def test_dropdown_state_city(self,setup): 
    #     driver = setup
    #     driver.get(self.url)
    #     driver.maximize_window()
    #     time.sleep(30)
    #     state_dropdown=driver.find_element(By.XPATH,'//*[@id="stateCity-wrapper"]//div[@id="state"]')
    #     driver.execute_script("arguments[0].scrollIntoView();",state_dropdown)
    #     state_dropdown.click()
    #     time.sleep(10)
    #     wait = WebDriverWait(driver, 10)
    #     option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Uttar Pradesh']")))
    #     option.click()


    # def test_scroll_page_by_key(self,setup):
    #     driver = setup
    #     driver.get(self.url)
    #     driver.maximize_window()
    #     body = driver.find_element(By.TAG_NAME, "body")
    #     body.send_keys(Keys.PAGE_DOWN)  # Scroll down
    #     time.sleep(3)
    #     body.send_keys(Keys.ARROW_DOWN)
    #     time.sleep(3) 
    #     body.send_keys(Keys.ARROW_DOWN) 
    #     time.sleep(3)
    #     body.send_keys(Keys.ARROW_DOWN) 
    #     body.send_keys(Keys.PAGE_UP)  # Scroll up
    #     body.send_keys(Keys.ARROW_DOWN)  # Scroll slightly down
    #     body.send_keys(Keys.ARROW_UP)  # Scroll slightly up    


    
