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

with open("plain_order.csv","r+") as txtfile:
            
            with open("dbase.csv","r") as dbase:
                        
                        with open("plain_order_fill.csv","w",newline = '') as file:
                                    fieldnames = ['Id','Dish','Spice','Quantity','X','Y']
                                    writer = csv.DictWriter(file, fieldnames = fieldnames)  
                                    writer.writeheader()

                                    length = 0
                                   
                                    reader = csv.DictReader(txtfile)
                                    
                                    dbase_reader = csv.DictReader(dbase)
                                    dbase_x = {b["Dish"] : b["X"] for b in dbase_reader}
                                    dbase.seek(0)
                                    # seek to set cursor back to 0 to enabable reading of y cood
                                    #otherwise will read empty lines
                                    dbase_y = {b["Dish"] : b["Y"] for b in dbase_reader}
                                    
                                    for row in reader:
                                               # print(row["Dish"])
                                                print(dbase_y.get(row["Dish"]))
                                                if dbase_x.get(row["Dish"]):
                                                            
                                                            row["X"] = dbase_x.get(row["Dish"])
                                                            row["Y"] = dbase_y.get(row["Dish"])
                                                writer.writerow(row)
                             

                         

                        

                                                            
                                                            
                                                            
                                                            
                        
                                    
                        
                                               

                                    
        
            
                        
            
