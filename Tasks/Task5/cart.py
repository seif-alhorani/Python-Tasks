class Cart:
    def __init__(self):
    
        self.items = {}

    def add_product(self, product, quantity):
        if product.id in self.items:
            self.items[product.id]["quantity"] += quantity
        else:
            self.items[product.id] = {"product": product, "quantity": quantity}

    def remove_product(self, product_id, quantity):
        if product_id in self.items:
            current_qty = self.items[product_id]["quantity"]
            if quantity >= current_qty:
             
                del self.items[product_id]
            else:
                self.items[product_id]["quantity"] -= quantity
            return True
        return False

    def clear_cart(self):
        self.items = {}

    def calculate_total(self):
        total = 0.0
        for item in self.items.values():
            product = item["product"]
            quantity = item["quantity"]
            total += product.get_price() * quantity
        return total

    def view_cart(self):
        if len(self.items) == 0:
            return "Your cart is empty."
            
        cart_details = "--- Cart Contents ---\n"
        for item in self.items.values():
            product = item["product"]
            quantity = item["quantity"]
            cart_details += f"{product.name} (x{quantity}) - Price per unit: ${product.get_price()} - Total: ${product.get_price() * quantity}\n"
        return cart_details