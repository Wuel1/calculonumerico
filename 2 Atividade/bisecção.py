import math

#Método da função
def f(x):
  return math.sqrt(9-x**2)-math.exp(x)/8

#Definição dos pontos 
a = 0
b = 1

#Precisão
erro = 0.00009
#Iterações
k = 0

#loop para procurar a raiz
while b-a>erro:
  M = (a+b)/2
  if f(a)*f(M)<0:
    b = M
  else:
    a = M
  k = k+1

print('A raiz encontrada foi de ' , (a+b)/2)
print('O número de iterações foi:', k)