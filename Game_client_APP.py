import requests, json, psycopg2
from time import sleep
from game_loft import loft_attach
from mod_chat import msg_chat_read, msg_server_read
gameuuid='23cc8c85-8b7c-48c2-ab19-8694ba54e410'
playeruuid='c733d541-923e-4917-af50-7403a9eaa363'
id=1

msg_server_read(gameuuid)

def attach_game_to_room(uuid_gameroom: str):
    task = {"uuid_client": gameuuid, "uuid_gameroom": uuid_gameroom, "ipsrvgame": srvgamesavailable['ips'] }
    response = requests.post('http://pfsenseassec.netextreme.com.br:4000/client_attached_gameroom/', json=task)
    if response.status_code != 201:
     print('ERRO')
    else:
     print('OK')
try:    
 array = requests.get('http://pfsenseassec.netextreme.com.br:4000/gamerooms/')
except:
  print('Erro Backend #45323')
  exit()
lista = array.json()
sleep (2)
while id <= len(lista):
 response = requests.get('http://pfsenseassec.netextreme.com.br:4000/gamerooms/'+str(id))
 srvgamesavailable = response.json()
 print(srvgamesavailable['status'])
 id += 1
 if srvgamesavailable['status'] == 'OK':
  print ('ASSIGN SUCCESS')
  uuid_gameroom = srvgamesavailable['uuid']
  #gameroom_ip_attach(uuid_gameroom)
  attach_game_to_room(uuid_gameroom)
  try:
   loft_attach("'" +gameuuid+ "'","'" +playeruuid+ "'")
  except:
    print("Usuário já conectado na sala!")
  break
 else:
  print(srvgamesavailable['uuid'])
  print ('NOT ATTACHED')
  sleep (1)
  if id == len(lista)+1:
   print ('NENHUMA SALA DISPONIVEL')

