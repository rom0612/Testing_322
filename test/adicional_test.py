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

def test_navegacion_registro(driver):
    driver.get(URL)
    time.sleep(2)
    
    try:
        btn_registro = driver.find_element(By.CSS_SELECTOR, "a[href='pages/registro.html']")
        btn_registro.click()
        time.sleep(3)
        
        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot("evidencias/pytest_vista_registro.png")
        
        assert True 
    except Exception as e:
        os.makedirs("evidencias", exist_ok=True)
        driver.save_screenshot("evidencias/pytest_error_registro.png")
        raise e
if __name__ == "__main__":
    pytest.main(["-v", __file__])