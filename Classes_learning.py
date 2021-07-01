valor1=int(input())
valor2=int(input())
class Calc:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    def Soma(self):
        return self.valor1 + self.valor2
    def Multiplica(self):
        return self.valor1 * self.valor2
    def Divide(self):
        return self.valor1 / self.valor2
calcula=Calc(valor1,valor2)
print(calcula.Soma())
print(calcula.Multiplica())
print(calcula.Divide())

print('Ok {} {} {}'.format(calcula.Soma(),calcula.Multiplica(),calcula.Divide()))