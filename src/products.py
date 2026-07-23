from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self) -> str:
        """Информация о продукте"""
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        """Вывод общей цены продуктов"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_dict: dict):
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Product(ABC, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is type(self):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict):
        """Создает новый продукт из словаря."""
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


class CatalogEntity(ABC):
    @abstractmethod
    def __str__(self):
        """Вывод Иформации о классе и его содержимом"""
        pass

    @abstractmethod
    def add_product(self, product_add: Product):
        """Добавление продуктов в класс"""
        pass


class Category(CatalogEntity):
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

    def middle_price(self):
        """метод, который подсчитывает средний ценник всех товаров"""
        try:
            catalog_middle_price = round(
                sum((product.price / product.quantity) for product in self.__products) / len(self.__products), 2
            )
        except ZeroDivisionError:
            catalog_middle_price = 0
        return catalog_middle_price


class Order(CatalogEntity):
    order_id: int
    description: str
    products: list[Product]
    product_count: int

    def __init__(self, order_id, products: list[Product] | None = None):
        self.order_id = order_id
        self.__products = products if products is not None else []
        self.product_count = len(self.__products) if products else 0

    def __str__(self):
        return (
            f"Заказ №{self.order_id}, количество продуктов: {sum(product.quantity for product in self.__products)} шт."
        )

    def add_product(self, product_add: Product):
        if not isinstance(product_add, Product):
            raise TypeError
        self.__products.append(product_add)
        self.product_count += 1
        return

    @property
    def products(self):
        return self.__products


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
