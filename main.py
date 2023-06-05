from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#Inicia uma nova conexão
DRIVER_PATH = '/path/to/chromedriver'
options = Options()
#options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)

driver.get('https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fmynetwork%2Finvite-connect%2Fconnections%2F&fromSignIn=true&trk=cold_join_sign_in')
driver.maximize_window()

time.sleep(5)

email = ''
senha = ''

#Encontra e inseri o email para login
while True:
    try:
        campoEmail = driver.find_element(By.XPATH, '//input[@id="username"]')
    except:
        time.sleep(2)
    else:
        for letra in email:
            campoEmail.send_keys(letra)
        time.sleep(2)
        break

while True:
    try:
        campoSenha = driver.find_element(By.XPATH, '//input[@id="password"]')
    except:
        time.sleep(2)
    else:
        for letra in senha:
            campoSenha.send_keys(letra)
        time.sleep(2)
        break
    
#Encontra e clica no botão para aceitar o email
while True:
    try:
        driver.find_element(By.XPATH, '//button[@class="btn__primary--large from__button--floating"]').click()
    except:
        time.sleep(2)
    else:
        time.sleep(2)
        break

time.sleep(5)
antiBot = True
while antiBot:
    time.sleep(1)
    try:
        
        driver.find_elements(By.XPATH, '//button[@class="artdeco-button artdeco-button--2 artdeco-button--secondary ember-view"]')
            
    except:
        print("")
    else:
        antiBot=False
        time.sleep(5)

time.sleep(5)

#laço de repetição para gerar todos os links do site
x = 0
while x <= 10:
    try:
        driver.find_element(By.XPATH,'//button[@class="artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button"]').click()
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    else:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    x+=1

botoes = driver.find_elements(By.XPATH, '//button[@class="artdeco-button artdeco-button--2 artdeco-button--secondary ember-view"]')

texto =   ', na STS, somos a ponte que conecta simplicidade e inovação para você. Nossa missão é construir um mundo onde os sonhos se tornem realidade e a complexidade ceda lugar à simplicidade. Na Silva Tech Souza, somos especialistas em criar aplicativos e sites personalizados para atender às suas necessidades. Oferecemos soluções tecnológicas inovadoras que ajudam você a alcançar seus objetivos. Estamos empenhados em mudar o mundo ao nosso redor, ao lado daqueles que sonham grande e nunca desistem.' 

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

for botao in botoes:
        
    controle = True
    while controle:
        try:
            botao.click()
        except:
            print("n")
        else:
            controle  = False
            break
            
    time.sleep(5)
    
    try:
        driver.find_element(By.XPATH,'//a[@class="app-aware-link  profile-card-one-to-one__profile-link"]')
    except:
        botoesControle = driver.find_element(By.XPATH,'//div[@class="msg-overlay-bubble-header__controls display-flex align-items-center"]').find_elements(By.TAG_NAME, 'button')
        botoesControle[3].click()
    else:
        try:
            nome = driver.find_element(By.XPATH,'//a[@class="app-aware-link  profile-card-one-to-one__profile-link"]').text
        except:
            nome = ''
            
        try:    
            textoFinal = 'Olá, ' + str(nome) + texto
            textarea = driver.find_element(By.XPATH, '//div[@role="textbox"]')
            textarea.send_keys(textoFinal)
        except:
            textoFinal = 'Olá, ' + texto
            textarea = driver.find_element(By.XPATH, '//div[@role="textbox"]')
            textarea.send_keys(textoFinal)
        
        time.sleep(2)
    
    while True:
        try:
            driver.find_element(By.XPATH,'//div[@class="msg-form__right-actions display-flex align-items-center"]/div/button[@class="msg-form__send-button artdeco-button artdeco-button--1"]').click()
        except:
            time.sleep(1)
            print("")
            break
        else:
            time.sleep(5)
            
            botoesControle = driver.find_element(By.XPATH,'//div[@class="msg-overlay-bubble-header__controls display-flex align-items-center"]').find_elements(By.TAG_NAME, 'button')
            botoesControle[3].click()
        
