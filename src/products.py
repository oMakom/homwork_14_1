class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price < self.__price:
            if new_price <= 0:
                print("Цена не должна быть нулевая или отрицательная")
            else:
                is_the_price_lower = input(
                    f"Цена уменьшается с {self.__price} на {new_price} Уверены что хотите снизить цену? (y/n)"
                ).lower()
                if is_the_price_lower == "y":
                    self.__price = new_price


class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    @property
    def products(self):
        products_string = ""
        for product in self.__products:
            products_string += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_string

    def add_product(self, product_add: Product):
        for product in self.__products:
            if product.name == product_add.name:
                if product.price < product_add.price:
                    product.price = product_add.price
                product.quantity += product_add.quantity
                return True
        self.__products.append(product_add)
        Category.product_count += 1
        return True
