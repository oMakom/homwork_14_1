from src.products import Category, Product
from src.utils import create_from_json, read_json_file

if __name__ == "__main__":
    # код для проверки
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product_2 = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 150000.0,
         "quantity": 1})
    print(new_product_2.name)
    print(new_product_2.description)
    print(new_product_2.price)
    print(new_product_2.quantity)
    print("-----------------Тестовый тескт для добавления------------------\n")
    category2 = Category(
        "Смартфоны------------",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product3]
    )
    print(category2.product_count)
    category2.add_product(new_product)
    category2.add_product(new_product_2)
    print(category2.products)
    print(category2.product_count)
    print("-----------------Тестовый тескт для цены------------------\n")
    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

    # код для проверки Utils

    print("-----------------Тестовый тескт для файла------------------\n")

    data_file = read_json_file("data/products.json")

    categories_data = create_from_json(data_file)

    print(categories_data[0].name)

    print(categories_data[0].products)

    print(categories_data[1].name)

    print(categories_data[1].products)
