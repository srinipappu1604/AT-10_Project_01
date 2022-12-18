from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Login:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Chrome()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
    
    def test_get_title(self, booting_function):
        try:
            self.driver.get(self.url)
            assert self.driver.title == "OrangeHRM"
            print("WEB TITLE CAPTURED SUCCESSFULLY")
        except:
            print("ERROR IN THE FUCTION - test_get_title")
        
    def test_edit(self, booting_function):
        try:
            self.driver.get(self.url)
            time.sleep(5)
            self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_username).send_keys(data.Orange_Login.username)
            time.sleep(3)
            self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_password).send_keys(data.Orange_Login.password)
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.login_xpath).click()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.pim_module_click).click()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.pim_select_edit).click()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.pim_edit_existing_user).click()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.employee_id).send_keys(data.edit_emp.employeeid)
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.edit_save).click()
            assert self.driver.title == "OrangeHRM"
            print("EMPLOYEE ID EDITED SUCCESSFULLY")
        except:
            print("ERROR IN THE FUCTION - test_edit")
