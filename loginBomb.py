import cv2
import pyautogui
from time import sleep

def loginBomb():
    #Verifica se ainda esta na tela de login // Bug!
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    bombCrypto = cv2.imread('./images/bombCrypto.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95
    res = cv2.matchTemplate(image, bombCrypto, method)
    min_valBombCrypto, max_valBombCrypto, min_locBombCrypto, max_locBombCrypto = cv2.minMaxLoc(res)
    if max_valBombCrypto > threshold:
        pyautogui.moveTo(max_locBombCrypto)
        sleep(0.5)
        pyautogui.click(max_locBombCrypto)
        sleep(0.5)
        pyautogui.press('f5')
        sleep(10)

    #Connect Wallet - Login
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    connectWallet = cv2.imread('./images/connectWallet.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95
    res = cv2.matchTemplate(image, connectWallet, method)
    min_valConnect, max_valConnect, min_locConnect, max_locConnect = cv2.minMaxLoc(res)
    if max_valConnect > threshold:
        pyautogui.moveTo(max_locConnect)
        sleep(0.5)
        pyautogui.click(max_locConnect)
        sleep(5)

    #Selecionar Wallet Metamask - Login
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    metamask = cv2.imread('./images/metamask.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95
    res = cv2.matchTemplate(image, metamask, method)
    min_valMetamask, max_valMetamask, min_locMetamask, max_locMetamask = cv2.minMaxLoc(res)
    if max_valMetamask > threshold:
        pyautogui.moveTo(max_locMetamask)
        sleep(0.5)
        pyautogui.click(max_locMetamask)
        sleep(5)


    #Assinar Metamask - Login
    pyautogui.screenshot('./images/image.png')
    image = cv2.imread('./images/image.png', cv2.COLOR_BGR2GRAY)
    assinar = cv2.imread('./images/assinar.png', cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95
    res = cv2.matchTemplate(image, assinar, method)
    min_valAssinar, max_valAssinar, min_locAssinar, max_locAssinar = cv2.minMaxLoc(res)
    if max_valAssinar > threshold:
        pyautogui.moveTo(max_locAssinar)
        sleep(0.5)
        pyautogui.click(max_locAssinar)
        sleep(20)