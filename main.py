def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def get_price(choice):
    prices = [3.50, 5.00, 4.00, 2.45]
    return prices[choice - 1]


def main():
    orders = []
    total = 0.0

    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    while True:
        print_menu()
        choice = int(input("Enter your selection: "))

        if choice == 5:
            break
        elif choice >= 1 and choice <= 4:
            items = ["Taco", "Burrito", "Nachos", "Soft Drink"]
            item = items[choice - 1]

            print("You have selected a", item)
            price = get_price(choice)
            total += price
            orders.append(item)
        else:
            print("Invalid selection. Please try again.")

    print("\nYour order:")
    if orders:
        for item in orders:
            print(item)
    else:
        print("No items ordered.")

    print(f"Your total is ${total:.2f}")


main()