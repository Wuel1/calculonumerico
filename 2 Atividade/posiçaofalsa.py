import math

#método da função
def f(x):
  return math.sqrt(9-x**2)-math.exp(x)/8

#definição dos pontos 
a = 0
b = 3

#precisão
erro = 0.00009
#iterações
k = 0

M = (a*f(b)-b*f(a))/(f(b)-f(a))

#loop para procurar a raiz
while abs(f(M))>erro:
  M = (a*f(b)-b*f(a))/(f(b)-f(a))
  if f(a)*f(M)<0:
    b = M
  else:
    a = M
  k = k+1

print('A raiz encontrada foi de' , M)
print('O número de iterações foi:', k)