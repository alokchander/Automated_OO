import csv


#def database_cood

def nameEntry():
    with open("plain_order_fill.csv","r",newline = '') as namefile:
        lines = []
        for row in namefile:
            lines.append(row)
        name = lines[0]
    return name
            

#def menu_find
#def menu_select
#def tab_select

def saveOrder(name)
#saves order after dishes have been entered and enters name and sends to chef



def enterItem(instr, quantity):
    for i in range(0, quantity):
        for line in instr:
            click(line[0], line[1])

def click(x,y)
        
    

#include info in dbase about which tab the dish is in as well as coord of tab
#def submit_order

def info_extractor(item_info):
    return item_info[2], item_info[3], item_info[4], item_info[5]
    

line  = 0

name = nameEntry()
with open("plain_order_fill.csv","r",newline = '') as file:
    reader = csv.reader(file)
    for row in reader:
        if (line > 0):
            #Extract order info from the line
            #option for NA spice
            spice_x,spice_y, quantity, x_cor ,y_cor,tab_x,tab_y = info_extractor(row)
    
            instr = []
            instr.append((tab_x,tab_y))
            instr.append((x_cor,y_cor))
            instr.append((spice_x, spice_y))
            enterItem(instr,quantity)
saveOrder()

        
    
  