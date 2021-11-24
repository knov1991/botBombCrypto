from datetime import datetime
import cv2
import pyautogui
from time import sleep

def treasureHunt():
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    treasureHunt = cv2.imread('./images/treasureHunt.png', cv2.COLOR_BGR2GRAY)

    method = cv2.TM_CCOEFF_NORMED

    threshold = 0.95

    #Primeira comparação pra pegar coordenadas das contas
    res = cv2.matchTemplate(image, treasureHunt, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #Pegar coordenadas das contas
    if max_val > threshold:
        sleep(1)
        pyautogui.moveTo(max_loc)
        sleep(0.5)
        pyautogui.click(max_loc)
        sleep(2)