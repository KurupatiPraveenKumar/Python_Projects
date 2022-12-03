
from datetime import datetime
name = input("Enter your Name:")

lists = '''
Rice   Rs 20/kg
Sugar  Rs 30/kg
Salt   Rs 20/kg
Oil    Rs 80/liter
paneer Rs 110/kg 
maggi  Rs 50/kg
Boost  Rs 90/each

'''

# declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

# price for items
items ={'rice' :20,
         'Sugar' :30,
         'Salt': 20,
         'Oil': 80,
         'paneer': 110,
         'maggi': 50,
         'Boost': 90
         }
option = int(input("for list of items press 1"))
#displaying items to user
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("if u want to buy press 1 or for exit press 2"))
    if inp1 == 2:
        break
        #asking user for input
    if inp1 == 1:
        item = input("enter your items:")
        quantity = int(input("enter your quantity:"))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            Finalprice=gst+totalprice
        else:
            print("entered item not in the store ")
            print("please continue shopping")
    else:
         print("you entered invalid number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        #welcomemessage
        if Finalprice!=0:
            print(25*"=","Welcome to SuperMarket",25*"=")
            print(28*"=","Hello Customer",28*"=")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("S.NO",8*" ","items",8*" ","Quantity",3*" ","Price",3*" ")
            #billgeneration
            for i in range(len(pricelist)):
                print(75 * "-")
                print(i,11*" ",ilist[i],11*" ",qlist[i],8*" ",plist[i],3*" ")
        print(75 * "-")
        print(50*" ","TotalAmount",totalprice)
        print(75*"-")
        print( "gstAmount",40*" ",gst)
        print(75 * "-")
        print(50 * " ", "FinalAmount",Finalprice)
        print(75*"=")
        print(25 * " ", "Thanks for visiting",25*" ")
        print(75*"=")






