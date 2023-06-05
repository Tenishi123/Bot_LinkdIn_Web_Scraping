from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

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
            #time.sleep(1)
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
            #time.sleep(1)
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
        main = driver.find_element(By.XPATH, '//div[@class="scaffold-finite-scroll__content"]')     
    except:
        print("")
    else:
        antiBot=False

#laço de repetição para gerar todos os links do site
x = 0
while x <= 3:
    try:
        driver.find_element(By.XPATH,'//button[@class="artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button"]').click()
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    else:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    x+=1

tags = main.find_elements(By.TAG_NAME, 'a')

links = []
for tag in tags:
    links.append(tag.get_attribute('href'))

links_tratados = []
for link in links:
    controle = True
    for link2 in links_tratados:
        if (link2 == link):
            controle = False
    
    if controle:
        links_tratados.append(link)
        
#setando variaveis que serão usadas no laço de repetição
num = 2
wb = Workbook()
ws1 = wb.worksheets[0]

# nome da empresa da última experiência e a URL da mesma

ws1['A1'] = "Nomes"
ws1['B1'] = "Perfil"
ws1['C1'] = "Telefone"
ws1['D1'] = "E-mail" 
ws1['E1'] = "Nome da ultima experiencia"
ws1['F1'] = "URL da ultima experiencia"
   
#executa um laço de repetição que ira passar por todos os links de login encontrados
for link in links_tratados:
    
    # Abre uma nova aba e vai para o site do SO
    driver.execute_script("window.open('" + link + "', '_blank')")
    
    #espera o novo carregamento da pagina
    time.sleep(5)
    
    driver.switch_to.window(driver.window_handles[1])
    
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
    
    try:
        nome = driver.find_element(By.XPATH, '//h1[@class="text-heading-xlarge inline t-24 v-align-middle break-words"]').text
    except:
        nome = ''
    
    try:
        textWebCards = driver.find_elements(By.XPATH, '//section[@tabindex="-1"]')
    except:
        textWebCards = None
    experienia = ''
    urlExperiencia = ''
    
    for textWebCard in textWebCards:
        textBruto = textWebCard.text.split('\n')
        if(textBruto[0] == 'Experiência'):
            experienia = textBruto[5]
            
            try:
                urlExperiencia = textWebCard.find_element(By.TAG_NAME, 'a').get_attribute('href')
            except:
                urlExperiencia = ''
  
    try:
        driver.find_element(By.ID, 'top-card-text-details-contact-info').click()
        
        time.sleep(3)
        
        infoBruta = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/section/div').text
    except:
        infoBruta = ''
        
    telefone = ''
    email = ''
    infoArray = infoBruta.split("\n")
    numLocal = 0
    numArray = 0
    
    for nd in infoArray:
        numArray+=1
        
    while numLocal < numArray:
        
        if(infoArray[numLocal].upper() == 'telefone'.upper()):
            telefone = infoArray[numLocal+1]
        elif(infoArray[numLocal].upper() == 'E-mail'.upper()):
            email = infoArray[numLocal+1]
            
        numLocal +=1

    #setando as informações na planilha
    ws1['A'+str(num)] = nome

    #setando as informações na planilha
    ws1['B'+str(num)] = link 
        
    #setando as informações na planilha
    ws1['C'+str(num)] = telefone

    #setando as informações na planilha
    ws1['D'+str(num)] = email
    
    #setando as informações na planilha
    ws1['E'+str(num)] = experienia
    
    #setando as informações na planilha
    ws1['F'+str(num)] = urlExperiencia
    
    #salvando a planilha gerada
    wb.save(filename = './DadosLinkedin.xlsx')

    num+= 1
      
    driver.close() 
    driver.switch_to.window(driver.window_handles[0]) 