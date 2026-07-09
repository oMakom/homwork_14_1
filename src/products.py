class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    __products: list
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

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1
