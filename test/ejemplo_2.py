#LogIn correcto
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Arrange: Preparar
driver = webdriver.Chrome()
driver.get("https://rom0612.github.io/SistemaDeCamaras/")

# Act: Ejecutar
campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")

campos[0].send_keys("director.ti@gmail.com")
campos[1].send_keys("admin123")

driver.find_element(By.ID,"btnIngresar").click()

time.sleep(5)

# A: Verificar
assert "principal.html" in driver.current_url
print("Login exitoso")

#limpiar
driver.quit()