import pyautogui as pag
pag.moveTo(900,200)
lol= pag.locateCenterOnScreen('close.png', confidence = .90)
print("x = ",lol[0])
print("y = ",lol[1])
pag.PAUSE=2
pag.click(700,300)
pag.scroll(-1,700,300)