import cv2
import pyautogui
from time import sleep
from error import error

def trabalhar():
    #Clica na barra do boneco
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    barraHeroes = cv2.imread('./images/barraHeroes.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.98
    res = cv2.matchTemplate(image, barraHeroes, method)
    min_valBarraHeroes, max_valBarraHeroes, min_locBarraHeroes, max_locBarraHeroes = cv2.minMaxLoc(res)
    if max_valBarraHeroes > threshold:
        pyautogui.moveTo(max_locBarraHeroes)
        sleep(0.5)
        pyautogui.click(max_locBarraHeroes)
        sleep(1)
        #Rolar a lista de Heroes ate o final
        i=0
        while i < 100:
            pyautogui.scroll(-50)
            i+=1

    #Colocando Heroes pra trabalhar
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png')
    work = cv2.imread('./images/work.png')
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.98
    res = cv2.matchTemplate(image, work, method)
    min_valWork, max_valWork, min_locWork, max_locWork = cv2.minMaxLoc(res)
    while max_valWork > threshold:
        pyautogui.moveTo(max_locWork)
        sleep(0.3)
        pyautogui.click(max_locWork)
        sleep(5)
        error()
        pyautogui.screenshot('./images/image.png')
        image = cv2.imread('./images/image.png')
        work = cv2.imread('./images/work.png')
        method = cv2.TM_CCOEFF_NORMED
        threshold = 0.98
        res = cv2.matchTemplate(image, work, method)
        min_valWork, max_valWork, min_locWork, max_locWork = cv2.minMaxLoc(res)

    #Verifica se esta na tela de Heroes
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    character = cv2.imread('./images/character.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.98
    res = cv2.matchTemplate(image, character, method)
    min_valCharacter, max_valCharacter, min_locCharacter, max_locCharacter = cv2.minMaxLoc(res)
    if max_valCharacter > threshold:
        #Verifica se todos os Heroes estão trabalhando
        pyautogui.screenshot('./images/image.png')
        image = cv2.imread('./images/image.png')
        work = cv2.imread('./images/work.png')
        threshold = 0.98
        res = cv2.matchTemplate(image, work, method)
        min_valWork, max_valWork, min_locWork, max_locWork = cv2.minMaxLoc(res)
        if max_valWork < threshold:
            return True
        else:
            return False
    else:
        return False
        

