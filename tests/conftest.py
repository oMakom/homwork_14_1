import pytest

from src.product_types import Smartphone, LawnGrass
from src.products import Category, Product


@pytest.fixture
def first_category():
    return Category(
        "Телефоны",
        "Современный телефон, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [
            Product("Samsung", "256GB", 180000.0, 5),
            Product("Iphone", "512GB", 210000.0, 8),
            Product("Xiaomi", "1024GB", 31000.0, 14),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [
            Product("Samsung", "256GB", 180000.0, 5),
            Product("Iphone", "512GB", 210000.0, 8),
        ],
    )


@pytest.fixture
def first_product():
    return Product("Samsung", "256GB", 180000.0, 5)


@pytest.fixture
def first_product_smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def first_product_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def smartphone_category():
    smartphone10 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone20 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    return Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone10, smartphone20])
