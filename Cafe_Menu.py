#Define the menu of cafe
Menu={
    "Pizza":50,
    "Burger":40,
    "Pasta":45,
    "Coffe":80,
    "Salad":60
}


#Greet
print("Welcome to our cafe")
print("Pizza:50\nBurger:40\nPasta:45\nCoffe:80\nSalad:60")

order_total=0

item_1 =input("Enter the name of item you want to order= ")
if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"your order {item_1} has been added to your order")

else:
    print(f"your order {item_1} is not availaible yet!") 

another_order =input("Do you want to add another item in your order(Yes/No)")
if another_order == "Yes" :
    item_2 =input("Enter the name of item you want add to order= ")   
    if item_2 in Menu:
        order_total += Menu[item_2]
        print(f"your order {item_2} has been added to your order")
    else:
        print(f"your order {item_2} is not availaible yet!") 
  
print(f"The total amount of item to pay is {order_total} ")