import bs4
import csv
import re
File = open("em.html")
filehtml = bs4.BeautifulSoup(File,'html.parser')
count = 0
# newline to avoid extra space between rows
with open("order.csv","w", newline = '') as txtfile:
    with open("plain_order.csv","w", newline = '') as plain_order_file:
        
        
        writer = csv.writer(txtfile)
        writer_plain = csv.writer(plain_order_file)
        
        print(type(filehtml))
        #print(filehtml.prettify())
        name = filehtml.select('h1[ style="margin:0;text-align:left;font-size:41px;line-height:40px;font-family:Georgia,serif;font-style:normal;font-weight:400;color:#ffffff"]')
        Name = name[0].getText() 
        Name = Name[16:-1]
        namelen = len(Name);
        writer.writerow(["1",Name])
        shipping = filehtml.select('tr > td[ style="color:#b65162;border:1px solid #e5e5e5;font-family:Georgia,serif;border-color:#e4e4e4;border-width:1px;border-style:solid;padding:12px;padding-left:px;padding-right:px;text-align:left"]')[-3]
        writer.writerow(["2",shipping])
        
        address = filehtml.select('address > table >tbody>tr>td')
     
        address_list = str(address[0]).split("<br/>")
        #prints name by splitting address_list 0th element based on \t and the extract last element
        street = address_list[1] +" "+ address_list[2]
        mobile_num = address_list[3].strip("</td>")
       
      
        name = ((address_list[0]).split('\t'))[-1] 
        writer.writerow(['3',street])
        writer.writerow(['4',mobile_num])
        
        
        
        
        bu = filehtml.select('td[style="color:#b65162;border:1px solid #e5e5e5;font-family:Georgia,serif;border-color:#e4e4e4;border-width:1px;border-style:solid;padding:12px;padding-left:px;padding-right:px;text-align:left;vertical-align:middle;word-wrap:break-word"]')
        
    
        pu = filehtml.select('tr td[style="color:#b65162;border:1px solid #e5e5e5;font-family:Georgia,serif;border-color:#e4e4e4;border-width:1px;border-style:solid;padding:12px;padding-left:px;padding-right:px;text-align:left;vertical-align:middle"]:nth-child(2)')
        
        writer_plain.writerow(["Id", "Dish","Spice", "Quantity", "X","Y"])
        n_items=len(bu)
        for i in range(0, n_items):
            print(bu[i].getText().lstrip().rstrip("\n"))
            if (bu[i].select('td>ul')):
                spice = bu[i].select('td>ul>li>p')
                print(spice[0].getText())
                
                writer.writerow([5 + i,bu[i].getText().strip().rstrip("\n"),spice[0].getText(),pu[i].getText().strip()])
                writer_plain.writerow([5 + i,bu[i].getText().strip().rstrip("\n"),spice[0].getText(),pu[i].getText().strip(),0,0])
            else:
                writer.writerow([5 + i,bu[i].getText().strip().rstrip("\n"),'NA',pu[i].getText().strip()])
                writer_plain.writerow([5 + i,bu[i].getText().strip().rstrip("\n"),'NA',pu[i].getText().strip(),0,0])
plain_order_file.close()
txtfile.close()
