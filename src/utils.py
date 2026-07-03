import json
import os

from products import Category, Product


def read_json_file(path: str) -> dict:
    """Читает json и выводит словарь"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return data


def create_from_json(data: dict):
    """Читает словарь и заполняет по класам Category, Product """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    # код для проверки
    data_file = read_json_file("../data/products.json")
    categories_data = create_from_json(data_file)
    print(categories_data[0].name)
    print(categories_data[0].products)

    print(categories_data[1].name)
    print(categories_data[1].products)
