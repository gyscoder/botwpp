from selenium import webdriver #importa o selenium
import time

class facebook_bot(): #cria uma classe com operações iniciais
    def __init__(self, driver, url, username, password):
        self.driver = webdriver.Firefox() #define qual webdriver vai ser usado
        self.driver.get(url)  #define a url que o webdriver vai abrir
        self.login(username, password) #define dados do login
        #self.spam() # atira a função de entrar no perfil
        #self.argv[1] #procura meu perfil

    def login(self, username, password): #cria uma função de login aonde ele procura pelos campos de: email, senha e o botão enviar
        email_box = self.driver.find_element_by_name('email') #procura pelos dados do id email
        email_box.send_keys(username) #entra na form de email

        pass_box = self.driver.find_element_by_name('pass') #procura pelos dados do id pass
        pass_box.send_keys(password) #entra na form da senha

        login_button = self.driver.find_element_by_name('login')
        login_button.click() #clica no botão de login

        time.sleep(4)
        btn_ok = self.driver.find_element_by_class_name('bk') # procura pelo botão OK
        btn_ok.click() # clica no botão Ok

    def perfil(self): # cria uma função pra entrar no próprio perfil
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/div/form/table/tbody/tr/td[1]/div/a').click() # clica no link do perfil

    def spam(self, texto):

        time.sleep(5)
        #self.driver.find_element_by_link_text('ᚵᛂᚤᛊᚭᛘ ᛋᚭᛆᚱᛂᛊ').click() # clica em algum texto
        #self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div[2]/div/section/article[5]/footer/div[2]/a[1]').click() #clica nos comments do post // numero do article interfere em qual post ir
        while True:
            time.sleep(0.02)
            self.driver.find_element_by_xpath('//*[@id="composerInput"]').send_keys(texto) #clica na form do comentário
            self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[6]/form[1]/table/tbody/tr/td[2]/div').click() #clica em enviar 
        pass