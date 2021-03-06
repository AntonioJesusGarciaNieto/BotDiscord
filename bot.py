import discord
from discord.ext import commands
import asyncio
import requests
from requests.auth import HTTPBasicAuth
import json
import config as c

TOKEN = c.TOKEN

intents = discord.Intents.default()
intents.members = True

description = ""
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

DIC = {}


'''
##############################
# Funcionalidades            #
##############################
'''

@bot.command()
async def iniVotacion(ctx):

    ''' Permite iniciar el proceso de votación de forma amena. '''

    a = ctx.author

    await a.create_dm()
    await a.dm_channel.send('Hello, if you want to start the voting process you must log in with the command !loginAsUser followed by your username and password. For example, !loginAsUser Firulais PassWord')

@bot.command()
async def info(ctx):

    ''' Da al usuario una lista con un resumen de todos los comandos disponibles. '''

    a = ctx.author
    await a.create_dm()
    await a.dm_channel.send("Si necesitas ayuda has llamado al comando adecuado :). Te paso una chuleta con todos los comandos: \n"+
                                        " \t- !loginAsUser -> Te permite logearte, introduce el comando seguido de tu nombre de usuario y contraseña en decide \n"+
                                        " \t- !clean -> Borra todos los mensajes, solo en canales de texto \n"+
                                        " \t- !votings -> Te permite ver las votaciones disponibles para un usuario logeado. \n"
                                        " \t- !voting -> Te permite obtener detalles concretos de una votación, solo para un usuario logeado. Escribe !voting espacio y el ID de la votación. \n"
                                        " \t- !vote -> Permite realizar una votación. Escribe !vote espacio el id de la votación y la opción elegida. \n"
                                        " \t- !iniVotacion -> Permite iniciar el proceso de votación de forma amena. \n" )

@bot.command()
async def loginAsUser(ctx,user: str,clave: str):

    ''' Te permite logearte.
            Inputs: user (nombre de usuario)
                    clave (contraseña en decide). '''

    a = ctx.author

    consulta = "authentication/login/"
    url = c.BASE_URL_HEROKU + c.API_BASE + consulta

    auth = {
        "username": str(user),
        "password": str(clave)
    }

    response = requests.post(url,auth)
    
    data = response.json()

    token = data["token"]

    
    if(response.status_code==200):
        cadena = "Te has logeado genial, ya puedes votar !!! :). Mira las votaciones disponibles con el comando !votings"
    else:
        cadena = "Hay un fallo, lo siento mi pana :( . Pide ayuda al administrador"
                             
    

    DIC[str(a)] = token

    await a.create_dm()
    await a.dm_channel.send(cadena)

@bot.command()
async def votings(ctx):

    ''' Te permite ver las votaciones disponibles para un usuario logeado. '''
    

    a = ctx.author
    token = DIC[str(a)]

    headers = {"token": str(token)}

    consulta = "voting/"

    url = c.BASE_URL_HEROKU + c.API_BASE + consulta

    response = requests.get(url, headers = headers)

    response = json.loads(response.text)

    diccionarioVotaciones  = parseVotings(response)
    
    a = ctx.author

    DIC[str(a)] = token

    num_opt = len(diccionarioVotaciones)

    listaCadenas=[]
    for element in diccionarioVotaciones:
        cadena = "ID-> "+ str(element.get("id")) + " .El título es: "+str(element.get("name"))+" y su descripción es: "+ str(element.get("question").get("desc"))
        listaCadenas.append(cadena)

    cadena = "Hay "+str(num_opt)+" encuestas.Te paso info sobre ellas. Recuerda que puedes acceder a ellas en detalle con el comando !voting espacio y el id"

    for cad in listaCadenas:
        cadena = cadena + "\n"+cad
    
    await a.create_dm()
    await a.dm_channel.send(cadena)    

@bot.command()
async def voting(ctx,option: int):

    ''' Te permite obtener detalles concretos de una votación, solo para un usuario logeado.
            Inputs: option (ID de la votación). '''

    consulta = "voting/?id="

    
    url_base = c.BASE_URL_HEROKU + c.API_BASE
    url = url_base + consulta+str(option)

    a = ctx.author

    token = DIC[str(a)]

    headers = {"token": str(token)}

    response = requests.get(url, headers = headers)

    r = json.loads(response.text)
    r = r[option-1]

    v = {'id': r['id'], 'name': r['name'], 'desc': r['desc'], 'end_date': r['end_date'],'start_date': r['start_date'], 'question': r['question'], 'pub_key': r['pub_key']}
    options = v["question"].get("options")

    opt1 = options[0]
    opt2 = options[1]

    await a.create_dm()
    await a.dm_channel.send("Nombre de la votación "+ str(v["name"])+ ", ID = "+str(v["id"])+". Como opciones tienes :\n" + "Opción "+ str(opt1.get("number"))+" equivale a "+str(opt1.get("option"))+ "\nOpción "+ str(opt2.get("number"))+" equivale a "+str(opt2.get("option")))
    await a.dm_channel.send("Recuerda: !vote -> Permite realizar una votación. Escribe !vote espacio el id de la votación y la opción elegida.")

@bot.command()
async def vote(ctx,encuesta: int,respuesta: int):

    ''' Te permite realizar una votación, solo para un usuario logeado.
            Inputs: encuesta (ID de la encuesta).
                    respuesta (ID de la respuesta). '''

    auth = ctx.author

    token = DIC[str(auth)]
    token = str(token)



    user = get_user(token)
    user = json.loads(user.text)
    user_id= user['id']

    a,b = 0,0
    if respuesta == 1:
        a = 1
    elif respuesta == 2:
        b = 1
    else:
        print("En este proyecto no se tendrán en cuenta votaciones con más de dos opciones")


    data_dict = {
        "vote": { "a": a,"b":b},
        "voting": encuesta,
        "voter": user_id,
        "token": token
    }

    r = save_vote_data(data_dict,token)

    await auth.create_dm()
    await auth.dm_channel.send("Todo ha salido genial :)")

@bot.command()
async def clean(ctx):

    ''' Te permite limpiar todos los mensajes de un canal.'''

    channel = ctx.channel
    await asyncio.sleep(3)
    await channel.purge()

'''
##############################
# on_ready                   #
##############################
'''

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
 

'''
##############################
# Métodos de utilidad        #
##############################
'''

def get_user(token):

    ''' Te permite obtener un usuario a través de su token.
            Inputs: token (token del usuario). '''

    data = {'token': token}
    r = requests.post(c.BASE_URL_HEROKU + "authentication/getuser/", data)

    return r

def save_vote_data(data_dict,token):

    ''' Te permite guardar el voto del usuario.
            Inputs: token (token del usuario).
                    data_dict (voto en formato json). '''
    
    headers = {"Authorization": "Token " + token,
                "Content-Type": "application/json"}
    
    r = requests.post(c.BASE_URL_HEROKU + "store/", json=data_dict, headers = headers)

    print(r.status_code)
    return r


def parseVotings(response):

    ''' Te permite parsear votaciones.
            Inputs: response (respuesta). '''

    res = []
    for r in response:
        v = {'id': r['id'], 'name': r['name'], 'desc': r['desc'], 'end_date': r['end_date'],
             'start_date': r['start_date'], 'question': r['question'], 'pub_key': r['pub_key']}

        if v['start_date'] is not None and v['end_date'] is None:
            res.append(v)

    return res

'''
##############################
# Main                       #
##############################
'''

if __name__ == "__main__":
    bot.run(TOKEN)

