from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app1 import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_power(self):
        with patch('requests.get') as w:
            w.return_value.text = "1"
            with patch('requests.post') as p:
                p.return_value.text = "11"
                response = self.client.get(url_for('home'))
                self.assertIn(b'11', response.data)

