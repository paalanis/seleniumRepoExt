from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time
from selenium.common.exceptions import NoSuchElementException
from Scripts.Valida_objetos import *
from Objetos.objetos import *

#cargamos archivo de credenciales
filesheet = "DatosDePrueba/login.xlsx"
wordbook = load_workbook(filesheet)
sheet = wordbook["Sheet1"]
wordbook.close()

#inicializamos la url y credenciales
row_test = sheet["A2"].value
userData = sheet["C{}".format(row_test)]
passwordData = sheet["D{}".format(row_test)]
url = sheet["E{}".format(row_test)]

def login(driver):    
    
    #abrimos aplicación
    driver.get(url.value)
    driver.maximize_window()
    driver.implicitly_wait(10)
    

    #inicializamos y validamos objetos    
    user_ = Valida_objetos(driver,"XPATH",user)
    password_ = Valida_objetos(driver,"XPATH",password)
    loginButton_ = Valida_objetos(driver,"XPATH",loginButton)
    
    #enviamos datos
    user_.send_keys(userData.value)
    password_.send_keys(passwordData.value)
    time.sleep(1)
    loginButton_.click()
    
    print("login OK!")
    

