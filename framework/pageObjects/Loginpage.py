import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    fname_id = "firstName"
    lname_xpath = '//*[@id="lastName"]'

    def __init__(self, driver):
        self.driver = driver

    def enter_user_fname(self, username):
        """Clear and enter first name."""
        self.driver.find_element(By.ID, self.fname_id).clear()
        self.driver.find_element(By.ID, self.fname_id).send_keys(username)

    def enter_user_lname(self, lastname):
        """Clear and enter last name."""
        self.driver.find_element(By.XPATH, self.lname_xpath).clear()
        self.driver.find_element(By.XPATH, self.lname_xpath).send_keys(lastname)



# from selenium import webdriver
# from selenium.webdriver.common.by import By

# class Test_Loginpage:
#     fname_id="firstName"
#     lname_xpath = '//*[@id="lastName"]'
#     def __init__(self,driver):
#         self.driver = driver
    
#     def Enter_user_fname(self,username):
#         self.driver.find_element(By.ID,self.fname_id).clear()
#         self.driver.find_element(By.ID,self.fname_id).send_keys(username)
    
        
