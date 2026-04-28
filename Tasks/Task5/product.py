
class Product:
    def __init__(self, id, name, base_price):
        self.id = id
        self.name = name
        self.base_price = base_price
        
    def get_price(self):
        return self.base_price
        
    def get_details(self):
        return f"ID: {self.id} | Name: {self.name} | Price: ${self.base_price}"

class PhysicalProduct(Product):
    def __init__(self, id, name, base_price, shipping_cost):
        super().__init__(id, name, base_price)
        self.shipping_cost = shipping_cost
        
    def get_price(self):
        return self.base_price + self.shipping_cost
        
    def get_details(self):
        return super().get_details() + f" | Shipping: ${self.shipping_cost}"

class DigitalProduct(Product):
    def __init__(self, id, name, base_price):
        super().__init__(id, name, base_price)
        
    def get_price(self):
        return self.base_price
        
    def get_details(self):
        return super().get_details() + " | Type: Digital"

class DiscountedProduct(Product):
    def __init__(self, id, name, base_price, discount_percentage):
        super().__init__(id, name, base_price)
        self.discount_percentage = discount_percentage
        
    def get_price(self):
        discount_amount = self.base_price * (self.discount_percentage / 100)
        return self.base_price - discount_amount
        
    def get_details(self):
        return super().get_details() + f" | Discount: {self.discount_percentage}%"

class SubscriptionProduct(Product):
    def __init__(self, id, name, monthly_fee, duration_in_months):
        super().__init__(id, name, monthly_fee)
        self.duration_in_months = duration_in_months
        
    def get_price(self):
        return self.base_price * self.duration_in_months
        
    def get_details(self):
        return super().get_details() + f" / month | Duration: {self.duration_in_months} months"