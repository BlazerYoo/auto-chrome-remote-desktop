import pyautogui as pag
import time


def main():
    print('started auto crd')
    while True:
        # ensure both prompt and continue button are present
        prompt = pag.locateOnScreen('./images/prompt.png', confidence=0.8)
        continue_button = pag.locateCenterOnScreen('./images/continue.png', confidence=0.8)
        if prompt != None and continue_button != None:
                time.sleep(3)
                print(f'crd prompt found - {time.strftime("%c")}')
                pag.click(x=continue_button[0], y=continue_button[1])
                print(f'continue clicked - {time.strftime("%c")}')


if __name__ == '__main__':
      main()