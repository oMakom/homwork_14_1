from src.products import Product, Category


def test_product_init(first_product):
    assert first_product.name == "Samsung"
    assert first_product.description == "256GB"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_category_init(first_category, second_category):
    assert first_category.name == "Телевизоры"
    assert (
        first_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(first_category.products) == 3

    assert first_category.category_count == 2
    assert first_category.product_count == 5

    assert second_category.category_count == 2
    assert second_category.product_count == 5

    assert Category.category_count == 2
    assert Category.product_count == 5
