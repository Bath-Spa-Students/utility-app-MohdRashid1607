#creating a vending machine

print("Hello")
print("______________________________")
print("WELCOME TO VENDING MACHINE")
print("*******************************************************************************")

#Codes of the Items in the shop
items={
   '1111' : 'Twizzlers' , 
   '2222' : 'Twix' , 
   '3333' : 'Hersheys' , 
   '4444' : 'Oreo' , 
   '5555' : 'Skittles' , 
   '6666' : 'Kitkat' , 
   '7777' : 'Doritos' , 
   '8888' : 'Mountain Dew' , 
   '9999' : 'Fanta' ,
   '1122' : 'Gatorade' , 
   '1133' : 'Redbull' , 
   '1144' : 'Pepsi' , 
   '1155' : 'Barbican' ,
   '1166' : 'Water' ,
   '1177' : 'Sprite', 
}

print("MENU OF SnackShop")
print("******************************************************************************")
print("*1. Twizzlers                   AED 10 ,   *   Code: 1111 ,    *     Stock:20*")
print("*2. Twix                        AED 10 ,   *   Code: 2222 ,    *     Stock:30*")
print("*3. Hersheys                    AED 15 ,   *   Code: 3333 ,    *    Stock:50 *")
print("*4. Oreo                        AED 10 ,   *   Code: 4444 ,    *     Stock:10*")
print("*5. Skittles                    AED 15 ,   *   Code: 5555 ,    *     Stock:30*")
print("*6. Kitkat                      AED 05 ,   *   Code: 6666 ,    *     Stock:80*")
print("*7. Doritos                     AED 10 ,   *   Code: 7777 ,    *     Stock:10*")
print("                           ...MENU OF DRINKS...                               ")
print("*8. Mountain Dew                AED 10 ,   *   Code: 8888 ,    *     Stock:10*")
print("*9. Fanta                       AED 10 ,   *   Code: 9999 ,    *     Stock:20*")
print("*10. Gatorade                   AED 20 ,   *   Code: 1122 ,    *     Stock:60*")
print("*11. Redbull                    AED 20 ,   *   Code: 1133 ,    *     Stock:80*")
print("*12. Pepsi                      AED 10 ,   *   Code: 1144 ,    *     Stock:10*")
print("*13. Barbican                   AED 15 ,   *   Code: 1155 ,    *    Stock:85* ")
print("*14. Water                      AED 01 ,   *   Code: 1166 ,    *     Stock:45*")
print("*15. Sprite                     AED 10 ,   *   Code: 1177 ,    *     Stock:15*")   
print("******************************************************************************")

#Price of items in the shop
Twizzlers=10
Twix=10
Hersheys=15
Oreo=10
Skittles=15
Kitkat=5
Doritos=10
MountainDew=10
Fanta=10
Gatorade=20
Redbull=20
Pepsi=10
Barbican=15
Water=1
Sprite=10

# check stock
stock=3000
if stock > 0:
    print("________________________")
    print("We have snacks and beverages in stock. Please make your selection.")
    print("_______________________")


#This is for Entering The Product Code      
items_code=input('Please enter the Product Code you would like to buy:')

# Enter the Amount of Money
money=int(input("Thankyou for your selection .Please insert the money"))



#Choice for Additional Item
choice = {
   '1': 'yes' ,
   '2': 'no'
}
choice=input('Snackers and Drinkers would like to suggest you to have some chocolate? (ok/no):')
if choice== 'ok':
   print("...............................")
   print("Thankyou for your Selection")
elif choice== 'no':
   print("Thankyou for your Selection")

   #Calculating and Returning the Correct Change Of Twizzlers
   if items_code=='1111':
      if money >= Twizzlers:
         money=money-Twizzlers

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Twix
   if items_code=='2222':
      if money >= Twix:
         money=money-Twix

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Hersheys
   if items_code=='3333':
      if money >= Hersheys:
         money=money-Hersheys

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Oreo
   if items_code=='4444':
      if money >= Oreo:
         money=money-Oreo

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Skittles
   if items_code=='5555':
      if money >= Skittles:
         money=money-Skittles

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Kitkat
   if items_code=='6666':
      if money >= Kitkat:
         money=money-Kitkat

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Dortitos
   if items_code=='7777':
      if money >= Doritos:
         money=money-Doritos

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Mountain Dew
   if items_code=='8888':
      if money >= MountainDew:
         money=money-MountainDew

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Fanta
   if items_code=='9999':
      if money >= Fanta:
         money=money-Fanta

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Gatorade
   if items_code=='1122':
      if money >= Gatorade:
         money=money-Gatorade

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Redbull
   if items_code=='1133':
      if money >= Redbull:
         money=money-Redbull

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Pepsi
   if items_code=='1144':
      if money >= Pepsi:
         money=money-Pepsi

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Barbican
   if items_code=='1155':
      if money >= Barbican:
         money=money-Barbican

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Water
   if items_code=='1166':
      if money >= Water:
         money=money-Water

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")

         



         #Calculating and Returning the Correct Change Of Sprite
   if items_code=='1177':
      if money >= Sprite:
         money=money-Sprite

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")