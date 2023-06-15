import pytest
import os
from io import open
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    actions = ActionChains(driver)
    driver.get("https://www.emag.ro/")
    driver.maximize_window()
    request.cls.driver= driver
    request.cls.actions = actions
    yield
    driver.close()




