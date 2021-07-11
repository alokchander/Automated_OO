import pyautogui as pag
pag.FAILSAFE = False
pag.moveTo(1366,768)

pag.moveTo(900,768)
pag.moveTo(153,751)
pag.click()
pag.PAUSE=2
pag.moveTo(562,68)
pag.click()
pag.write("www.youtube.co.nz")
pag.PAUSE = 1
pag.press('enter')
pag.moveTo(434,125)
pag.click()
pag.write("renai circulation")
pag.press('enter')
pag.moveTo(440,307)
pag.PAUSE = 2
pag.click()
pag.PAUSE=5
lol= pag.locateCenterOnScreen('skp.png', confidence = .90)
if(lol!=NONE):
    pag.moveTo(lol[0],lol[1])
    pag.click()
    
  
  
  
