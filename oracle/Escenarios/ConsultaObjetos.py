from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import pytest
import time
from Scripts.login import *
from Scripts.pruebaObjetos import *
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    
    """options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)"""
    driver = webdriver.Chrome()
    
    yield driver
    driver.quit()

def test_consulta_id(driver):
    login(driver) 
    recorre_objetos(driver)

