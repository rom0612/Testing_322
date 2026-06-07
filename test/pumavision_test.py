import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL = "https://rom0612.github.io/SistemaDeCamaras/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

def test_carga_pagina(driver):
    driver.get(URL)
    assert "Login - Seguridad" in driver.title

def test_login_correcto(driver):
    driver.get(URL)
    time.sleep(2)
    
    campos = driver.find_elements(By.CLASS_NAME, "entradaTexto")
    campos[0].send_keys("director.ti@gmail.com")
    campos[1].send_keys("admin123")
    
    driver.find_element(By.ID, "btnIngresar").click()
    time.sleep(4)
    
    driver.save_screenshot("evidencias/pytest_login_exitoso.png")
    
    assert "principal.html" in driver.current_url

def test_login_incorrecto(driver):
    driver.get(URL)
    time.sleep(2)
    
    campos = driver.find_elements(By.CLASS_NAME, "entradaTexto")
    campos[0].send_keys("hacker@gmail.com")
    campos[1].send_keys("hackerman123")
    
    driver.find_element(By.ID, "btnIngresar").click()
    time.sleep(4)
    
    driver.save_screenshot("evidencias/pytest_login_fallido.png")
    
    assert "principal.html" not in driver.current_url
if __name__ == "__main__":
    pytest.main(["-v", __file__])
