import pyautogui as pag
import time
input = 1

while(input!="Close"):
    x,y=pag.position()
    pag.PAUSE = 1
    print("X",x)
    print("Y",y)
    time.sleep(1)
    