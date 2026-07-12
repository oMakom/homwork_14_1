from unittest.mock import patch

from src.products import Category, Product


def test_product_init(first_product):
    assert first_product.name == "Samsung"
    assert first_product.description == "256GB"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_category_init(first_category, second_category):
    assert first_category.name == "Телефоны"
    assert (
        first_category.description
        == "Современный телефон, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(first_category.products.splitlines()) == 3

    assert first_category.category_count == 2
    assert first_category.product_count == 5

    assert second_category.category_count == 2
    assert second_category.product_count == 5

    assert Category.category_count == 2
    assert Category.product_count == 5


def test_price_increase_no_input():
    """При повышении цены input() не вызывается"""
    p = Product("Samsung", "256GB", 180000.0, 5)
    p.price = 220000.0
    assert p.price == 220000.0


@patch("builtins.input", return_value="y")
def test_price_decrease_y(mock_input):
    p = Product("Samsung", "256GB", 180000.0, 5)
    p.price = 10000.0
    assert p.price == 10000.0
    mock_input.assert_called_once()


@patch("builtins.input", return_value="n")
def test_price_decrease_n(mock_input):
    p = Product("Samsung", "256GB", 180000.0, 5)
    p.price = 10000.0
    assert p.price == 180000.0
    mock_input.assert_called_once()


def test_products_empty_category():
    category = Category("Телефоны", "256GB")
    result = category.products
    assert result == ""


def test_products_single_product():
    category = Category("Телефоны", "Все телефоны")
    p = Product("Samsung", "256GB", 180000.0, 5)
    category.add_product(p)

    expected = "Samsung, 180000.0 руб. Остаток: 5 шт.\n"
    assert category.products == expected


def test_add_new_product():
    """Добавляем товар, которого ещё нет в категории."""
    category_new_product = Category("Телефоны", "Все телефоны")
    p_new_product = Product("Samsung", "256GB", 180000.0, 5)
    result = category_new_product.add_product(p_new_product)
    assert result is None
    assert len(category_new_product.products.splitlines()) == 1


def test_add_sum_product():
    """Проверяем коректность суммы стоимости 2х продуктов"""
    p = Product("Samsung", "256GB", 180000.0, 5)
    p2 = Product("Lenovo", "128GB", 60000.0, 10)
    assert p + p2 == 180000.0 * 5 + 60000.0 * 10


def test_str_product(first_product):
    """Проверяем коректность строкового отображения продуктов"""
    assert str(first_product) == "Samsung, 180000.0 руб. Остаток: 5 шт."


def test_str_Category(first_category):
    """Проверяем коректность строкового отображения категорий"""
    category = first_category
    assert str(category) == "Телефоны, количество продуктов: 27 шт."