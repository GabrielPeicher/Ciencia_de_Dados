import numpy as np

# Exercício 1
array1 = np.array([3, 5, 9, 16, 25], dtype=float)
print(array1)

# Exercício 2
array2 = np.array([1.2, -3.6, 8.99999, 16.1], dtype=int)
print(array2)

# Exercício 3
matriz_zeros = np.zeros((3, 9))
print(matriz_zeros)

# Exercício 4
matriz_uns = np.ones((6, 7), dtype=int)
print(matriz_uns)

# Exercício 5
matriz_identidade = np.eye(4)
print(matriz_identidade)

# Exercício 6
array_aleatorio = np.random.rand(5)
print(array_aleatorio)

# Exercício 7
matriz_aleatoria = np.random.randint(0, 6, (3, 6))
print(matriz_aleatoria)

# Matriz para os exercícios 8 a 11
matriz = np.array([[4, 6, 8], [-4, 3, 2], [22, -15, 12]])

# Exercício 8
maximo = np.max(matriz)
print(maximo)

# Exercício 9
minimo = np.min(matriz)
print(minimo)

# Exercício 10
soma = np.sum(matriz)
print(soma)

# Exercício 11
media = np.mean(matriz)
print(media)

# Array para os exercícios 12 a 16
array3 = np.array([13, -2, 6, 8, 23, 15, 3, 90, 4, 10, 56, 12])

# Exercício 12
quarto_elemento = array3[3]
print(quarto_elemento)

# Exercício 13
tres_ultimos = array3[-3:]
print(tres_ultimos)

# Exercício 14
a_partir_posicao_2 = array3[2:]
print(a_partir_posicao_2)

# Exercício 15
entre_2_e_6 = array3[1:6]
print(entre_2_e_6)

# Exercício 16
array_especifico = array3[4:8]
print(array_especifico)

# Matriz para os exercícios 16 a 20
matriz2 = np.array([[1, 3, 16, -25, 14],
                    [2, 0, 10, 5, 17],
                    [19, 4, 8, 15, 13],
                    [7, 12, -5, 14, 0]])

# Exercício 17
terceira_linha = matriz2[2]
print(terceira_linha)

# Exercício 18
quarta_coluna = matriz2[:, 3]
print(quarta_coluna)

# Exercício 19
elemento_10 = matriz2[1, 2]
print(elemento_10)

# Exercício 20
submatriz = matriz2[1:3, 2:5]
print(submatriz)

# Matriz para o exercício final
matriz3 = np.array([[2, -1, 15, 24],
                    [-3, 18, 4, 25],
                    [9, 10, -13, 7]])

# Exercício final
nova_matriz = np.where(matriz3 % 2 == 0, 2, 1)
print(nova_matriz)