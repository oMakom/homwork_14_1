import pytest

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
