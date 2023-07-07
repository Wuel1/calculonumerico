# Dados fornecidos
temperatura = [35, 40, 45]
c_especifico = [0.99818, 0.99828, 0.99849]

def lagrange(x, x_data, y_data):
    n = len(x_data)
    p = 0

    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x - x_data[j]) / (x_data[i] - x_data[j])
        p += y_data[i] * L

    return p

def Newton(x,y,xi):
  n = len(x)
  fdd = [[None for x in range(n)] for x in range(n)]
  yint = 0
  for i in range(n):
    fdd[i][0]= y[i]

  for j in range (1,n):
    for i in range(n-j):
      fdd[i][j]= (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])
  xterm = 1
  yint= fdd[0][0]
  for order in range(1,n):
    xterm = xterm*(xi-x[order-1])
    yint= yint + fdd[0][order]*xterm


  return  yint  

# Realizando a interpolação polinomial
while True:
    x = float(input("Digite o Valor da temperatura, para achar o valor especifico:\n"))
    lagrange_resultado = lagrange(x, temperatura, c_especifico)
    Newton_resultado = Newton(temperatura, c_especifico, x)
    print(8*"-----------")
    print("O calor específico da água a 32.5°C usando o método de Lagrange é:", lagrange_resultado)
    print(8*"-----------")
    print("O calor específico da água a 32.5°C usando o método de Newton é:", Newton_resultado)
    print(8*"-----------")
    y = int(input("Você deseja continuar?\n 1 - Sim | 2 - Não\n"))
    if(y == 1):
        continue
    else:
        break