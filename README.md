Automatización de pruebas con Selenium y Pytest – SauceDemo

Este proyecto contiene un conjunto de pruebas automatizadas para el sitio web https://www.saucedemo.com
, utilizando Python, Selenium WebDriver y Pytest.
PRE-ENTREGA-TESTING_AUTOMATION/


tests/

└── test_saucedemo.py 
# Archivo con los casos de prueba
utils/

└── helpers.py
# Funciones reutilizables (driver y login)

README.md

requirements.txt

Instalación y configuración
pip install -r requirements.txt

Cómo ejecutar las pruebas:

Desde la terminal, dentro del proyecto
pytest -v

Generar reporte en HTML de las pruebas realizadas:
pytest pre-entrega-testing_automation/test_saucedemo.py -v --html=reporte.html
