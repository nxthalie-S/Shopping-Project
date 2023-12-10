import time

print ("Hello. Welcome to Jolly Bakery!! :)") 
cart =  []
print (" ")

cake_options = ["Strawberry Cake","Angel Cake",  "Sponge Cake", "Lava Cake",
      "Ice Cream Cake" ]
cookie_options= ["Red Velvet", "Chocolate Chip", "White Chocolate",
                 "Fortune Cookie", "Macarons"]
drink_options = ["Water", "Hot Chocolate", "Hot Tea", "Iced Coffee", "Juice", "Smoothie"]

print ("We sell a variety of treats here such as Cakes, Cookies, and Drinks.")
print (" ")                                                             
time.sleep(0.5)


print ("Here are the flavor options for Cakes" , cake_options)
print ("")
cake_choice = input("Would you like to purchase cake today? Please enter yes or no: ") 
cost1 = 0


if cake_choice.lower() == "yes" :
  print ("Wonderful.")
  time.sleep(1)
  cake_type = input(
     "Would you like a whole cake or a slice? Please enter whole or slice : ")

  if cake_type.lower() == "slice":
     cake_flavor_slice  = input("Please enter the type of cake of your choice: ")
     if cake_flavor_slice.lower() == "strawberry cake":
        cost1 = 3.50    
        cart.append("Strawberry Cake")
        print("Great Choice!")
        print(cart)
     elif cake_flavor_slice.lower() == "angel cake":
        cost1 = 4.50
        cart.append("Angel Cake")
        print("Good Choice!")
        print(cart)
     elif cake_flavor_slice.lower() == "sponge cake":
         cost1 = 3.00
         cart.append("Sponge Cake")
         print("Good Choice. Such a simple yummy cake!")
         print(cart)
     elif cake_flavor_slice.lower() == "lava cake":
         cost1 = 6.00
         cart.append("Lava Cake")
         print("Great Choice. I see you are a fan of chocolate.")
         print(cart)
     elif cake_flavor_slice.lower() == "ice cream cake":
         cost1 = 7.00
         cart.append("Ice Cream Cake")
         print("Great choice, especially when it's a hot day")
         print(cart)
     else :
         print("Please enter an available choice")

  elif cake_type.lower() == "whole":
     cake_flavor = input ("Please enter the cake flavor of your choice: ")
     if cake_flavor.lower() == "strawberry cake":
        cost1 = 45.00
        cart.append("Strawberry Cake")
        print("Great Choice!")
        print(cart)
     elif cake_flavor.lower() == "angel cake":
        cost1 = 55.00
        cart.append("Angel Cake")
        print("Good Choice!")
        print(cart)
     elif cake_flavor.lower() == "sponge cake":
        cost1 = 40.00
        cart.append("Sponge Cake")
        print("Good Choice. Such a simple yummy cake!")
        print(cart)
     elif cake_flavor.lower() == "lava cake":
        cost1 = 50.00
        cart.append("Lava Cake")
        print("Great Choice. I see you are a fan of chocolate.")
        print(cart)
     elif cake_flavor.lower() == "ice cream cake":
        cost1 = 65.00
        cart.append("Ice Cream Cake")
        print("Great choice, especially when it's a hot day")
        print(cart)

     else :
        print("Please enter an available choice")

elif cake_choice.lower() == "no" :
  print ("On to the next category.")

else :
  print("Please enter yes or no.")
  
  
print("")
time.sleep(1)
print ("Our cookie options are the following :", cookie_options )
print(" ")
cookie_choice = input("Are you interested in purchasing one of our cookies today? Type yes or no : ")
cost2 = 0
if cookie_choice.lower() ==  "yes" :
   cookie_order = input("Great! Enter what type of cookie you would like : ")
   if cookie_order.lower() == "red velvet":
    cost2 = 4.25
    cart.append("Red Velvet")
    print ("Good Choice!")
    print(cart)
   elif cookie_order.lower() == "chocolate chip":
    cost2 = 3.00
    cart.append("Chocolate Chip")
    print("Good choice, a classic cookie!")
    print(cart)
   elif cookie_order.lower() == "white chocolate":
     cost2 = 4.00
     cart.append("White Chocolate")
     print("Good Choice!")
     print(cart)
   elif cookie_order.lower() == "fortune cookie":
     cost2 = 2.00
     cart.append("Fortune Cookie")
     print("Great Choice. Hopefully you have a good fortune.")
     print(cart)
   elif cookie_order.lower() == "macarons":
     cost2 = 5.50
     cart.append("Macarons")
     print("Great Choice :)")
     print(cart)
   else :
     print("Please enter an available choice")

elif cookie_choice.lower() == "no" :
  print("Too bad. On to the drinks.")

else:
  print("Please enter yes or no")


print (" ")
time.sleep(1)
print ("Our last category are drinks : " , drink_options)
drink_choice = input("Would you like to buy a drink today? Please enter yes or no: ")
cost3 = 0
if drink_choice.lower() == "yes" :
   drink_order = input("Okay. Please enter the drink of your choice: ")
   if drink_order.lower() == "water":
     cost3 = 1.00
     cart.append("Water")
     print("Good Choice. Can never go wrong with water!")
     print(cart)
   elif drink_order.lower() == "hot chocolate":
     cost3 = 4.00
     cart.append("Hot Chocolate")
     print("Great choice! Such a cozy drink.")
     print(cart)
   elif drink_order.lower() == "hot tea":
     cost3 = 2.50
     cart.append("Hot Tea")
     print("Good Choice, especially during cold weather")
     print(cart)
   elif drink_order.lower() == "iced coffee":
     cost3 = 6.75
     cart.append("Iced Coffee")
     print("Great Choice")
     print(cart)
   elif drink_order.lower() == "juice":
     cost3 = 4.50
     cart.append("Juice")
     print("Such a refreshing drink!")
     print(cart)
   elif drink_order.lower() == "smoothie":
     cost3 = 7.00
     cart.append("Smoothie")
     print("Great choice :)")
     print(cart)
   else :
     print("Please enter an available drink option")

elif drink_choice.lower() == "no":
  print("Umm you're going to dehydrate yourself. oh well.")

else:
  print("You have to enter yes or no")



print(" ")


total = cost1 + cost2 + cost3
size = len(cart)
while size > 0 :
  print("The following is the items in your cart", cart)
  print("Your current total is $" , total)
  removal =input("Would you like to remove any items from your cart? Enter yes or no: ")
  if removal == "yes":
   itemRemoval=input("Which item would you like to remove. Please type the item as displayed: ")
   if itemRemoval == cart[0]:
     cart.remove(itemRemoval)
     total = total - cost1
   elif itemRemoval == cart[1]:
     cart.remove(itemRemoval)
     total = total - cost2
   elif itemRemoval == cart [2]:
     cart.remove(itemRemoval)
     total = total - cost3
   else:   
     size -= 1
     time.sleep(1)
     print("Your new cart is " , cart)
     print( "Your new total is $", total)
     print("  ") 
  else :
   print("Thank you for shopping at Jolly Bakery. Let's head to checkout.") 
   break

print(" ")
if total < 0:
  print ("Thank you for visiting Jolly Bakery today. Come again!")

else:
  print("Your total without tax is $", total)
  time.sleep(1)
  total = total * .6 + total
  print("With tax, your new total is $", total, ". Thank you for shopping at Jolly Bakery! Hope you come again!")

  
    
    
     








