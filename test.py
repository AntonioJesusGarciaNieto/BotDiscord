import unittest
import requests
import json
import sys
import config

USER_1_USER = "user"
USER_1_PASS = "rinoceronte2"
TOKEN = config.TOKEN
USER_1_TOKEN = "f016cd06e314c5f02c14f7408329067a4cd92bc0"

class TestMethods(unittest.TestCase):

    def test_login(self):

        credentials = {"username": USER_1_USER, "password": USER_1_PASS}
        
        consulta = "authentication/login/"

        url = config.BASE_URL_HEROKU + config.API_BASE + consulta
        
        r = requests.post(url, credentials)
        
        self.assertEqual(r.status_code, 200)


    def test_votings(self):
 
        headers = {"token": USER_1_TOKEN}

        consulta = "voting/"
        url = config.BASE_URL_HEROKU + config.API_BASE + consulta
        
        r = requests.get(url, headers = headers)
        
        self.assertEqual(r.status_code, 200)


    def test_voting(self):
 
        headers = {"token": USER_1_TOKEN}

        consulta = "voting/"

        elementoAConsultar = "?id=1/"

        url = config.BASE_URL_HEROKU + config.API_BASE + consulta + elementoAConsultar
        
        r = requests.get(url, headers = headers)
        
        self.assertEqual(r.status_code, 200)
    
    def test_get_user(self):

        data = {'token': USER_1_TOKEN}
        
        r = requests.post(config.BASE_URL_HEROKU + "authentication/getuser/", data)

        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
