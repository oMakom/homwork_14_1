import json
import os

from src.products import Category, Product


def read_json_file(path: str) -> dict:
    """Читает json и выводит словарь"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return data


def create_from_json(data: dict):
    """Читает словарь и заполняет по класам Category, Product"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
