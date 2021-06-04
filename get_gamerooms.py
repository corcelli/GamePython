import requests
import json
from time import sleep
print('UID UNICO DO GAME')
gamename=str(input('GAME_UID: '))
#request=('http://pfsenseassec.netextreme.com.br:4000/gamerooms/?id='+id)
#response = requests.get(request)
response = requests.get('http://pfsenseassec.netextreme.com.br:4000/gamerooms/?gamename='+gamename)
#print(response)
#if response:
#  print('Request is successful.')
#else:
#  print('Request returned an error.')
listaips = json.loads(response.text.strip('[]'))
print(listaips)
print (listaips['gamename'])
#print('UID_GAME: {}'.format(gamename))
