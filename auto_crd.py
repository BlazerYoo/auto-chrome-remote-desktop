import pyautogui as pag

while True:
    if pag.locateOnScreen('./images/prompt.png', confidence=0.8) != None:
        x, y = pag.locateCenterOnScreen('./images/continue.png', confidence=0.8)
        pag.click(x=x, y=y)