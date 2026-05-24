from models.store import Store, Product
from utils.storage import save_products, load_products


def menu():
    print("\n===== ONLINE STORE =====")
    print("1. Add product")
    print("2. List products")
    print("3. Add to cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Save")
    print("7. Quit")


def main():
    store = Store()
    store.products = load_products()

    while True:
        menu()
        choice = input("Choose option: ")

        try:
            # ADD PRODUCT
            if choice == "1":
                pid = int(input("ID: "))
                name = input("Name: ")
                price = float(input("Price: "))
                stock = int(input("Stock: "))

                store.add_product(Product(pid, name, price, stock))
                print("Product added.")

            # LIST PRODUCTS
            elif choice == "2":
                for p in store.list_products():
                    print(p)

            # ADD TO CART
            elif choice == "3":
                pid = int(input("Product ID: "))
                qty = int(input("Quantity: "))
                result = store.add_to_cart(pid, qty)
                print(result)

            # VIEW CART
            elif choice == "4":
                for item in store.view_cart():
                    print(
                        f"{item.product.name} x {item.quantity} = ${item.total()}")
                print("TOTAL:", store.cart_total())

            # CHECKOUT
            elif choice == "5":
                total = store.cart_total()
                print(f"💰 Total to pay: ${total}")
                store.clear_cart()
                print("Checkout complete!")

            # SAVE 
            elif choice == "6":
                save_products(store.products)
                print("Saved.")

            # QUIT
            elif choice == "7":
                save_products(store.products)
                print("Goodbye Jaale!")
                break

            else:
                print("Invalid option")

        except ValueError:
            print("❌ Invalid input!")


if __name__ == "__main__":
    main()
