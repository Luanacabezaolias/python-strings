# LISTAS 
# Estruturas de dados (sequencia de itens)
# delimitadas por colchetes []

lista = [3, 5, 7, 8]
print(lista)

# listas são estrtuturas heterogeneas (itens de tipos diferentes)
lista = [3, 2.66, 'abc', 4, 'lu']
print(lista)

# listas são mutáveis (podem ser alteradas)
lista = [3, 5, 7, 8]
lista[0] = 100
print(lista)

# listas são acessadas pelos indices (começa sempre no indice 0)
print(lista[0])

# indices negativos começam sempre em -1 (a partir do ultimo item)
lista = [3, 5, 7, 8]
print(lista[-1])

# len - retorna o tamanho da lista 
print(len(lista))

# appende - adicona um item no final da lista 
lista.append(300)
lista.append(400)
print(lista)

# insert (indice, item) - adiciona um item em uma posiçao especifica da lista 
lista.insert(0, 99)
print(lista)

# pop() - remove o ultimo elemendo da lista 
lista = [3, 7, 5, 10]
lista.pop()
print(lista)

# pop(indice) - remove o item do indice especifico
lista = [3, 7, 5, 10]
lista.pop(1)
print(lista)

# remove - removerá somente o primeiro valor igual ao passado como parametro
lista = [3, 7, 5, 10, 5]
lista.remove(5)
print(lista)

# operdor in - verifica se um item existe na lista 
lista = [3, 7, 5, 10, 5]
if 8 in lista:
    lista.remove(8)
print(lista)

# count - conta quantas vezes um item aparece na lista 
lista = [3, 7, 5, 10, 5]
print(lista.count(5))

# index - retorna o indice de um elemento 
print(lista.index(5))

# sort - ordena uma lista (ordem crescente)
lista = [3, 7, 5, 10, 5]
lista.sort()
print(lista)

lista.sort(reverse=True) #(ordem decrescente)
print(lista)

lista = ['Lu' , 'Anny', 'Camis', 'Lety']
lista.sort()
print(lista)

# max - retorna o maior elemento da lista 
lista = [3, 7, 5, 10, 5]
print(max(lista))

# min - retorna o menor elemento da lista 
lista = [3, 7, 5, 10, 5]
print(min(lista))

# sum - retorna a soma total dos elementos (apenas listas numericas)
print(sum(lista))

# media 
media = sum(lista)/ len(lista)
print(media)

# preencher lista com itens informados pelo usuario 
lista = []
for i in range(5):
    n = int(input("Digite um número inteiro: "))
    lista.append(n)
print(lista)

lista = []
while True:
    n = int(input("Digite um número inteiro (-1 para sair): "))
    if n == -1:
        break
    lista.append(n)
print(lista)

# percorrer itens da lista
lista = [3, 7, 5, 10, 5]
cont = 0
for item in lista: # for cada item na lista...
    if item % 2 == 0:
        cont += 1
print(f'quantidade de números pares: {cont}')

# percorrer indices da lista 
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)











