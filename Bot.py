from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://gshow.globo.com/realities/bbb/bbb21/votacao/paredao-bbb21-vote-para-eliminar-arthur-gilberto-ou-karol-conka-838ec4d5-7d17-4263-a335-29e13c3a769b.ghtml')
time.sleep(3)

def buscar_contato():
    campo_pesquisa = driver.find_elements_by_xpath("//div[@class='_2f489c1b8b0287b3c03']")
    print('encontrou ID')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem():
    print('entrou')
    #campo_mensagem = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    #campo_mensagem[1].click()
    #time.sleep(3)
    #campo_mensagem[1].send_keys(Keys.ENTER)

buscar_contato()
enviar_mensagem()