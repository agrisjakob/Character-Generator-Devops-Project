from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app2 import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_class(self):
        response = self.client.get('/weapons')
        weapons= ["1 Axe", "2 Dagger", "3 Staff", "4 Bow", "5 Wand", "6 Mace","7 Spear", "8 Sword", "9 Shield"]
        assert response.data.decode('utf-8') in weapons
