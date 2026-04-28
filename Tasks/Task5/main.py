from product import PhysicalProduct, DigitalProduct, DiscountedProduct, SubscriptionProduct
from store_system import StoreSystem

def main():
    store = StoreSystem()
    
    while True:
        print("\n=== Online Store System ===")
        print("1. Add a new product")
        print("2. Display all products")
        print("3. Search for a product by ID")
        print("4. Add product to cart")
        print("5. Remove product from cart")
        print("6. View cart contents")
        print("7. Calculate total price")
        print("8. Clear cart")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            print("\nSelect Product Type:")
            print("1. Physical Product")
            print("2. Digital Product")
            print("3. Discounted Product")
            print("4. Subscription Product")
            
            type_choice = input("Enter type (1-4): ")
            
            if type_choice not in ['1', '2', '3', '4']:
                print("Invalid product type selection!")
                continue
                
            id = input("Enter product ID: ")
            
            
            if store.find_product_by_id(id) != None:
                print("Error: Product ID already exists!")
                continue
                
            name = input("Enter product name: ")
            base_price = float(input("Enter base price: ")) # need to be fixed handle input  
            
            if base_price < 0:
                print("Error: Price cannot be negative!")
                continue
                
            if type_choice == '1':
                shipping = float(input("Enter shipping cost: "))
                if shipping < 0:
                    print("Error: Shipping cost cannot be negative!")
                    continue
                new_product = PhysicalProduct(id, name, base_price, shipping)
                
            elif type_choice == '2':
                new_product = DigitalProduct(id, name, base_price)
                
            elif type_choice == '3':
                discount = float(input("Enter discount percentage (0-100): "))
                if discount < 0 or discount > 100:
                    print("Error: Invalid discount value!")
                    continue
                new_product = DiscountedProduct(id, name, base_price, discount)
                
            elif type_choice == '4':
                duration = int(input("Enter duration in months: "))
                if duration <= 0:
                    print("Error: Invalid duration!")
                    continue
                new_product = SubscriptionProduct(id, name, base_price, duration)
                
            if store.add_product(new_product):
                print("Product added successfully!")
                
        elif choice == '2':
            print("\n" + store.display_all_products())
            
        elif choice == '3':
            id = input("Enter product ID to search: ")
            product = store.find_product_by_id(id)
            if product:
                print("\nProduct found:")
                print(product.get_details())
            else:
                print("\nProduct not found!")
                
        elif choice == '4':
            id = input("Enter product ID to add to cart: ")
            product = store.find_product_by_id(id)
            
            if product == None:
                print("Error: Product does not exist!")
            else:
                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print("Error: Quantity must be greater than zero!")
                else:
                    store.cart.add_product(product, qty)
                    print(f"Added {qty} of {product.name} to cart.")
                    
        elif choice == '5':
            id = input("Enter product ID to remove from cart: ")
            
            if id not in store.cart.items:
                print("Error: Product is not in the cart!")
            else:
                qty = int(input("Enter quantity to remove: "))
                if qty <= 0:
                    print("Error: Quantity must be greater than zero!")
                else:
                    store.cart.remove_product(id, qty)
                    print("Cart updated.")
                    
        elif choice == '6':
            print("\n" + store.cart.view_cart())
            
        elif choice == '7':
            total = store.cart.calculate_total()
            print(f"\nTotal Price in Cart: ${total:.2f}")
            
        elif choice == '8':
            store.cart.clear_cart()
            print("Cart has been cleared!")
            
        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break
            
        else:
            print("Invalid menu input. Please try again.")

if __name__ == "__main__":
    main()