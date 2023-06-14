#Thiago Veras 05/04/2023

#sudo apt --fix-broken install

#sudo apt install python3
#sudo apt install python3-pip
#pip3 install pyautogui

#sudo apt-get install python3-tk python3-dev

#sudo apt-get install xsel
#sudo apt-get install xclip

import pyautogui
import time
import pyperclip

groups = ['/680031346129512']
#groups = ['/680031346129512','/680031346129512']

time.sleep(5)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://facebook.com/groups'+groups[i]
    pyperclip.copy(link)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite('\n')

    print("wait 5 seconds\n")
    time.sleep(5)

    pyautogui.typewrite('p')
    time.sleep(2)
    print("write post\n")
    pyautogui.typewrite("test")
    time.sleep(4)

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
 
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    time.sleep(3)

    pyautogui.write(['f6'])
    time.sleep(1)