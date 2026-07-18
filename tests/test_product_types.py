def test_smartphone_init(first_product_smartphone):
    """Проверка корректности создания"""
    assert first_product_smartphone.efficiency == 95.5
    assert first_product_smartphone.model == "S23 Ultra"
    assert first_product_smartphone.memory == 256
    assert first_product_smartphone.color == "Серый"


def test_grass_init(first_product_grass):
    """Проверка корректности создания"""
    assert first_product_grass.country == "Россия"
    assert first_product_grass.germination_period == "7 дней"
    assert first_product_grass.color == "Зеленый"
