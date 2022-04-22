import os
from selenium import webdriver
from webdriver_manager import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
# os.system('cls')
x = int(0)
valor = int(0)
valorl = int(0)
nome = str(valor)
num = int(input("Quantidade de Pessoas: "))
Mensagem = str(input("Mensagem: "))
os.system('cls')
while(100 != x):
    os.system('cls')
    x = x + 20
    print("▒█░▒█ █▀▀ █░░ █░░ █▀▀█")
    print("▒█▀▀█ █▀▀ █░░ █░░ █░░█")
    print("▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀")
    print("\n\n\n CARREGANDO...%", x)
    time.sleep(1)
time.sleep(3)
file = open('nomes.txt', 'r')
time.sleep(1)
file = open('nomes.txt', 'r')


class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = Mensagem
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem2
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(service=Service(
            executable_path=chrome.ChromeDriverManager().install(), ))

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        y = int(0)
        while(y != num):
            y = y + 1
            nome = file.readline()
            print(nome)
            nome = nome.rstrip('\n')
            botao_chat = self.driver.find_element_by_xpath(
                "//span[@data-icon='chat']")
            botao_chat.click()
            time.sleep(1)
            campo_grupo = self.driver.find_element_by_xpath(
                "//div[@title='Caixa de texto de pesquisa']")
            campo_grupo.click()
            time.sleep(2)
            campo_grupo.send_keys(nome)
            print("prestes a pesquisar")
            time.sleep(2)
            pessoa = self.driver.find_element(By.CLASS_NAME, '_2EU3r')
            time.sleep(1)
            pessoa.click()
            time.sleep(1)
            print("prestes a enviar")
            chat_box = self.driver.find_element_by_xpath(
                "//div[@title='Mensagem']")
            time.sleep(1)
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(1)
            botao_enviar.click()
            time.sleep(1)
            valor + 1
        else:
            exit


bot = WhatsappBot()
bot.EnviarMensagens()
file.close()
