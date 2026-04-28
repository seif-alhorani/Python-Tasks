from cart import Cart

class StoreSystem:
    def __init__(self):
        self.products = []
        self.cart = Cart()

    def add_product(self, product):
      
        if self.find_product_by_id(product.id) != None:
            return False
        self.products.append(product)
        return True

    def find_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def display_all_products(self):
        if len(self.products) == 0:
            return "No products in the store."
            
        details = "--- All Products ---\n"
        for product in self.products:
            details += product.get_details() + "\n"
        return details