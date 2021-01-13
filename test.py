import unittest
import requests
import json
import sys
import config

USER_1_USER = "user"
USER_1_PASS = "rinoceronte2"
TOKEN = config.TOKEN

class TestMethods(unittest.TestCase):

    def test_login(self):

        credentials = {"username": USER_1_USER, "password": USER_1_PASS}
        
        consulta = "authentication/login/"
        url = config.BASE_URL_HEROKU + config.API_BASE + consulta
        
        r = requests.post(url, credentials)
        
        self.assertEqual(r.status_code, 200)


    def test_votings(self):

        
        headers = {"token": str(TOKEN)}
        consulta = "votings/"
        url = config.BASE_URL_HEROKU + config.API_BASE + consulta
        
        r = requests.get(url, headers = headers)
        
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
