import unittest
import requests
import json
import sys
import config
import bot

USER_1_USER = "user"
USER_1_ID = 2
USER_1_PASS = "rinoceronte2"
USER_1_TOKEN = "6adef60924e1a9a330e99a390a47147d87e5bac6"



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

    def test_save_vote_data(self):
    
        #Opción elegída.
        a = 1

        #Opción no elegída.
        b = 0

        #Encuesta elegída
        encuesta = 1

        data_dict = {
            "vote": { "a": a,"b": b},
            "voting": 1,
            "voter": USER_1_ID,
            "token": USER_1_TOKEN,
        }

        headers = {"Authorization":"Token   " + USER_1_TOKEN,"Content-Type": "application/json"}
    
        r = requests.post(config.BASE_URL_HEROKU + "store/", json=data_dict, headers = headers)

        self.assertEqual(r.status_code, 200)


    def test_save_vote_w_wrong_data(self):
    
        #Opción elegída.
        a = 1

        #Opción no elegída.
        b = 0

        #Encuesta elegída
        encuesta = 1

        data_dict = {
            "vote": { "a": a,"b": b},
            "voting": encuesta,
            "voter": USER_1_ID,
            "token": "  1221212121212121212"
        }

        headers = {"Authorization":"Token   " + " 1221212121212121212" ,"Content-Type": "application/json"}
    
        r = requests.post(config.BASE_URL_HEROKU + "store/", json=data_dict, headers = headers)

        self.assertEqual(r.status_code, 401)

    




if __name__ == '__main__':
    unittest.main()
