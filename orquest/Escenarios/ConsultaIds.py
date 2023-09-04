from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import pytest
import time
from Scripts.login import *
from Scripts.mercado_tienda import *

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_consulta_id(driver):
    login(driver)
    selecciona_mercado(driver)
    selecciona_tienda(driver)

