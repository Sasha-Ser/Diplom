import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        "name, price, type", [
            ("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
            ("sour cream", 200, INGREDIENT_TYPE_SAUCE),
            ("chili sauce", 300, INGREDIENT_TYPE_SAUCE),
            ("cutlet", 100, INGREDIENT_TYPE_FILLING),
            ("dinosaur", 200, INGREDIENT_TYPE_FILLING),
            ("sausage", 300, INGREDIENT_TYPE_FILLING)
        ])
    def test_get_name(self, name, price, type):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "name, price, type", [
            ("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
            ("sour cream", 200, INGREDIENT_TYPE_SAUCE),
            ("chili sauce", 300, INGREDIENT_TYPE_SAUCE),
            ("cutlet", 100, INGREDIENT_TYPE_FILLING),
            ("dinosaur", 200, INGREDIENT_TYPE_FILLING),
            ("sausage", 300, INGREDIENT_TYPE_FILLING)
        ])
    def test_get_type(self, name, price, type):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type

    @pytest.mark.parametrize(
        "name, price, type", [
            ("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
            ("sour cream", 200, INGREDIENT_TYPE_SAUCE),
            ("chili sauce", 300, INGREDIENT_TYPE_SAUCE),
            ("cutlet", 100, INGREDIENT_TYPE_FILLING),
            ("dinosaur", 200, INGREDIENT_TYPE_FILLING),
            ("sausage", 300, INGREDIENT_TYPE_FILLING)
        ])
    def test_get_name(self, name, price, type):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price