import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testiframes:
    url = "https://demoqa.com/frames"

    def test_iframes_001(self,setup):
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        ele = driver.find_element(By.XPATH,'//*[@id="frame1"]')
        driver.switch_to.frame(ele)
        ele2 = driver.find_element(By.TAG_NAME,"h1")
        print("########",ele2.text)
        print("come back to original frame")
        driver.switch_to.default_content()
        element2 = driver.find_element(By.XPATH,'//*[@id="framesWrapper"]/h1').text
        print(element2)

        


