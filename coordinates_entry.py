
import csv

with open("plain_order.csv","r+") as txtfile:

            length = 0
            reader = csv.DictReader(txtfile)
         
            for row in reader:
            
                                    print(row)

                                    
        
            
                        
            
