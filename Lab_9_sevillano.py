from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

#--------parte 1

driver = webdriver.Edge('C:/Selenium/edgedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

#--------parte 2
keyword = "computer"
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys(keyword)
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()
item = driver.find_element(By.CLASS_NAME, 'a-link-normal')
item.click()
cantidad = driver.find_element(By.CLASS_NAME, 'a-dropdown-label')
cantidad.click()
numero = driver.find_element(By.ID, 'quantity_1')
numero.click()
botoncar = driver.find_element(By.ID, 'add-to-cart-button')
botoncar.click()
carrito = wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'attach-sidesheet-view-cart-button')))
carrito.click()

driver.close()