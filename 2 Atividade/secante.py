import math

#função 
def f(x):
  return math.sqrt(9-x**2)-math.exp(x)/8

#aproximações inicial
x0 = 0
x1 = 3

#erro
erro = 0.00009

#contagem das iterações
k = 0

#iterações
while abs (f(x1))>erro:
  if abs(x0-x1)<erro:
    break
  x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
  x0 = x1
  x1 = x2
  k += 1

print("-----------SECANTE-------------")
print("A solução encontrada foi:", x1)
print("O número de iterações foi:", k)