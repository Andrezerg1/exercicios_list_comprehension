# 1 -Crie uma lista com os números pares de 1 a 10.

numeros_pares = [n for n in range(10) if n % 2 == 0]
print(numeros_pares)

# 2 -Crie uma lista com os quadrados dos números de 1 a 10.

numeros_quadrados = [n * n for n in range(10)]
print(numeros_quadrados)

# 3 -Dada uma lista de palavras, crie uma nova lista contendo o tamanho de cada palavra.

palavras = ['Maça', 'Banana', 'Uva', 'Laranja']
tamanho_palavras = [len(p) for p in palavras] 
print(tamanho_palavras)

# 4 -Dada uma lista de números, crie uma nova lista apenas com os números maiores que 5.

numeros = [1, 2, 4, 6, 9, 10]
maiores_que_cinco = [m for m in numeros if m > 5]
print(maiores_que_cinco)

# 5 -Crie uma lista com as letras maiúsculas de uma string.

string = 'AnDré'
maiusculas_string = [s for s in string if s.isupper()]
print(maiusculas_string)

#6 -Dada uma lista de números, crie uma nova lista contendo apenas os números pares e maiores que 10.

lista_numeros = [5, 10, 8, 13, 14, 18, 20, 2]
maiores_que_dez_pares = [x for x in lista_numeros if x > 10 and x % 2 == 0]
print(maiores_que_dez_pares)

# 7 -Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam com a letra "A".

nomes = ['André', 'Luiz', 'Alexandre', 'Pedro']
nomes_upper = []
for nome in nomes:
    nomes_upper.append(nome.capitalize())
iniciam_por_a = [z for z in nomes_upper if z[0] == 'A']
print(iniciam_por_a)

# 9 -Dada uma lista de números, crie uma nova lista com o dobro de cada número, mas apenas se o número for ímpar

numeros_lista = [1, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15]
dobro_numero_impar = [y*2 for y in numeros_lista if y % 2 != 0]
print(dobro_numero_impar)