import cv2
import pyautogui
from time import sleep

def error():
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    error = cv2.imread('./images/error.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95

    #Procura imagem de erro na tela
    res = cv2.matchTemplate(image, error, method)
    min_valError, max_valError, min_locError, max_locError = cv2.minMaxLoc(res)

    if max_valError > threshold:
        pyautogui.screenshot('./images/image.png')
        image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
        imgX = cv2.imread('./images/imgX.png', cv2.COLOR_BGR2GRAY)
        method = cv2.TM_CCOEFF_NORMED
        threshold = 0.95

        #Procura imagem do X para fechar janela
        res = cv2.matchTemplate(image, imgX, method)
        min_valX, max_valX, min_locX, max_locX = cv2.minMaxLoc(res)
        
        if max_valX > threshold:
            pyautogui.moveTo(max_locX)
            sleep(0.5)
            pyautogui.click(max_locX)
        else:
            pyautogui.moveTo(max_locError)
            sleep(0.5)
            pyautogui.click(max_locError)

        #Apos clicar pra fechar o erro esperar a informação carregar na tela
        sleep(5)