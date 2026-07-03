import pytest

from src.utils import create_from_json, read_json_file


def test_read_json_file_not_found():
    import os

    bad_path = os.path.abspath("несуществующий_файл.json")
    with pytest.raises(FileNotFoundError):
        read_json_file(bad_path)


def test_load_categories_from_file_with_mock():
    data = [
        {
            "name": "Mocked",
            "description": "Mock desc",
            "products": [{"name": "Nokia", "description": "mobile", "price": 10.0, "quantity": 1}],
        }
    ]
    result = create_from_json(data)
    assert len(result) == 1
    assert result[0].name == "Mocked"


def test_create_from_json_wrong_type():
    with pytest.raises(TypeError):
        create_from_json("точно не список")
    with pytest.raises(TypeError):
        create_from_json({"categories": ["наверно тоже не список категорий"]})
