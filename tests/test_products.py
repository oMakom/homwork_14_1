from unittest.mock import patch

import pytest

from src.products import Category, CategoryProductIterator, Order, Product


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


def test_error_add_new_product(smartphone_category):
    """Проверка? что при добавлении не смартфонов, травы газонной или других продуктов вызывается TypeError"""
    with pytest.raises(TypeError):
        smartphone_category.add_product("Not a product")


def test_add_sum_product():
    """Проверяем коректность суммы стоимости 2х продуктов"""
    p = Product("Samsung", "256GB", 180000.0, 5)
    p2 = Product("Lenovo", "128GB", 60000.0, 10)
    assert p + p2 == 180000.0 * 5 + 60000.0 * 10


def test_error_add_sum_product(first_product_smartphone, first_product_grass):
    """Проверяем ошибки суммы стоимости 2х разных продуктов"""
    with pytest.raises(TypeError):
        first_product_smartphone + first_product_grass


def test_str_product(first_product):
    """Проверяем коректность строкового отображения продуктов"""
    assert str(first_product) == "Samsung, 180000.0 руб. Остаток: 5 шт."


def test_str_Category(first_category):
    """Проверяем коректность строкового отображения категорий"""
    category = first_category
    assert str(category) == "Телефоны, количество продуктов: 27 шт."


def test_CategoryProductIterator(first_category):
    """Проверяем коректность вывода списка товаров класса"""
    pit = Product("Samsung", "256GB", 180000.0, 5)
    pit2 = Product("Iphone", "512GB", 210000.0, 8)
    pit3 = Product("Xiaomi", "1024GB", 31000.0, 14)
    category_iterator = CategoryProductIterator(first_category)
    assert str(next(category_iterator)) == str(pit)
    assert str(next(category_iterator)) == str(pit2)
    assert str(next(category_iterator)) == str(pit3)


def test_PrintMixin(capsys):
    """Проверяем коректность вывода сообщения при инициализации продуктов"""
    pit = Product("Samsung", "256GB", 180000.0, 5)
    str(pit)
    captured = capsys.readouterr()
    expected = "Product('Samsung', '256GB', 180000.0, 5)\n"
    assert captured.out == expected


def test_order_creation():
    p1 = Product("Samsung", "256GB", 180000.0, 5)
    p2 = Product("Iphone", "512GB", 210000.0, 8)
    order = Order(102, [p1, p2])

    assert order.order_id == 102
    assert len(order.products) == 2
    assert order.products[0] is p1
    assert order.products[1] is p2
    assert order.product_count == 2  # теперь это корректно
    assert str(order) == "Заказ №102, количество продуктов: 13 шт."


def test_add_product_wrong_type():
    """Ошибка при добавлении не продукта"""
    order = Order(105)
    with pytest.raises(TypeError):
        order.add_product("not a product")


def test_add_product_allows_duplicates_by_name():
    """Проверка добавления товара с токим же именем"""
    p1 = Product("Xiaomi", "1024GB", 31000.0, 14)
    p2 = Product("Xiaomi", "Pro", 35000.0, 2)

    order = Order(104, [p1])
    order.add_product(p2)

    assert len(order.products) == 2
    assert order.products[0] is p1
    assert order.products[1] is p2
    assert order.product_count == 2
    assert str(order) == "Заказ №104, количество продуктов: 16 шт."


def test_product_invalid():
    """Ошибка добавления товара с нулевым количеством"""
    with pytest.raises(ValueError) as e:
        product_test = Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_middle_price(first_category):
    """Проверка корректности подсчета среднего ценника всех товаров"""
    assert  Category.middle_price(first_category) == 21488.1


def test_middle_price_ZeroDivisionError():
    """Ошибка, если 0 продуктов в категории (средняя цена приравнивается нулю)"""
    category_empty = Category("Пустая категория", "Категория без продуктов", [])

    assert Category.middle_price(category_empty) == 0
