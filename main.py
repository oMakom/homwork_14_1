from src.products import Category, CategoryProductIterator, Product
from src.utils import create_from_json, read_json_file

if __name__ == "__main__":
    # код для проверки
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
    print(f"Это пример строки категории: {category1}")
    print("-----------------Тестовый тест для проверки задания со звездочкой------------------\n")
    for i in CategoryProductIterator(category1):
        print(i)

    # код для проверки Utils

    print("-----------------Тестовый тест для файла------------------\n")

    data_file = read_json_file("data/products.json")

    categories_data = create_from_json(data_file)

    print(categories_data[0].name)

    print(categories_data[0].products)

    print(categories_data[1].name)

    print(categories_data[1].products)
