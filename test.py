import unittest
import requests
import json
import sys
import config

USER_1_USER = "user"
USER_1_PASS = "rinoceronte2"

class TestMethods(unittest.TestCase):

    def test_login(self):

        credentials = {"username": USER_1_USER, "password": USER_1_PASS}
        
        consulta = "authentication/login/"
        url = config.BASE_URL_HEROKU + config.API_BASE + consulta
        
        r = requests.post(url, credentials)
        
        print(r.status_code)
        
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
