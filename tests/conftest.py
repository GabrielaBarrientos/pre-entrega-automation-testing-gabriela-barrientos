import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# El fixture para configurar y proporcionar el driver de Chrome a cualquier test que lo necesite.
@pytest.fixture
def driver():
    # Configurar el servicio de ChromeDriver.
    # webdriver-manager descarga el driver si es necesario y devuelve la ruta del ejecutable.
    service = Service(ChromeDriverManager().install())

    # Crear las opciones de configuración del browser Chrome.
    options = webdriver.ChromeOptions()

    # Configurar Chrome para que se inicie con la ventana maximizada.
    options.add_argument("--start-maximized")

    # Inicializar el browser con el servicio y las opciones configuradas.
    driver = webdriver.Chrome(service=service, options=options)

    # Entregar el driver al test que utiliza el fixture.
    yield driver

    # Cerrar el browser y finalizar la sesión de WebDriver cuando termina la ejecución del test.
    driver.quit()
