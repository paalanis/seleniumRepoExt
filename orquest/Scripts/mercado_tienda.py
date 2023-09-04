from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from Objetos.Valida_objetos import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#cargamos archivo de mercados
filesheet = "DatosDePrueba/mercados_tiendas.xlsx"
wordbook = load_workbook(filesheet)
sheet = wordbook["Sheet1"]
wordbook.close()

#inicializamos mercados
mercado_test = sheet["A2"].value
tienda_test = sheet["B2"].value
mercado = sheet["D{}".format(mercado_test)]
tienda = sheet["F{}".format(tienda_test)]
print("mercado: "+mercado.value+" tienda: "+tienda.value)

#se seleccina mercado
def selecciona_mercado(driver):
    mercado_select = Valida_objetos(driver,"XPATH","//*[@id='serviceDashboardPage']/div/div[1]/div[1]/div/div[1]/div/span/span/span[1]")
    mercado_select.click()
    time.sleep(1)
    mercado_input = Valida_objetos(driver,"XPATH","/html/body/div[14]/div/span/input")
    #time.sleep(1)
    mercado_input.send_keys(mercado.value)
    time.sleep(1)
    mercado_input.send_keys(Keys.ENTER)
    time.sleep(3)
    print("mercado OK")

def selecciona_tienda(driver):    
    #tienda_select = Valida_objetos(driver,"XPATH","//*[@id='serviceDashboardPage']/div/div[1]/div[1]/div/div[2]/span/span/span[1]")
    #tienda_select.click()
    #time.sleep(3)
    #tienda_input = Valida_objetos(driver,"XPATH","/html/body/div[15]/div/span/input")
    #time.sleep(1)
    #tienda_input.send_keys(tienda.value)
    #time.sleep(1)
    #tienda_input.send_keys(Keys.ENTER)
    #time.sleep(3)
    print("tienda OK")
    
    
    #Seguimos con el ingreso da gestion de emplados/personas
    
    #//*[@id="serviceDashboardPage"]/div/div[1]/div[1]/div/div[1]/div/span
    #//*[@id="serviceDashboardPage"]/div/div[1]/div[1]/div/div[1]/div/span/span
    #//*[@id="serviceDashboardPage"]/div/div[1]/div[1]/div/div[1]/div/span/span/span[1]
    #//*[@id="serviceDashboardPage"]/div/div[1]/div[1]/div/div[1]/div/span/select
    #/html/body/div[14]/div/span/input /html/body/div[14]/div/span/input
    #/html/body/div[14]/div/div[2]/ul
    #//*[@id="serviceDashboardPage"]/div/div[1]/div[1]/div/div[2]/span/span/span[1]
    #/html/body/div[17]/div/span/input
    #/html/body/div[17]/div/span/input
    #/html/body/div[17]/div/span/input
    #/html/body/div[17]/div/span
    #xpath=//div[18]/div/span/input
    #//*[@id="serviceDashboardPage"]/div/div[1]/div[1]/div/div[2]/span/span/span[1]/text()
    #//*[@id="serviceDashboardPage"]/div/div[1]/div[1]/div/div[2]/span/span/span[1]
    #/html/body/div[17]/div/span
    #body > div:nth-child(57) > div > span > input
    #/html/body/div[17]/div/span/input
    #//*[@id="serviceDashboardPage"]/div/div[1]/div[1]/div/div[2]/span/span/span[1]
    #/html/body/div[15]/div/span/input
    