# Pre Entrega de Proyecto Final: Automatización de Login y Navegación Básica

Este proyecto **pre-entrega del Proyecto Final de Automation Testing (hasta la Clase 8)** implementa una automatización de pruebas para la aplicación SauceDemo, utilizando Selenium WebDriver y Python.

## Propósito del proyecto

El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:

1. Login con credenciales válidas e inválidas.
2. Verificación del catálogo de productos
3. Interacción con el carrito de compras (añadir productos y verificar su contenido)
4. Cierre de sesión

## Tecnologías utilizadas

- **Python:** lenguaje de programación de las pruebas.
- **Pytest:** framework para ejecutar y organizar los tests.
- **Selenium WebDriver:** automatización de interfaces web.
- **Git:** control de versiones.
- **GitHub:** alojamiento del repositorio de código del proyecto.
- **Google Chrome:** browser utilizado para ejecutar las pruebas.

## Organización del código

Estructura de referencia:

- `tests/test_saucedemo.py`: pruebas del login, inventario y carrito.
- `utils/helpers.py`: funciones auxiliares reutilizables.
- `utils/__init__.py`: identifica la carpeta `utils` como paquete de Python.
- `README.md`: descripción e instrucciones del proyecto.

## Requisitos previos

Tener instalados **Python** 3.7 o superior, **pip** y **Google Chrome**. Para trabajar con el repositorio también se necesita **Git**. Las versiones recientes de Selenium pueden gestionar automáticamente el controlador compatible con Chrome mediante Selenium Manager.

## Instalación de dependencias

Desde una terminal ubicada en la **raíz del proyecto**, ejecutar:

1. Crear un entorno virtual (recomendado): `python -m venv .venv`
2. Activarlo en **PowerShell (Windows)**: `.\.venv\Scripts\Activate.ps1`
3. Instalar las dependencias: `python -m pip install selenium pytest`


Si el proyecto incluye un archivo `requirements.txt`, se puede instalar desde él con `python -m pip install -r requirements.txt`.

## Cómo ejecutar las pruebas

Desde la **raíz del proyecto** ejecutar el archivo de test: 
`python -m pytest tests/test_saucedemo.py -v -s`

Para generar un reporte HTML: 
`python -m pytest -v --html=reports/reporte.html`

## Funcionalidades implementadas

Automatización de Login:
- Caso de éxito con credenciales válidas
- Caso de fallo con credenciales inválidas

Navegación y Verificación del Catálogo: 
- Comprobación del título de la página
- Verificación de presencia de productos
- Validación de elementos de la interfaz (menú, filtros, etc.)

Interacción con Productos:
- Añadir producto al carrito
- Verificar que el contador se incremente
- Navegar al carrito
- Comprobar que el producto añadido aparezca correctamente

Cierre de Sesión:
- Verificar que el usuario pueda cerrar sesión correctamente
