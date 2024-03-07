from datetime import datetime
class Product:
    def __init__ (self,product_id,name, quantity_in_stock):
        self.product_id=product_id
        self.name=name
        self.quantity_in_stock=quantity_in_stock
    def calculate_value(self):
        pass
class SimpleProduct(Product):
    def __init__(self,product_id,name, quantity_in_stock,unit_price):
       super().__init__(product_id,name,quantity_in_stock)
       self.unit_price=unit_price
    def calculate_value(self):
        return self.quantity_in_stock*self.unit_price
class PerishableProduct(Product):
    def __init__ (self,product_id,name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id,name,quantity_in_stock)
        self.unit_price=unit_price
        self.expiry_date=expiry_date
    def calculate_value(self):
        remaining_shelf_life = (self.expiry_date - datetime.now()).days
        if remaining_shelf_life > 0:
            max_discount = 0.7
            discount_factor =1 - (1 / remaining_shelf_life) * max_discount
            return self.quantity_in_stock * self.unit_price * discount_factor
        else:
            return 0
class DigitalProduct(Product):
    def __init__ (self,product_id,name, quantity_in_stock, price):
        super().__init__(product_id,name,quantity_in_stock)
        self.price=price
    def calculate_value(self):
        return self.quantity_in_stock*self.price
simple_Product=SimpleProduct(4,"i",34,2.5)
perishable_product=PerishableProduct(5,"Fresh produce",45,1.3, datetime(2024,3,7))
digital_product=DigitalProduct(6,"E-citizen",10,50)
print(simple_Product.calculate_value())
print(perishable_product.calculate_value())
print(digital_product.calculate_value())