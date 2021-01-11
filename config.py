from boto.s3.connection import S3Connection

#===Secret======

TOKEN = S3Connection(os.environ['TOKEN'], os.environ['S3_SECRET'])

#=====DECIDE-HEROKU========
BASE_URL_HEROKU = "https://decide-voting.herokuapp.com/"
API_BASE = "gateway/"

#=======LOCAL=============
API_DECIDE = 'http://localhost:8000/'

#=======HEROKU============
PORT = '5000'
HEROKU_APP_NAME = 'decide-cabina-bot-discord'
