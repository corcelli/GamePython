import requests, json 
from time import sleep

id=1
def gameroom_ip_attach(gameroom_ip : str):
 print(gameroom_ip)
array = requests.get('http://pfsenseassec.netextreme.com.br:4000/gamerooms/')
lista = json.loads(array.text)
sleep (2)
while id <= len(lista):
 response = requests.get('http://pfsenseassec.netextreme.com.br:4000/gamerooms/'+str(id))
 srvgamesavailable = json.loads(response.text)
 print(srvgamesavailable['status'])
 id += 1
 if srvgamesavailable['status'] == 'OK':
  print ('ASSIGN SUCCESS')
  ip = srvgamesavailable['ips']
  gameroom_ip_attach(ip)
  break
 else:
  print(srvgamesavailable['ips'])
  print ('NOT ATTACHED')
  sleep (1)
  if id == len(lista):
   print ('NENHUMA SALA DISPONIVEL')

