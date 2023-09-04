from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def Valida_objetos(driver,tipo,objeto):

    if tipo == "ID":
        try:
            elemento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, objeto)))
            print("Existe elemento: " + objeto)
            return elemento
        
        except NoSuchElementException:
            pytest.fail("No existe elemento: " + objeto)
    
    elif tipo == "XPATH":
        try:
            elemento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, objeto)))
            print("Existe elemento: " + objeto)
            return elemento
        
        except NoSuchElementException:
            pytest.fail("No existe elemento: " + objeto)
            
    elif tipo == "CLASS":
        try:
            elemento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, objeto)))
            print("Existe elemento: " + objeto)
            return elemento
        
        except NoSuchElementException:
            pytest.fail("No existe elemento: " + objeto)        