import os
import ProxyCloud

BOT_TOKEN = '5620117342:AAGZ0cTnmVuW9GQPW6UVxSQ9ZaE0QiB1W2w' #Aqui va el token del bot
API_ID = 15745491 #Tu api id de telegram
API_HASH = '2618ec2cdeb1b513eabf02f83f5a1553' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','overlordox').split(';')

static_proxy = 'http://KDDHKIYEJEJGGIYFJEGDIEYEKIKGFFRJHHCDHICJ'
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['overlordox'] = 0

