from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#driver=navegador
driver = webdriver.Chrome()
#abrir navegador
driver.get("https://search.brave.com")
time.sleep(1)

busqueda = driver.find_element(By.NAME,"q")
busqueda.send_keys("Facultad de Ingeniería")
time.sleep(2)
busqueda.send_keys(Keys.ENTER)

time.sleep(5)

#cerrar navegador
driver.quit()