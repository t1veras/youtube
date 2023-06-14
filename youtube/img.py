#Thiago Veras 05/04/2023

#requests==2.26.0
#selenium==3.141.0
#PyAutoGUI==0.9.53
#Pillow==9.0.1
#black==21.7b0
#pre-commit==2.15.0

#sudo apt --fix-broken install

#sudo apt install python3
#sudo apt install python3-pip
#pip3 install selenium
#pip3 install webdriver_manager
#pip3 install pyautogui

#sudo apt-get install python3-tk python3-dev

#sudo apt-get install python3-pil python3-pil.imagetk

import time
import pyautogui
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

height = pyautogui.size()[1]
width = pyautogui.size()[0]
print("resolution = " + str(width) + ", " + str(height))
window  = tk.Tk()
window.title("youtube")
window.resizable(0,0)
window.configure(background="white")
window.rowconfigure([0], minsize=round(width/96), weight=0)
window.columnconfigure([0,2], minsize=round(width/24), weight=0)
window.columnconfigure(1, minsize=round(width/2.13), weight=0)

def fetch(x):
    import requests as r
    res = r.get(f"https://img.youtube.com/vi/{x}/maxresdefault.jpg")
    with open("./images/image1.jpg", "wb") as f:
        f.write(res.content)

def filter():
    x = url_input.get().strip().split("=")[1].strip().split("&")[0]
    if x == "":
        print("can't find image")
        return
    else:
        try:
            fetch(x)
            global img0
            img0 = Image.open("./images/image1.jpg")
            img0 = img0.resize((round(img0.size[0]*0.7*width/1920), round(img0.size[1]*0.7*width/1920)))
            print("thumbnail size -> " + str(img0.size[0]) + ", " + str(img0.size[1]))
            img0 = ImageTk.PhotoImage(img0)
            thumbnail_frm.configure(image=img0)
        except:
            print("permission error: writing to a file")
            return

def duration_split(duration):
    hour = 0
    min = 0
    sec = 0
    list = duration.split(":")
    hour = int(list[0])
    min = int(list[1])
    sec = int(list[2])
    return hour*3600 + min*60 + sec

def start():
    dur = dur_entry.get()
    loop = loop_entry.get()

    if len(dur.split(":")) == 3:
        dur = duration_split(dur)
    else:
        return
    if loop == "":
        return
    else:
        if loop.lower() == "inf":
            loop = 999999999
        else:
            try:
                loop = int(loop)
            except:
                return

    while loop:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url_input.get().strip())
        plybtn = driver.find_element(by=By.CLASS_NAME, value="ytp-play-button")
        time.sleep(3)
        #if video doesnt start disable this
        plybtn.click()                      
        time.sleep(dur)
        driver.close()
        loop -= 1

#images
img0 = Image.open("./images/image.jpg")
img0 = img0.resize((round(img0.size[0]*0.7*width/1920), round(img0.size[1]*0.7*width/1920)))
print("img0 size -> " + str(img0.size[0]) + ", " + str(img0.size[1]))
img0 = ImageTk.PhotoImage(img0)

#description
desc = tk.Label(master=window, text = "bot", font=("aNYTHING", 25), bg="white")
desc.grid(row=1, column=0, pady=(5,30), columnspan=3)

#url input
url_label = tk.Label(master=window, text="url", font=("", 15), bg="white")
url_label.grid(row=2, column=0, padx=(15, 5), pady=(0, 5))
url_input = ttk.Entry(master=window, font=("", 15))
url_input.grid(row=2, column=1, sticky="ew", pady=(0, 5))

#submit button
style = ttk.Style()
style.configure("TButton", font=("", 15))
url_btn = ttk.Button(style='TButton', master=window, text="submit", command = filter)
url_btn.grid(row=2, column=2, padx=(3, 15), pady=(0, 5))

#thumbnail frame
thumbnail_frm = tk.Label(master=window, image=img0, bg="red")
thumbnail_frm.grid(row=3, column=0, columnspan=3)

#bottom frame
dur_loop_frm = tk.Frame(master=window, bg="white")
dur_loop_frm.grid(row=4, column=0, columnspan=3, sticky="nsew")

#duration
dur_lbl = tk.Label(master=dur_loop_frm, text="time (00:00:00) ", font=("", 15), bg="white")
dur_lbl.pack(side="left", pady=10, padx=(15,3))
dur_entry = ttk.Entry(master=dur_loop_frm, font=("", 15))
dur_entry.pack(side="left")

#loop
loop_lbl = tk.Label(master=dur_loop_frm, text="loops (inf for infinity) ", font=("", 15), bg="white")
loop_lbl.pack(side="left", pady=10, padx=(15,3))
loop_entry = ttk.Entry(master=dur_loop_frm, font=("", 15))
loop_entry.pack(side="left")

#start button
dur_loop_btn = ttk.Button(style = "TButton", master=dur_loop_frm, text="start", command=start)
dur_loop_btn.pack(side="right", padx=15)

window.mainloop()