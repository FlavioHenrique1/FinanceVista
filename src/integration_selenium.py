from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChromeBrowser:
    def __init__(self, profile_path, profile_directory="Profile 3"):
        """
        Inicializa o navegador Chrome com o perfil especificado.

        :param profile_path: Caminho para a pasta do perfil do Chrome.
        :param profile_directory: Diretório do perfil dentro do perfil principal.
        """
        self.profile_path = profile_path
        self.profile_directory = profile_directory
        self.driver = None

    def start_browser(self):
        """Configura e inicializa o driver do Chrome."""
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir={self.profile_path}")
        chrome_options.add_argument(f"--profile-directory={self.profile_directory}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def navigate_to(self, url,produtos):
        """
        Navega até a URL especificada.

        :param url: URL a ser acessada.
        """

        if self.driver is None:
            raise Exception("O navegador não foi iniciado. Use o método start_browser primeiro.")
        
        self.driver.get(url)
        btn_enter = self.driver.find_element(By.CLASS_NAME, "ZS4fKc").click()
        time.sleep(3)
            # inicio do loop
        for produto in produtos:
            btn_add = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "WRe7Yb"))
            )
            btn_add.click()

            input_ativo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Insira o nome ou símbolo de um investimento']"))
            )
                    # Clique no campo
            input_ativo.click()
            
            # Enviar o texto
            input_ativo.send_keys(produto['produto'],Keys.RETURN)
            # Enviar o tenter
            input_ativo.send_keys(Keys.ENTER)
            time.sleep(1)

            input_quantidade = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ylDj9e"))
            )

            # Digita "quantidade" no campo de entrada
            input_quantidade.send_keys(produto['quantidade'])
            time.sleep(2)

            input_data = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd"))
            )

            # Digita "quantidade" no campo de entrada
            input_data.send_keys(produto['data'])
            time.sleep(2) 

            input_valor = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "Is59ac"))
            )

            # Digita "quantidade" no campo de entrada
            input_valor.clear()
            input_valor.send_keys(produto['Valor da Operação'])
            time.sleep(2)

            btnSalve = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ilG6Gf"))
            )
            btnSalve.click()


    def stop_browser(self):
        """Fecha o navegador."""
        if self.driver:
            self.driver.quit()

# Exemplo de uso
# if __name__ == "__main__":
#     profile_path = r"C:\\Users\\fla-h\\AppData\\Local\\Google\\Chrome\\User Data"
#     browser = ChromeBrowser(profile_path)

#     try:
#         browser.start_browser()
#         browser.navigate_to("https://www.google.com/finance/")
#         time.sleep(10)  # Aguarda o carregamento da página
#     finally:
#         browser.stop_browser()

