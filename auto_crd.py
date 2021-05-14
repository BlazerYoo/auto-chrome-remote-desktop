import pyautogui as pag

while True:
    # ensure both prompt and continue button are present
    prompt = pag.locateOnScreen('./images/prompt.png', confidence=0.8)
    continue_button = pag.locateCenterOnScreen('./images/continue.png', confidence=0.8)
    if prompt != None and continue_button != None:
            pag.click(x=continue_button[0], y=continue_button[1])