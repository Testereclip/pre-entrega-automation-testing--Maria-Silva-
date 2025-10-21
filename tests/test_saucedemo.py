import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils.helpers import login_saucedemo, get_driver
import time

@pytest.fixture
def driver():
    #configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()


def test_login(driver):
     login_saucedemo(driver)
     assert "/inventory.html" in driver.current_url
     titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
     titulo_logo = driver.find_element(By.CLASS_NAME, "app_logo").text
     assert titulo_logo == "Swag Labs"
     assert  titulo == 'Products'

    #logeo de usuario con username y password
    #click al boton de login

    #redirija a la pagina de inventario

    #verifica el titulo de la pagina
def test_catalago(driver):
      login_saucedemo(driver)
      products = driver.find_elements(By.CLASS_NAME, 'inventory_list')
      assert len(products) > 0
   
def test_carrito(driver):
    login_saucedemo(driver)
        
    #logeo del usuario con username y password
    #click al boton de login
    products = driver.find_elements(By.CLASS_NAME, 'inventory_list')
    total_products = len(products)
    products[0].find_element(By.TAG_NAME,'button').click()
    badge = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text
    time.sleep(7)
        #incremento de carrito al agregar un producto
    assert badge == "1"
    #llevarme a la pagina de carrito de compras
    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    producto_correcto = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
    #comprobar que el carrito aparezca el producto correcto
    assert producto_correcto == 'Sauce Labs Backpack'



