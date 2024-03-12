class ECommerce:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name, price, quantity):
        product = {
            'name': product_name,
            'price': price,
            'quantity': quantity
        }
        self.products[product_name] = product
        return product

    def update_price(self, product, new_price):
        product['price'] = new_price
        return product

    def update_quantity(self, product, quantity_change):
        product['quantity'] += quantity_change
        if product['quantity'] < 0:
            raise ValueError("Quantity cannot be negative")
        return product
ecommerce = ECommerce()

# Add a product
product = ecommerce.add_product('Product 1', 10.0, 10)
print(product)

# Update the price of the product
updated_product = ecommerce.update_price(product, 12.0)
print(updated_product)

# Update the quantity of the product
updated_product = ecommerce.update_quantity(updated_product, 5)
print(updated_product)

# Try to update the quantity to a negative value
try:
    updated_product = ecommerce.update_quantity(updated_product, -10)
except ValueError as e:
    print(e)