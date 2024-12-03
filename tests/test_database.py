import pytest
from praktikum.database import Database


class TestDatabase:

    def test_available_buns (self):
        database = Database()
        list_of_buns = []
        for bun in database.buns:
            list_of_buns.append(bun)
        assert database.available_buns() == list_of_buns

    def test_available_ingredients (self):
        database = Database()
        list_of_ingredients = []
        for ingredient in database.ingredients:
            list_of_ingredients.append(ingredient)
        assert database.available_ingredients() == list_of_ingredients

