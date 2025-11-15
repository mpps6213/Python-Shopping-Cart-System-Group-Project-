drinks = [{'name': "Neo's Green Tea", 'code': 'N32', 'price': 3.00},
          {'name': "Melo Chocolate Malt Drink", 'code': 'M13', 'price':2.85},
          {'name': "Very-Fair Full Cream Milk", 'code': 'V76', 'price': 3.50},
          {'name': "Nirigold UHT Milk", 'code': 'N14', 'price': 4.15}]

beer = [{'name': "Lion (24 x 320 ml)", 'code': 'L11', 'price': 52.0},
        {'name': "Panda (24 x 320 ml)", 'code': 'P21', 'price': 78.0},
        {'name': "Axe (24 x 320 ml)", 'code': 'A54', 'price': 58.0},
        {'name': "Henekan (24 x 320 ml)", 'code': 'H91', 'price': 68.0}]

frozen = [{'name': "Edker Ristorante Pizza 355g", 'code': 'E11 ', 'price': 6.95},
        {'name': "Fazzler Frozen Soup 500g ", 'code': 'F43 ', 'price': 5.15},
        {'name': "CP Frozen Ready Meal 250g ", 'code': 'CP31 ', 'price': 4.12},
        {'name': "Duitoni Cheese 270g ", 'code': 'D72 ', 'price': 5.60}]

household = [{'name': "FP Facial Tissues", 'code': 'FP76', 'price': 9.50},
             {'name': "FP Premium Kitchen Towel", 'code': 'FP32', 'price': 5.85},
             {'name': "Klinex Toilet Tissue Rolls ", 'code': 'K22', 'price': 7.50},
             {'name': "Danny Softener ", 'code': 'D14', 'price': 9.85},]

snacks = [{'name': "Singshort seaweed", 'code': 'SS93', 'price': 3.10},
          {'name': "Mei crab cracker", 'code': 'MC14', 'price': 2.05},
          {'name': "Reo pokemon cookie", 'code': 'R35', 'price': 4.80},
          {'name': "Huat seng cracker", 'code': 'HS11', 'price': 3.55}]

i=0

def menu():
    print("-" * 75)
    print(f'|{"WELCOME TO MYA SHI SHOP":^73}|')
    print("-" * 75)
    print(f'|{"Category":^10}|{"Item":^40}|{"Code":^10}|{"Price":>10}|')
    print("-" * 75)
    for i in range(len(drinks)):
        print(f"|{'Drinks':^10}|{drinks[i]['name']:^40}|{drinks[i]['code']:^10}|{drinks[i]['price']:>10}|")
    for i in range(len(beer)):
        print(f"|{'Beer':^10}|{beer[i]['name']:^40}|{beer[i]['code']:^10}|{beer[i]['price']:>10}|")
    for i in range(len(frozen)):
        print(f"|{'Frozen':^10}|{frozen[i]['name']:^40}|{frozen[i]['code']:^10}|{frozen[i]['price']:>10}|")
    for i in range(len(household)):
        print(f"|{'Household':^10}|{household[i]['name']:^40}|{household[i]['code']:^10}|{household[i]['price']:>10}|")
    for i in range(len(snacks)):
        print(f"|{'Snacks':^10}|{snacks[i]['name']:^40}|{snacks[i]['code']:^10}|{snacks[i]['price']:>10}|")
    print("-" * 75)

