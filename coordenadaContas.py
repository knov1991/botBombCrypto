import cv2
import pyautogui
from time import sleep
import os

def procuraCoordenadasChrome(max_contas):
    contas = 0
    local_chrome = []

    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    chrome = cv2.imread('./images/chrome.png', cv2.COLOR_BGR2GRAY)

    h, w = chrome.shape[:2]

    method = cv2.TM_CCOEFF_NORMED

    threshold = 0.98

    #Primeira comparação pra pegar coordenadas das contas
    res = cv2.matchTemplate(image, chrome, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #Pegar coordenadas das contas
    while max_val > threshold and contas < max_contas:
        res = cv2.matchTemplate(image, chrome, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        #Coloca um marcador na imagem pra não repetir o mesmo resultado encontrado
        image[max_loc[1]:max_loc[1]+h+1:, max_loc[0]:max_loc[0]+w+1, 0] = 0     # blue channel
        image[max_loc[1]:max_loc[1]+h+1:, max_loc[0]:max_loc[0]+w+1, 1] = 0     # green channel
        image[max_loc[1]:max_loc[1]+h+1:, max_loc[0]:max_loc[0]+w+1, 2] = 255   # red channel

        #pyautogui.moveTo(max_loc)
        #print('local: ',max_loc,'acertivo: ',max_val)
        local_chrome.append(max_loc)
        #print('conta'+str(contas+1)+':',local_chrome[contas])
        contas +=1
        sleep(0.1)

    #print(local_chrome)
    #cv2.imwrite('output.png', image)

    #os.remove('images/image.png')
    return local_chrome

#print(procuraCoordenadasChrome(2))