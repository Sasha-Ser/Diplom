import pytest

import praktikum.bun
from praktikum.burger import Burger
from unittest.mock import Mock, patch


class TestBurger:


    @pytest.fixture()
    def bun(self):
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Test bun"
        bun_mock.get_price.return_value = 220
        return bun_mock

    @pytest.fixture()
    def ingredient1(self):
        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = "Test sauce"
        ingredient_mock.get_price.return_value = 80
        ingredient_mock.get_type.return_value = "SAUCE"
        return ingredient_mock

    @pytest.fixture()
    def ingredient2(self):
        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = "Test flavour"
        ingredient_mock.get_price.return_value = 180
        ingredient_mock.get_type.return_value = "FILLING"
        return ingredient_mock

    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, ingredient1):
        burger = Burger()
        burger.add_ingredient(ingredient1)
        assert burger.ingredients == [ingredient1]

    def test_remove_ingredient(self, ingredient1, ingredient2):
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient2]

    def test_move_ingredient(self, ingredient1, ingredient2):
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2

    def test_get_price_for_buns_and_ingredients(self, bun, ingredient1, ingredient2):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_price = 700
        assert burger.get_price() == expected_price

    @patch('praktikum.bun.Bun.get_price', return_value = "Test bun")
    @patch('praktikum.ingredient.Ingredient.get_type', return_value="sauce")
    @patch('praktikum.ingredient.Ingredient.get_name', return_value="Test sauce")
    def test_get_receipt(self, bun, ingredient1, ingredient2):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        assert burger.get_receipt() == f'(==== {bun.get_name()} ====)\n= {str(ingredient1.get_type()).lower()} {ingredient1.get_name()} =\n(==== {bun.get_name()} ====)\n\nPrice: {burger.get_price()}'