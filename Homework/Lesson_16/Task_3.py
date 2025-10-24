# Product Store 

class Product:                              # клас для товарів
    
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.type}) - {self.price} грн"


class ProductStore:                         # клас - продуктовий магазин
    
    def __init__(self):                     # Словник для товарів
        
        self.products = {}
        self.income = 0.0

    def add(self, product, amount):         # Додає товар до магазину з націнкою 30%."""
        
        if not isinstance(product, Product):
            raise ValueError("Можна додавати лише об'єкти класу Product.")
        if amount <= 0:
            raise ValueError("Кількість має бути більшою за 0.")

        price_with_margin = product.price * 1.3     # націнка 30%

        if product.name in self.products:
            self.products[product.name]["amount"] += amount
        else:
            self.products[product.name] = {
                "product": product,
                "amount": amount,
                "price": price_with_margin,
                "discount": 0
            }

    def set_discount(self, identifier, percent, identifier_type='name'):        # Додає знижку для товарів за назвою або типом
       
        if percent < 0 or percent > 100:
            raise ValueError("Знижка повинна бути в межах від 0 до 100%.")

        found = False
        for info in self.products.values():
            product = info["product"]
            if (identifier_type == 'name' and product.name == identifier) or \
               (identifier_type == 'type' and product.type == identifier):
                info["discount"] = percent
                found = True

        if not found:
            raise ValueError("Товар для надання знижки не знайдено.")

    def sell_product(self, product_name, amount):           # Продає вказану кількість товару, якщо його достатньо в магазині
        
        if product_name not in self.products:
            raise ValueError(f"Товар '{product_name}' відсутній у магазині.")
        if amount <= 0:
            raise ValueError("Кількість для продажу має бути більшою за 0.")

        product_info = self.products[product_name]

        if product_info["amount"] < amount:
            raise ValueError(f"Недостатньо товару '{product_name}' .")

        price = product_info["price"]               # Розрахунок ціни з урахуванням знижки
        discount = product_info["discount"]
        final_price = price * (1 - discount / 100)


        product_info["amount"] -= amount            # Зменшуємо кількість та додаємо прибуток
        self.income += final_price * amount

    def get_income(self):                           # Повертає загальний дохід магазину
        return round(self.income, 2)

    def get_all_products(self):                     # Повертає список усіх товарів із кількістю та ціною
        
        return [
            (info["product"].name, info["amount"], f"{info['price']} грн", f"Знижка: {info['discount']}%")
            for info in self.products.values()
        ]

    def get_product_info(self, product_name):        # Повертає a tuple з назвою товару та кількістю
        
        if product_name not in self.products:
            raise ValueError(f"Товар '{product_name}' відсутній у магазині.")
        info = self.products[product_name]
        return (product_name, info["amount"])

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)

print("Усі перевірки пройдено успішно!")
print("Дохід магазину:", s.get_income(), "грн")