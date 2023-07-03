import  numpy as np

def gauss(a,b):
    #A é a matriz dos coeficientes
    #B é o vetor de termos independentes

    n = len(b)

    for k in range(0,n-1): #percorre a diagonal
        pivo = a[k][k]

        for i in range(k+1, n): #percorre a linha
            m = a[i][k] / pivo

            for j in range (k,n): #percorre as colunas
                a[i][j] =  a[i][j] - m * a[k][j]

            b[i] = b[i] - m*b[k]
    return a,b

A = [[3,2,4],[1,1,2],[4,3,-2]]
b = [1,2,3]

def subs_reversa(A_t,b_t):
    n = len(b)
    x = n*[0] #Vetor Solução

    x[n-1] = b[n-1] / A[n-1][n-1]

    for k in range(n-2,-1,-1):
      s = 0
      for j in range(k+1,n):
        s = s +A[k][j]*x[j]


      x[k] = (b[k] - s) / A[k][k]

    return x # retorna a solução do SL A*x = b

def matriz_de_Hilbert(n):

  A = np.zeros((n,n))

  B = n*[0]

  for i in range(0,n):
    for j in range(0,n):
      A[i][j] = 1 / ((i+1) + (j+1) -1)

  for i in range(0,n):
    s = 0
    for j in range(0,n):
      s = s + A[i][j]
    B[i] = s
    
  return A, B 
  # A é a matriz de Hilbert 
  # B é o vetor de termos independentes

A, B = matriz_de_Hilbert(10)
A_t, B_t = gauss(A, B)

print(A_t)
print(20*'__')
print(B_t)
print(20*'__')

x = subs_reversa(A_t, B_t)
print(x)