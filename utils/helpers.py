
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By # llama a cualquier selector mediante by
import time

URL_LOGIN = "https://www.saucedemo.com/"

def login_helper(driver, username, password):
    """
    Realiza el inicio de sesión en SauceDemo.
    
    Args:
        driver: Instancia del WebDriver
        username: Nombre de usuario
        password: Contraseña
    """
    
    # Abrir la página de login
    driver.get("https://www.saucedemo.com/")
    
    # Esperar a que el formulario de login sea visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    
    # Ingresar credenciales
    username_input.send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    
    # Hacer clic en el botón de login
    driver.find_element(By.ID, "login-button").click()
    
    # Esperar a que se complete el login
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )




def add_product_to_cart(driver, product_index=0):
    """
    Añade un producto específico al carrito.
    
    Args:
        driver: Instancia del WebDriver
        product_index: Índice del producto a añadir (por defecto, el primero)
        
    Returns:
        str: Nombre del producto añadido
    """
    from selenium.webdriver.common.by import By
    
    # Obtener todos los productos
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    if product_index >= len(products):
        raise IndexError(f"Índice de producto {product_index} fuera de rango (hay {len(products)} productos)")
    
    # Obtener el producto específico
    product = products[product_index]
    
    # Obtener el nombre del producto
    product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    # Añadir al carrito
    add_button = product.find_element(By.XPATH, ".//button[contains(@data-test, 'add-to-cart')]")
    add_button.click()
    
    return product_name

def get_cart_count(driver):
    """
    Obtiene el número de productos en el carrito.
    
    Args:
        driver: Instancia del WebDriver
        
    Returns:
        int: Número de productos en el carrito, 0 si está vacío
    """
    from selenium.webdriver.common.by import By
    
    try:
        badge = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return int(badge.text)
    except TimeoutException:
        # Si no hay badge, el carrito está vacío
        return 0