cart=[]
item_list=['1','2','3','4']
def add_to_cart(item):
    while True:
        if item==1:
            choose_item=input("Enter item number to add to cart: ")

            if choose_item not in item_list:
                print("INVALID ENTRY")
                continue

            else:
                cart.append(drinks[int(choose_item)-1])
                try:
                    quantity = int(input("Enter quantity to add to cart:"))
                    drinks[int(choose_item) - 1]["quantity"] = quantity
                    break
                except ValueError:
                    print("INVALID ENTRY")

        elif item==2:
            choose_item=input("Enter item number to add to cart: ")

            if choose_item not in item_list:
                print("INVALID ENTRY")
                continue

            else:
                cart.append(beer[int(choose_item)-1])
                try:
                    quantity = int(input("Enter quantity to add to cart:"))
                    beer[int(choose_item) - 1]["quantity"] = quantity
                    break
                except ValueError:
                    print("INVALID ENTRY")

        elif item == 3:
            choose_item = input("Enter item number to add to cart: ")
            if choose_item not in item_list:
                print("INVALID ENTRY")
                continue

            else:
                cart.append(frozen[int(choose_item) - 1])
                try:
                    quantity = int(input("Enter quantity to add to cart:"))
                    frozen[int(choose_item)-1]["quantity"] = quantity
                    break

                except ValueError:
                    print("INVALID ENTRY")

        elif item == 4:
            choose_item = input("Enter item number to add to cart: ")
            if choose_item not in item_list:
                print("INVALID ENTRY")
                continue

            else:
                cart.append(household[int(choose_item) - 1])
                try:
                    quantity = int(input("Enter quantity to add to cart:"))
                    household[int(choose_item) - 1]["quantity"] = quantity
                    break

                except ValueError:
                    print("INVALID ENTRY")

        elif item == 5:
            choose_item = input("Enter item number to add to cart: ")
            if choose_item not in item_list:
                print("INVALID ENTRY")
                continue

            else:
                cart.append(snacks[int(choose_item) - 1])
                try:
                    quantity = int(input("Enter quantity to add to cart:"))
                    snacks[int(choose_item) - 1]["quantity"] = quantity
                    break

                except ValueError:
                    print("INVALID ENTRY")

def change_quantity():
    while True:
        change_quantity= input("Enter item number to change quantity:")
        if change_quantity not in item_list:
            print("INVALID ENTRY")
            continue

        else:
            while True:
                try:
                    update_quantity= int(input("Update quantity: "))
                    cart[int(change_quantity)-1]["quantity"]= update_quantity
                    show_cart()
                    break

                except ValueError:
                    print("INVALID ENTRY.")
def show_cart():
    print("-"*85)
    print(f"|{'YOUR SHOPPING CART':^84}|")
    print('-'*85)
    print(f"|{'No':^5}|{'Item':^40}|{'Quantity':^10}|{'Price':^10}|{'Total Price':^15}|")
    print('-'*85)
    total_price=0
    for i in range(len(cart)):
        item_price=cart[i]["quantity"]*cart[i]["price"]
        print(f"|{i+1:^5}|{cart[i]['name']:^40}|{cart[i]['quantity']:^10}|{cart[i]['price']:^10}|{item_price:^15.2f}|")
        i=i+1
        total_price= total_price+item_price
    print('-'*85)
    print(f'|{"Total before GST":>68}|{total_price:^15.2f}|')
    gst= total_price*0.09
    print(f'|{"GST Amount":>68}|{gst:^15.2f}|')
    final_total= total_price+gst
    print(f'|{"Final total with GST":>68}|{final_total:^15.2f}|')
    print('-'*85)
def remove_item():
    show_cart()
    while True:
        remove_item= int(input("Enter item number to remove from cart:"))
        if remove_item- 1 not in range(len(cart)):
            print("INVALID ENTRY")
            continue

        else:
            del cart[remove_item-1]
            show_cart()
            break
def clear_cart():
    cart.clear()
    show_cart()

def check_out():
    print("-"*20)
    membership_list=[["Senior card member",10],
                     ["MYA SHI Shop member",8],
                     ["NS Men",5],
                     ["No membership",0]]
    print("MYA SHI SHOP DISCOUNT")
    print("-"*40)
    for i in range(len(membership_list)):
        print(f"{i+1}.{membership_list[i][0]:<20}[{membership_list[i][1]}%]")
    print("-"*40)
    membership= int(input("Select membership:"))
    if membership-1 not in range(len(membership_list)):
        print("INVALID ENTRY")

    else:
        print("-" * 85)
        print(f"|{'MYA SHI SHOPPING CART':^84}|")
        print('-' * 85)
        print(f"|{'No':^5}|{'Item':^40}|{'Quantity':^10}|{'Price':^10}|{'Total Price':^15}|")
        print('-' * 85)
        total_price = 0
        for i in range(len(cart)):
            quantity = cart[i]["quantity"]
            price = cart[i]["price"]
            item_price = quantity * price
            print(
                f"|{i + 1:^5}|{cart[i]['name']:^40}|{cart[i]['quantity']:^10}|{cart[i]['price']:^10}|{item_price:^15.2f}|")
            i = i + 1
            total_price = total_price + item_price
        print('-' * 85)
        print(f'|{"Total before GST":>68}|{total_price:^15.2f}|')
        gst = total_price * 0.09
        print(f'|{"GST Amount":>68}|{gst:^15.2f}|')
        final_total = total_price + gst
        print(f'|{"Final total with GST":>68}|{final_total:^15.2f}|')
        print('-' * 85)
        discount_amount= total_price* membership_list[membership-1][1]/100
        print(f'|{"Discount amount":>68}|{discount_amount:^15.2f}|')
        total_before_gst= total_price- discount_amount
        print(f'|{"Total before GST":>68}|{total_before_gst:^15.2f}|')
        gst_amount= total_before_gst*0.09
        print(f'|{"GST Amount":>68}|{gst_amount:^15.2f}|')
        final_total= total_before_gst+gst_amount
        print(f'|{"Final Total with GST":>68}|{final_total:^15.2f}|')
        print('-' * 85)
        print("Thank you for shopping with us. Have a nice day!")

