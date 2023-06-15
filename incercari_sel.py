import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://www.emag.ro/")
cont = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@id='my_account']")))
cont.click()


time.sleep(3)


