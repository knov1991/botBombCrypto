from datetime import datetime
import cv2
import pyautogui
from time import sleep

def menuPrincipal():
    #Sair de Treasure Hunt
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    voltarTela = cv2.imread('./images/voltarTela.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95
    res = cv2.matchTemplate(image, voltarTela, method)
    min_valVoltar, max_valVoltar, min_locVoltar, max_locVoltar = cv2.minMaxLoc(res)
    if max_valVoltar > threshold:
        sleep(1)
        pyautogui.moveTo(max_locVoltar)
        sleep(0.5)
        pyautogui.click(max_locVoltar)
        sleep(2)

    #Sair da tela Heroes/Characters
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    character = cv2.imread('./images/character.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95
    res = cv2.matchTemplate(image, character, method)
    min_valCharacter, max_valCharacter, min_locCharacter, max_locCharacter = cv2.minMaxLoc(res)
    if max_valCharacter > threshold:
        imgX = cv2.imread('./images/imgX.png', cv2.COLOR_BGR2GRAY)
        method = cv2.TM_CCOEFF_NORMED
        threshold = 0.95
        res = cv2.matchTemplate(image, imgX, method)
        min_valX, max_valX, min_locX, max_locX = cv2.minMaxLoc(res)
        if max_valX > threshold:
            sleep(1)
            pyautogui.moveTo(max_locX)
            sleep(0.5)
            pyautogui.click(max_locX)
            sleep(2)