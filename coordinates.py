import csv
def coordinates(dish):
            x = 0
            y = 0
            with open("dbase.csv","r") as txtfile:
                        reader = csv.reader(txtfile)
                        print("yoyo")
                        for row in reader:
                                    if dish ==  ((row[0]).split(','))[0]:
                                                x = ((row[0]).split(','))[1]
                                                y =  ((row[0]).split(','))[2]
            return(x,y)
                        
                      
x,y = coordinates("Butter chicken")
print(x)
print(y)