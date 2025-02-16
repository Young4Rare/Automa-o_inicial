import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Caminho para o arquivo Excel
CAMINHO_ARQUIVO = "usuarios.xlsx"


# Função para carregar os dados do Excel
def carregar_usuarios(caminho):
    df = pd.read_excel(caminho)
    return df


# Função para iniciar o Chrome
def iniciar_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


# Função para criar usuários no sistema corporativo
def criar_usuario(driver, usuario):
    driver.get("URL_DO_SISTEMA_CORPORATIVO")  # Alterar para a URL real
    time.sleep(3)  # Tempo para carregar a página

    # Exemplo de preenchimento de um formulário (ajuste os seletores conforme necessário)
    driver.find_element(By.NAME, "nome").send_keys(usuario['Nome'])
    driver.find_element(By.NAME, "cpf").send_keys(str(usuario['CPF']))
    driver.find_element(By.NAME, "rg").send_keys(str(usuario['RG']))
    driver.find_element(By.NAME, "data_nascimento").send_keys(str(usuario['Data de Nascimento']))
    driver.find_element(By.NAME, "login").send_keys(usuario['Login'])
    driver.find_element(By.NAME, "email").send_keys(usuario['Email'])

    driver.find_element(By.NAME, "submit").click()  # Botão de envio
    time.sleep(2)  # Espera a ação ser processada


# Fluxo principal
def main():
    usuarios = carregar_usuarios(CAMINHO_ARQUIVO)
    driver = iniciar_navegador()

    for _, usuario in usuarios.iterrows():
        criar_usuario(driver, usuario)
        print(f"Usuário {usuario['Nome']} criado com sucesso!")

    driver.quit()


if __name__ == "__main__":
    main()