def option():
    option = ["Show all merchandise", "Add Item", "Remove Item", "Show Cart", "Clear Cart", "Change Quantity",
              "Check out"]
    print("MYA SHI Shop")
    print("-" * 75)
    while True:
        for i in range(len(option)):
            print(f"{i + 1}. {option[i]}")
            i = i + 1

        choose_option = input("Please choose an option: ")
        if choose_option == "1":
            menu()

        elif choose_option == '2':
            category = ["Drinks", "Beer", "Frozen", "Household", "Snacks"]
            for i in range(len(category)):
                print(f"{i + 1}.{category[i]}")
                i = i + 1

            choose_category = input("Please choose a category: ")
            if choose_category == "1":
                print("-" * 75)
                print(f"|{'Drinks Category':^62}|")
                print("-" * 75)
                print(f"|{'No':^10}|{'Item':^40}|{'Price':>10}|")
                for i in range(len(drinks)):
                    print(f"|{i + 1:^10}|{drinks[i]['name']:^40}|{drinks[i]['price']:>10}|")
                    i += 1
                print("-" * 75)
                add_to_cart(1)

            elif choose_category == "2":
                print("-" * 75)
                print(f"|{'Beer Category':^62}|")
                print("-" * 75)
                print(f"|{'No':^10}|{'Item':^40}|{'Price':>10}|")
                for i in range(len(beer)):
                    print(f"|{i + 1:^10}|{beer[i]['name']:^40}|{beer[i]['price']:>10}|")
                    i += 1
                print("-" * 75)
                add_to_cart(2)

            elif choose_category == "3":
                print("-" * 75)
                print(f"|{'Frozen Category':^62}|")
                print("-" * 75)
                print(f"|{'No':^10}|{'Item':^40}|{'Price':>10}|")
                for i in range(len(frozen)):
                    print(f"|{i + 1:^10}|{frozen[i]['name']:^40}|{frozen[i]['price']:>10}|")
                    i += 1
                print("-" * 75)
                add_to_cart(3)

            elif choose_category == "4":
                print("-" * 75)
                print(f"|{'Household Category':^62}|")
                print("-" * 75)
                print(f"|{'No':^10}|{'Item':^40}|{'Price':>10}|")
                for i in range(len(household)):
                    print(f"|{i + 1:^10}|{household[i]['name']:^40}|{household[i]['price']:>10}|")
                    i += 1
                print("-" * 75)
                add_to_cart(4)

            elif choose_category == "5":
                print("-" * 75)
                print(f"|{'Snacks Category':^62}|")
                print("-" * 75)
                print(f"|{'No':^10}|{'Item':^40}|{'Price':>10}|")
                for i in range(len(snacks)):
                    print(f"|{i + 1:^10}|{snacks[i]['name']:^40}|{snacks[i]['price']:>10}|")
                    i += 1
                print("-" * 75)
                add_to_cart(5)

            else:
                print("Invalid entry.")
                continue

        elif choose_option=="3":
            remove_item()

        elif choose_option=="4":
            show_cart()

        elif choose_option=="5":
            clear_cart()

        elif choose_option=="6":
            show_cart()
            change_quantity()

        elif choose_option=="7":
            check_out()
            break

        else:
            print("Invalid entry. Please choose an option between 1 and 7.")

def main():
    menu()
    option()

#=======main codes=======
main()