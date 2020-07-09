from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from random import randint
from app4 import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_matching_power_high_roll(self):
        with patch('random.choice',return_value = 99):
            response = self.client.post('/power', data="11")
            base = list(range(600,1001))
            assert int(response.data.decode('utf-8')) in base

    def test_not_matching_power_high_roll(self):
        with patch('random.choice',return_value= 100):
            response = self.client.post('/power', data="13")
            base = list(range(500,801))
            assert int(response.data.decode('utf-8')) in base


    def test_matching_power_low_roll(self):
        with patch('random.choice',return_value= 5):
            response = self.client.post('/power', data="11")
            base = list(range(600,901))
            assert int(response.data.decode('utf-8')) in base
    
    def test_not_matching_power_low_roll(self):
        with patch('random.choice',return_value= 2):
            response = self.client.post('/power', data="13")
            base = list(range(200,601))
            assert int(response.data.decode('utf-8')) in base
