"""
Para números flutuante, podemos usar essa fórmula {<variável>:.(1,2,3,...)f} para diminuir o tamanho do valor que
aparece no console.

* Ex: print(f'A divisão da {d:.2f}
d:.2f com "d" sendo a variável.
"""

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+ n2
m = n1* n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma vale {s}, o produto é {m} e a divisão da {d:.2f}\n'
      f'A divisão inteira da {di} e a potencia da {e}')
