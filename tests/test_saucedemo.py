from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import *  # Importar todas las funciones auxiliares

URL_SAUCEDEMO = "https://www.saucedemo.com/"

# Test de login con credenciales válidas
def test_login_exitoso(driver):
    """
    Caso de Prueba de Login: Login exitoso con credenciales válidas.
    Verifica que el usuario pueda iniciar sesión y es redirigido a la página de inventario.
    """
    # Navegar a la página de login de SauceDemo.
    driver.get(URL_SAUCEDEMO)

    # Localizar el campo de usuario e ingresar una credencial válida.
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    # Localizar el campo de contraseña e ingresar la contraseña válida.
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Hacer clic en el botón de login.
    driver.find_element(By.ID, "login-button").click()
  
    # Esperar explícitamente hasta que la URL contenga "/inventory.html".
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))

    # Validar que el login fue exitoso mediante la URL de inventario.
    assert "/inventory.html" in driver.current_url, "El login falló: no se redirigió a la página de inventario"

    print("✅ Login exitoso completado")


# Test de navegación y verificación del catálogo de productos
def test_navegacion_catalogo(driver):
    """
    Caso de prueba: Verificación del catálogo de productos.
    Verifica que el título de la página sea correcto, que existan productos y elementos principales.
    """

    # Configurar una espera explícita de hasta 10 segundos.
    wait = WebDriverWait(driver, 10)

    # Realizar login con credenciales válidas
    login_helper(driver, "standard_user", "secret_sauce")
    
    # Verificar el título de la página
    assert driver.title == "Swag Labs", "El título de la página es incorrecto"

    print("\nTítulo de la página validado:", driver.title)

    # Esperar hasta que la URL corresponda a la página de inventario.
    wait.until(EC.url_contains("/inventory.html"))

    # Esperar hasta que el título del catálogo sea visible.
    titulo_catalogo = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "title")
        )
    )

    # Verificar que el título del catálogo sea el esperado.
    assert titulo_catalogo.text == "Products", "El título del catálogo es incorrecto"

    print("Título del catálogo validado:", titulo_catalogo.text)

    # Guardar los elementos encontrados en la lista 'productos'.
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    # Verificar que hay productos visibles
    assert len(productos) > 0, "No se encontraron productos visibles en la página"

    print("Productos visibles:", len(productos))

    # Localizar el botón del menú de navegación mediante su ID.
    menu = driver.find_element(By.ID, "react-burger-menu-btn")

    # Verificar que el botón del menú esté visible.
    assert menu.is_displayed(), "El menú de navegación no está visible"

    print("Menú de navegación validado")

    # Localizar el selector de ordenamiento de productos mediante su clase CSS.
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    # Verificar que el selector de ordenamiento esté visible.
    assert filtro.is_displayed(), "El filtro de productos no está visible"

    print("Filtro de productos validado")

    # Localizar el ícono del carrito mediante su clase CSS.
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    
    # Verificar que el ícono del carrito esté visible.
    assert carrito.is_displayed(), "El ícono del carrito no está visible"
    
    print("Ícono del carrito validado")

    print("✅ Verificación del catálogo completada")


# Test de interacción con productos y carrito
def test_carrito(driver):
    """
    Caso de prueba: Interacción con productos y carrito.
    Añade un producto al carrito, verifica que el contador se incremente,
    verifica el producto añadido en el carrito.
    """

    # Configurar una espera explícita de hasta 10 segundos.
    wait = WebDriverWait(driver, 10)

    # Realizar login con credenciales válidas
    login_helper(driver, "standard_user", "secret_sauce")

    # Localizar el primer producto del catálogo.
    primer_producto = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    # Obtener el nombre del primer producto para verificarlo posteriormente en el carrito.
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    # Agregar el primer producto al carrito
    boton_agregar = primer_producto.find_element(By.CLASS_NAME, "btn_inventory")
    boton_agregar.click()

    print("Producto agregado:", nombre_producto)

    # Verificar el botón de "Remove" para confirmar que el producto fue agregado al carrito.
    boton_remover = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "btn_inventory")
        )
    )

    assert boton_remover.text.capitalize() == "Remove", "El botón no cambió a 'Remove' después de agregar al carrito"

    print("Botón de 'Remove' validado")

    # Esperar hasta que el contador del carrito sea visible.
    contador = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    # Verificar que el contador del carrito muestre 1.
    assert contador.text == "1", "El contador del carrito no muestra 1"

    print("Contador del carrito validado:", contador.text)

    # Localizar el enlace al carrito de compras.
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    # Hacer clic para ingresar al carrito.
    carrito.click()

    # Esperar la redirección a la página del carrito.
    wait.until(EC.url_contains("/cart.html"))

    assert "/cart.html" in driver.current_url, "No se redirigió a la página del carrito"

    # Obtener el nombre del producto en el carrito.
    nombre_producto_carrito = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    # Verificar que el producto agregado aparezca en el carrito.
    assert nombre_producto == nombre_producto_carrito.text, "El producto agregado no aparece en el carrito"

    print("✅ Verificación del carrito completada")
