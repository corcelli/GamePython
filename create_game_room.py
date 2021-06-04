import requests, json
id=str(input('ID: '))
ips=str(input('ips: '))
status=str(input('status: '))
gamename=str(input('game_name:'))
uuidgamerrom=str(input('UUID:'))
task = {"id": id, "ips": ips, "status": status,"gamename": gamename,'uuid': uuidgamerrom}
response = requests.post('http://pfsenseassec.netextreme.com.br:4000/gamerooms/', json=task)
print(response.status_code)
if response.status_code != 201:
    print('ERRO')
else:
   print('OK')

