#Thiago Veras 05/04/2023

#sudo apt --fix-broken install

#sudo apt install python3
#sudo apt install python3-pip
#pip3 install pyautogui
#sudo apt-get install python3-tk python3-dev

import pyautogui as pg
import webbrowser as wb
import time

wb.open("https://web.whatsapp.com")
time.sleep(30)

for i in range(10):
    pg.typewrite("test")
    pg.press("enter")