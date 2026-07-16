# homwork_14_1
## Установка:

1. Клонируйте репозиторий:
```
https://github.com/oMakom/homwork_14_1.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
poetry install
```
### Реализация работы с классами и заполенния классов из файла json
- Классы реализованы в модуле products.py
- - Product(name: str, description: str, price: float, quantity: int)
- - Category(name: str, description: str, products: list[Product])
- Наследники класса Product реализованы в модуле product_types.py
- - Smartphone(...., efficiency: int, model: str, memory: int, color: str)
- - LawnGrass(...., country: str, germination_period: str, color: str)
- функционал чтения и записи в файл реализован в модуле utils.py
- пробный вызов функционала вызван в модуле main.py