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

                        length = 0
                       
                        reader = csv.DictReader(txtfile)
                        
                        dbase_reader = csv.DictReader(dbase)
                        dbase_x = {b["Dish"] : b["X"] for b in dbase_reader}
                        dbase_y = {b["Dish"] : b["Y"] for b in dbase_reader}
                        
                        for row in reader:
                                    print(row["Dish"])
                                    print(dbase_x.get(row["Dish"]))
                                    if dbase_x.get(row["Dish"]):
                                                
                                                row["X"] = dbase_x.get(row["Dish"])
                        with open("plain_order.csv","w") as file:
                                    
                                                            
                                    fieldnames = ['Id','Dish','Spice','Quantity','X','Y']
                                    writer = csv.DictWriter(file, fieldnames = fieldnames)
                                    for row in reader:
                                                
                                                
                                                writer.writerow(row)            

                                                
                                    

                         

                        
                                    
                     
                       # for row in reader:
                                    
                       #             dish = dbase_reader.get(row["Dish"])
                        
                        #            if dish:
                         #                       print(dish)
                                    
                                  #  for items in dbase_reader:
                                                
                                                
                                                
                                                
                                   #             print(row["Dish"])
                                    #            #print(items["Dish"])
                                     #           if row["Dish"] == items["Dish"]:
                                      #                      row["X"] = items["X"]
                                       #                     row["Y"] = items["Y"]
                                        #                    reader.writerow(row) 
                                             
                                   
                                                

                                     
                                                            
                                                            
                                                            
                                                            
                        
                                    
                        
                                               

                                    
        
            
                        
            
