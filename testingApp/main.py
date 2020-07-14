
"""
from selenium import webdriver
import os
import time

chrome_options= webdriver.ChromeOptions()
chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)

print('Test to know if selenium is working properly...')
url='https://sjf.scjn.gob.mx/SJFSist/Paginas/DetalleGeneralV2.aspx?ID=159819&Clase=DetalleTesisBL&Semanario=0'
driver.get(url)
time.sleep(1)

print(driver.page_source)
"""

print('Testing working well..')

