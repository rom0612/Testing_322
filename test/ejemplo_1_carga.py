#Prueba 1: ver si la página abre

from selenium import webdriver
import io
# Arrange: Preparar
driver = webdriver.Chrome()

# Act: Ejecutar
driver.get("https://rom0612.github.io/SistemaDeCamaras/")

# A: Verificar
assert "Login - Seguridad" in driver.title
print("El sistema cargó correctamente")
print("Título: ", driver.title)
driver.save_screenshot("evidencias/ejemplo_1_carga.png")
#limpiar
driver.quit()
