print('-----------------------------------------------------while')
x = 1

while x < 10:
    print(x)
    x += 5

print('-----------------------------------------------------for')
lista = [1, 2, 3, 4, 5]
listaString = ['ola', 'mundo', '!']
listaMany = [0, 'matheus', 2, 'alves', 9.8, True]

print('-----<lista>')
for i in lista:
    print(i)
print('-----</lista>')

print('-----</listaString>')
for i in listaString:
    print(i)
print('-----</listaString>')

print('-----</listaMany>')
for i in listaMany:
    print(i)
print('-----</listaMany>')

print('-----</range>')
for i in range(2):
    print(i)
print('-----</range>')