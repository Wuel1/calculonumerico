import math

#função original
def f(x):
    return math.sqrt(9-x**2)-math.exp(x)/8

def f_linha(x):
    return (-x/math.sqrt(9-x**2))-math.exp(x)/8

#função de iteração
def phi(x):
    return x - (f(x) / f_linha(x))

#aproximação inicial
x_k = 2

#erro
erro = 0.00009

#contagem das iterações
k = 0

#iterações
while abs(f(x_k))>=erro:
    x_k = phi(x_k)
    k += 1

print("-----------NEWTON-------------")
print("A solução encontrada foi:", x_k)
print("O número de iterações foi:", k)