from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def login(self,username,password):
        self.email = username
        self.password = password


        login_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='b2indexPage']/div[1]/div/header/nav[1]/div[2]/div/a"))
        )
        login_button.click()

        email_box = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='username']"))
        )
        email_box.send_keys(username)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()

        password_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
        password_box.send_keys(password)

        autentificare = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        autentificare.click()

