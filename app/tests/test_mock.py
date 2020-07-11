from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from os import getenv
from app1 import app, db

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TESTING_URI'),
            WTF_CSRF_ENABLED=False,
            DEBUG=True)
        return app
    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_power(self):
        with patch('requests.get') as w:
            w.return_value.text = "1"
            with patch('requests.post') as p:
                p.return_value.text = "11"
                response = self.client.get(url_for('home'))
                self.assertIn(b'11', response.data)

