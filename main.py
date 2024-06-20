from datetime import datetime
import pandas as pd
import datetime, time
import sys 

class BakerySystem:

    
    def __init__(self) :
        self.order = pd.DataFrame(columns=['name', 'order', 'quantity', 'datetime', 'orderid','price'])
        self.next_orderid = 1

    def add_order(self):
        total_price = 0
        name = input("Enter the Name of customer: ")
        while True:
            order = int(input("Enter the Number of order from menu: "))
            quantity = int(input("Enter the Quantity of the order: "))
            if order == 1:
                order = "Egg"
                price = quantity * 20
            elif order == 2:
                order = "Bread"
                price = quantity * 150
            elif order == 3:
                order = "Rusk"
                price = quantity * 200
            elif order == 4:
                order = "Cake Rusk"
                price = quantity * 20
            elif order == 5:
                order = "Cake"
                price = quantity * 500
            elif order == 6:
                order = "Cold Drinks"
                price = quantity * 200
            else:
                print("Enter Right Number!!!!")
                break  
            total_price += price
            ask = input("Do you want to add more order?(Y/n)")
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            order_Id = self.next_orderid
            self.next_orderid += 1
            new_order = pd.DataFrame([[name, order, quantity, date_time, order_Id, price]],
                                    columns=['name', 'order', 'quantity', 'datetime', 'orderid', 'price'])
            self.order = pd.concat([self.order, new_order], ignore_index=True)
            
            if ask.lower() == 'n':
                print(f"Total Price: Rs.{total_price}")
                break
            else:
                continue

    def view_order(self):
        if self.order.empty:
            print("The order is empty")  
        else:
            print(self.order)
            
    def update_order(self):
        inp_name = input("Enter the name: ")
        idx = self.order.index[self.order['name'] == inp_name].tolist()
        if idx:
            price = 0
            order = int(input("Enter the new order"))
            quantity = int(input("Enter the new quantity: "))
            if order == 1:
                order = "Egg"
                price = quantity*20
            elif order == 2:
                order = "Bread"
                price = quantity*150
            elif order == 3:
                order = "Rusk"
                price = quantity*200
            elif order == 4:
                order = "Cake Rusk"
                price = quantity*20
            elif order == 5:
                order = "Cake"
                price = quantity*500
            elif order == 6:
                order = "Cold Drinks"
                price = quantity*200
            print("Updating the Order ID")
            self.order.at[0, 'order'] = order
            self.order.at[0, 'quantity'] = quantity
            self.order.at[0, 'orderid'] = input("Enter the new order ID: ")
            self.order.at[0, 'datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.order.at[0, 'price'] = price
            print(f"Your Updated Bill is Rs.{price}")
            print("Order updated successfully!")
        else:
            print("Enter the Valid Name of the user")
            
    def convert_to_excel(self):
        self.order.to_csv("Bakery Management Sheet.csv",index=False)

if __name__ == "__main__":
    ban = BakerySystem()
    print("                      Welcome to the Abdul Wahab Bakery Management System🍔🍞🏪\n")
    time.sleep(3)
    print("<------Our Menu List------>\n")
    print("1. Eggs - 20        2. Bread - 150\n3. Rusk - 200       4. Cake Rusk - 20\n5. Cake - 500       6. Cold Drinks - 200")
    pass
    while True:
        time.sleep(2)
        choice = int(input("\n\nEnter the Number of Option you Select:\n1. Add Order\n2. View Order\n3. Update Order\n4. Save to Excel\n5. Exit\nEnter Here: "))
        if choice == 1:
            ban.add_order()
        elif choice == 2:
            ban.view_order()
        elif choice == 3:
            ban.update_order()
        elif choice == 4:
            ban.convert_to_excel()
        elif choice == 5:
            sys.exit()


