from selenium import webdriver
from selenium.webdriver.common.by import By

def pesquisar_nome_posto(endereco):
    driver = webdriver.Chrome()
    driver.get(endereco)
    elemento = driver.find_element(By.CLASS_NAME, 'hfpxzc')
    nome_do_posto = elemento.get_attribute("aria-label")
    print(nome_do_posto)
    driver.quit()
    return nome_do_posto
