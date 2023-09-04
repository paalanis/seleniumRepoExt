from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest


def Valida_objetos(driver,tipo,objeto):

    if tipo == "ID":
        try:
            elemento = driver.find_element(By.ID,objeto)
            assert elemento.is_displayed()
            print("Existe elemento: " + objeto)
            return elemento
        
        except NoSuchElementException:
            pytest.fail("No existe elemento: " + objeto)
    
    elif tipo == "XPATH":
        try:
            elemento = driver.find_element(By.XPATH,objeto)
            assert elemento.is_displayed()
            print("Existe elemento: " + objeto)
            return elemento
        
        except NoSuchElementException:
            pytest.fail("No existe elemento: " + objeto)
            
    elif tipo == "CLASS":
        try:
            elemento = driver.find_element(By.TAG_NAME,objeto)
            assert elemento.is_displayed()
            print("Existe elemento: " + objeto)
            return elemento
        
        except NoSuchElementException:
            pytest.fail("No existe elemento: " + objeto)        