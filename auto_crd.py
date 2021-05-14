import pyautogui as pag

while True:
    if pag.locateOnScreen('./images/crd_prompt.png') != None:
        x, y = prompt_center = pag.locateCenterOnScreen('./images/crd_continue.png', confidence=0.8)
        pag.click(x=x, y=y)