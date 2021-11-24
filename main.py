import pyautogui
import conexaoDB
from coordenadaContas import procuraCoordenadasChrome as getContas
from time import sleep
from newMap import newMap
from error import error
from loginBomb import loginBomb
from dormindo import dormindo
from datetime import datetime
from trabalhar import trabalhar
from treasureHunt import treasureHunt
from telaHeroes import telaHeroes
from menuPrincipal import menuPrincipal
from bugHunt import bugHunt
from hwid import hwid

""" while True:
    newMap()
    sleep(3) """

#Login no banco de dados
acesso = conexaoDB.verificaLogin('teste@teste.com','123123') # Conecta com banco de dados e retorna o máximo de contas
idUsuario = acesso[0]
maxContas = acesso[1]
hwidDB = acesso[2]

#Verifica quantidade de Contas permitidas
if(maxContas > 0):
    pass

#Registra novo Computador
if(hwid() == hwidDB):
    pass
elif(hwidDB == None):
    conexaoDB.novoPC(hwid(), idUsuario)
    print('Configurando primeiro acesso...')
    sleep(10)
    print('Configuração')
    exit()
else:
    print('Acesso Negado!')
    exit()

print('Acesso Autorizado!')
sleep(2)
print('Nº de contas:',maxContas)

coord = getContas(maxContas)
print(coord)

#Variaveis para funcionamento do BOT
tempoDescanso = 50
horaDormindo = []
tempoBug = 5
horaBugHunt = []
i=0

while i < maxContas:
    horaDormindo.append(0)
    sleep(0.5)
    horaBugHunt.append(0)
    i+=1


while True:
    try:
        loopContas=0
        while loopContas < maxContas:
            #print('Conta:',loopContas+1)
            #Se tiver acesso a + de 1 conta, muda de conta // se tiver acesso a 1 não faz nada
            if(maxContas > 1):
                pyautogui.moveTo(coord[loopContas])
                sleep(0.5)
                pyautogui.click(coord[loopContas])

            #Login BombCrypto
            loginBomb()

            #Clicar em treasureHunt para iniciar o farm
            treasureHunt()

            #verifica erro e clica pra retirar
            error()

            #passa de mapa quando finalizar
            newMap()

            #verifica se algum boneco esta dormindo, se estiver registra hora
            verificaDormir = dormindo()
            if(type(verificaDormir) == datetime and type(horaDormindo[loopContas]) == int):
                horaDormindo[loopContas] = verificaDormir
            #Verifica se o tempo descansando é maior que o permitido para decanso, se for vai pra onde coloca os bonecos pra trabalhar
            if(type(horaDormindo[loopContas]) == datetime):
                horaAtual = datetime.now()
                calculaTempo = horaAtual - horaDormindo[loopContas]
                minutos = calculaTempo.total_seconds()/60
                if(minutos > tempoDescanso):
                    print(datetime.now(),' - Indo trabalhar // Conta',loopContas+1)
                    menuPrincipal()
                    telaHeroes()

            #Coloca os Heroes para trabalhar e se ocorrer tudo remove a horaDormindo que os bonecos começaram a dormir     
            trabalhando = trabalhar()
            if trabalhando == True:
                print(datetime.now(),' - Trabalhando // Conta',loopContas+1)
                horaDormindo[loopContas] = 0
                menuPrincipal()
                treasureHunt()

            #Verifica quanto tempo esta na tela de Hunt
            verificaBugHunt = bugHunt()
            if(type(verificaBugHunt) == datetime and type(horaBugHunt[loopContas]) == int):
                horaBugHunt[loopContas] = verificaBugHunt
            #Se o tempo for maior que o tempoBug - retorna para menuPrincipal para evitar bug
            if(type(horaBugHunt[loopContas]) == datetime):
                horaAtual = datetime.now()
                calculaTempo = horaAtual - horaBugHunt[loopContas]
                minutos = calculaTempo.total_seconds()/60
                if(minutos > tempoBug):
                    print(datetime.now(),' - Desbugando Hunt // Conta',loopContas+1)
                    menuPrincipal()
                    treasureHunt()
                    horaBugHunt[loopContas] = 0

            #Fim das ações do BOT // prepara para a proxima conta
            loopContas+=1
            #print('Fim - Preparando próxima conta...')
            sleep(5)
    except:
        pass