import cv2
import pyautogui
from time import sleep

def telaHeroes():
    #Ir para tela de trabalho dos HEROES
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    heroes = cv2.imread('./images/heroes.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95
    res = cv2.matchTemplate(image, heroes, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #Pegar coordenadas das contas
    if max_val > threshold:
        pyautogui.moveTo(max_loc)
        sleep(0.5)
        pyautogui.click(max_loc)
        sleep(20)

