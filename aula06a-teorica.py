"""3 Tipos de print abaixo"""
# 1° print('A soma entre', n1 'e', n2 'vale', s) = Python2
# 2° print('A soma entre {} e {} vale {}'.format(n1, n2 , s))
# 3° print(f'A soma entre {n1} e {n2} vale {s}')
"""A 3° forma é a minha preferida!!!"""

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale {s}')
