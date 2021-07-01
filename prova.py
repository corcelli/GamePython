NA=0
NB=0
NC=0

replicas=int(input('Quantidade de PODS: '))
print(replicas)
while True:
    if replicas == 0:
     break
    else:
     NA+=1
     replicas -= 1
     
    if replicas == 0:
     break
    else:
     NB+=1
     replicas -= 1
     
    if replicas == 0:
     break
    else:
     NC+=1
     replicas -= 1
     
print('NODE A {}'.format(NA))
print('NODE B {}'.format(NB))
print('NODE C {}'.format(NC))
