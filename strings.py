# STRINGS
# SEQUENCIA DE CARACTERES

texto = 'Exemplo de texto'
a = texto[0]
print(a)
a = texto[-1]  # -1 ultima letra
print(a)

for c in texto:
    print(c)


# tamanho da string
print(len(texto))

# opeador in (busca)
if 'x' in texto:
    print('x existe na string')

if 'texto' in texto:
    print('texto existe na string')

# upper (converte para maiusculo)
print(texto.upper())

# lower (converte para minusculo)
print(texto.lower())

# title (iniciais de cada palavra em maiuscula)
print(texto.title())

#capitalize (coloca a inicial em maiuscula)
print(texto.capitalize())

# strip lstrip rstrip
texto = '    exemplo de texto    '
print(texto.strip())  # strip (remove os espaços em branco do inicio e do final)
print(texto.lstrip())  # lstrip (remove os espaços em branco do inicio)
print(texto.rstrip())  # rstrip (remove os espaços em branco do final)


# count (conta a quantidade de vezes que o caracter aparece na string)
texto = 'exemplo de texto'
print(texto.count('e'))

# replace (substitui uma string por outra)
texto = 'banana, laranja, maçã'
texto = texto.replace('laranja', 'melancia')
print(texto)

# split (divide uma string de acordo um separador)
texto = 'banana, laranja, maçã'
frutas = texto.split(',') # retorna lista
print(frutas)












