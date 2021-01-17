import unittest
import requests
import json
import sys
import config
import bot

#Usamos los datos del usuario user, lo hemos creado para poder realizar pruebas con él.
USER_1_USER = "user"
USER_1_PASS = "rinoceronte2"
USER_1_ID = 2

#El token de los usuarios es dináico luego lo cojeremos con el primer caso de prueba.
USER_1_TOKEN = ""



class TestMethods(unittest.TestCase):

    #Es importante que se ejecute primero este test. Los test se ejecutan por orden alfabéico.
    
    def test_login(self):
        #Probamos que el usuario se puede registrar de forma correcta.
        
        credentials = {"username": USER_1_USER, "password": USER_1_PASS}
        
        consulta = "authentication/login/"

        url = config.BASE_URL_HEROKU + config.API_BASE + consulta
        
        r = requests.post(url, credentials)

        respuesta = r.json()

        global USER_1_TOKEN 

        USER_1_TOKEN = respuesta["token"]

        self.assertEqual(r.status_code, 200)
        
    def test_login_wrong(self):
        #Comprobamos que el usuario no se pueda registrar de forma correcta si introduce una contraseña erronea.
        
        credentials = {"username": USER_1_USER, "password": USER_1_PASS+"EstoNoFunciona"}
        
        consulta = "authentication/login/"

        url = config.BASE_URL_HEROKU + config.API_BASE + consulta
        
        r = requests.post(url, credentials)

        respuesta = r.json()

        global USER_1_TOKEN 
        
        try:
            USER_1_TOKEN = respuesta["token"]
        except:

        self.assertEqual(r.status_code, 400)


    def test_votings(self):
        
        #Comprobamos que podemos obtener todas las votaciones.
 
        headers = {"token": USER_1_TOKEN}

        consulta = "voting/"
        url = config.BASE_URL_HEROKU + config.API_BASE + consulta
        
        r = requests.get(url, headers = headers)
        
        self.assertEqual(r.status_code, 200)


    def test_voting(self):
        
        #Comprobamos que podemos obtener detalles de una votacion.
 
        headers = {"token": USER_1_TOKEN}

        consulta = "voting/"

        elementoAConsultar = "?id=1/"

        url = config.BASE_URL_HEROKU + config.API_BASE + consulta + elementoAConsultar
        
        r = requests.get(url, headers = headers)
        
        self.assertEqual(r.status_code, 200)
    
    def test_z_get_user(self):

        #Comprobamos que podemos obtener un ID de usuario a través de su token.
   
        data = {'token': USER_1_TOKEN}
        
        r = requests.post(config.BASE_URL_HEROKU + "authentication/getuser/", data)

        self.assertEqual(r.status_code, 200)
        
    def test_z_get_user_wrong(self):

        #Comprobamos que no podemos obtener el ID de usuario a través de su token.
        
        data = {'token': USER_1_TOKEN+"estofalla"}
        
        r = requests.post(config.BASE_URL_HEROKU + "authentication/getuser/", data)

        self.assertEqual(r.status_code, 404)

        
    def test_save_vote_data(self):

        #Comprobamos que podemos votar.
        
        data_dict = {
            "vote": { "a": 0,"b": 1},
            "voting": 1,
            "voter": 2,
            "token": USER_1_TOKEN,
        }

        headers = {"Authorization":"Token   " + USER_1_TOKEN,"Content-Type": "application/json"}
    
        r = requests.post(config.BASE_URL_HEROKU + "store/", json=data_dict, headers = headers)

        self.assertEqual(r.status_code, 200)


    def test_save_vote_w_wrong_token(self):
        
        #Comprobamos que no podemos votar.
    
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
