from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from Scripts.Valida_objetos import *
from Objetos.objetos import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#recorremos la lista de ojetos de la tabla
def recorre_objetos(driver):
 
   objeto_a = Valida_objetos(driver,"XPATH",navigator)
 
   objeto_a.click()
   time.sleep(10)

   objeto_b = Valida_objetos(driver,"XPATH",salesArrow)
   
   objeto_b.click()
   time.sleep(10)
   
   objeto_c = Valida_objetos(driver,"XPATH",workspace)
   
   objeto_c.click()
   time.sleep(10)

    