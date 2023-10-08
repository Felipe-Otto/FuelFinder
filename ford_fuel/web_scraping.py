import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  # Importe as opções do Chrome aqui
from resources.utils import confirmador_posto

def obter_elementos(driver, by, value):
    try:
        elementos = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((by, value))
        )
        return elementos
    except Exception as e:
        print(f"Erro ao obter elementos: {e}")
        return []

def pesquisar_nome_posto(url, cep):
    try:
        # Configurar as opções do Chrome para modo headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Executar em modo headless

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        elementos = obter_elementos(driver, By.CLASS_NAME, 'hfpxzc')
        if not elementos:
            elemento = obter_elementos(driver, By.CLASS_NAME, 'DUwDvf ')[0].text
            if not elemento:
                elemento = obter_elementos(driver, By.CLASS_NAME, 'hfpxzc ')[0].text
            else:
                return elemento
        postos = {}
        links = []

        if len(elementos) > 3:
            elementos = elementos[:3]

        for elemento in elementos:
            postos[elemento.get_attribute("aria-label")] = elemento.get_attribute("href")

        enderecos = endereco_posto(driver, postos)
        posto = confirmador_posto(enderecos, cep)

        if posto is not None:
            return posto
        else:
            return 'Não há posto'

    finally:
        driver.quit()

def endereco_posto(driver, postos):
    link_falha = []

    for i, link in enumerate(postos.values()):
        try:
            driver.get(link)
            endereco = obter_elementos(driver, By.CLASS_NAME, 'Io6YTe')[0].text
            nome = obter_elementos(driver, By.CLASS_NAME, 'DUwDvf ')[0].text
            if endereco:
                postos[nome] = endereco  # Atualize o dicionário postos com os novos valores
            else:
                link_falha.append(link)  # Adicione à cópia da lista link_falha
        except Exception as e:
            print(f'Erro ao obter endereço: {e}')

    while True:
        if link_falha:
            for link in link_falha:
                try:
                    driver.get(link)
                    endereco = obter_elementos(driver, By.CLASS_NAME, 'Io6YTe')[0].text
                    nome = obter_elementos(driver, By.CLASS_NAME, 'DUwDvf ')[0].text
                    if endereco:
                        postos[nome] = endereco  # Atualize o dicionário postos com os novos valores
                    else:
                        link_falha.append(link)  # Adicione à cópia da lista link_falha
                except Exception as e:
                    print(f'Erro ao obter endereço: {e}')
        return postos