"""Tipos primitivos"""
# 1° int = Inteiro (ex: 1; 2; 5499;...)
# 2° float = Real(Ponto flutuante) (ex: 1.5; 35.3; 125.55;...)
# 3° str = String (ex: "Olá"; "Thalles"; "54";...)
# 4° bool = Booleanos (ex: True; False)

name = str(input('Digite seu nome: '))
number1 = int(input('Digite um número: '))
number2 = float(input('Digite mais um número: '))
soma = number1 + number2
print(f'{name}, a soma entre eles é\n{soma}')
