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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is type(self):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError

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
        else:
            self.__price = new_price


class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products: list[Product] | None = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт."

    @property
    def products(self):
        products_string = ""
        for product in self.__products:
            products_string += f"{str(product)}\n"
        return products_string

    def add_product(self, product_add: Product):
        if not isinstance(product_add, Product):
            raise TypeError
        for product in self.__products:
            if product.name == product_add.name:
                if product.price < product_add.price:
                    product.price = product_add.price
                product.quantity += product_add.quantity
                return
        self.__products.append(product_add)
        Category.product_count += 1
        return


class CategoryProductIterator:
    """класс, с помощью которого можно перебирать товары одной категории"""

    def __init__(self, category_iter: Category):
        #  Итерируется по приватному списку объектов (category._Category__products)
        self.products_iter = category_iter._Category__products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.products_iter):
            raise StopIteration
        product = self.products_iter[self.index]
        self.index += 1
        return product
