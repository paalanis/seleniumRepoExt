from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from Objetos.Valida_objetos import *

#cargamos archivo de credenciales
filesheet = "DatosDePrueba/login.xlsx"
wordbook = load_workbook(filesheet)
sheet = wordbook["Sheet1"]
wordbook.close()

#inicializamos la url y credenciales
row_test = sheet["A2"].value
user = sheet["C{}".format(row_test)]
password = sheet["D{}".format(row_test)]
url = sheet["E{}".format(row_test)]

def login(driver):    
    
    #abrimos aplicación Orquest
    driver.get(url.value)
    driver.maximize_window()
    time.sleep(2)

    #inicializamos y validamos objetos    
    user_input = Valida_objetos(driver,"ID","username")
    password_input = Valida_objetos(driver,"ID","password")
    login_btn = Valida_objetos(driver,"XPATH","//div[@id='loginPanel']/div/form/div[5]")
    
    user_input.send_keys(user.value)
    password_input.send_keys(password.value)
    time.sleep(1)
    login_btn.click()

    time.sleep(5)
    print("login OK!")
    

