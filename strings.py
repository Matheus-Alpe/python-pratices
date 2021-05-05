a = "Matheus"
b = "Alves"

concatena = a + " " + b

print(a)
print(b)
print(concatena)

#len é uma função que pega o tamanho da string
print('"'+ a + '"', 'contem', len(a), 'caracteres')

#pega o indice da letra na string
print(a[0])
#pega o so um pedaço da string
print(a[0:3])
print(a[1:])

for letra in a:
    print(letra)

#metodo lowercase no python
x = "UPPERCASE PARA LOWER"
print(x.lower())

y = "lowercase para upper"
print(y.upper())

#metodo remove espaços e caracteres espciais no final da string
z = '         oi \n'
print(z.strip())

#metodo converte uma string para lista
t = 'matheus alves pereira'
print(t.split())
print(t.split('a'))

#metodo busca de substring
u = 'alce pulando de um predio mt alto'
print(u.find('predio'))

#metodo replace
print(u.replace('alce', 'viado'))