import math

#função original
def f(x):
    return math.sqrt(9-x**2)-math.exp(x)/8

#função de iteração
def phi(x):
    #math.sqrt(-math.exp(2*x)/64 + 9)
    #math.log(8) + math.log(3-x)
    return math.sqrt(-math.exp(2*x)/64 + 9)

#aproximação inicial
x_k = 1

#erro
erro = 0.00009

#contagem das iterações
k = 0

#iterações
while abs(f(x_k))>erro:
    x_k = phi(x_k)
    k += 1

print("-----------PONTO FIXO-------------")
print("A solução encontrada foi:", x_k)
print("O número de iterações foi:", k)