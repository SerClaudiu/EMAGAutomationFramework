from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver



    def scroll_to_element(self, element):
        self.element = element
        wait = WebDriverWait(self.driver, 10)
        scroll_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, element)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)

    #custom wait
    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_visibility_of_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element






