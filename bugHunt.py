from datetime import datetime
import cv2
import pyautogui
from time import sleep

def bugHunt():
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    voltarTela = cv2.imread('./images/voltarTela.png', cv2.COLOR_BGR2GRAY)

    method = cv2.TM_CCOEFF_NORMED

    threshold = 0.95

    #Primeira comparação pra pegar coordenadas das contas
    res = cv2.matchTemplate(image, voltarTela, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #Pegar coordenadas das contas
    if max_val > threshold:
        return datetime.now()