from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app3 import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_class(self):
        response = self.client.get('/class')
        classes = ["1 Barbarian", "2 Rogue","3 Druid","4 Hunter","5 Sorcerer", "6 Shaman","7 Dragoon", "8 Samurai", "9 Tank"]
        assert response.data.decode('utf-8') in classes
