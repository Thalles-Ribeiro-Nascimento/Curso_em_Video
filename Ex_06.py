def Escrever(texto):
      print('-' * 65)
      print(texto)
      print('-' * 65)


Escrever('Seja bem-vindo ao segundo desafio da aula 07 do Curso em Vídeo!!')

# Algoritmo que leia um número e apresente seu dobro, triplo e raiz quadrada
number2 = int(input('Insira um valor: '))

print(f'O número escolhido foi o {number2}\n'
      f'O dobro de {number2} é {number2 * 2}\n'
      f'O triplo de {number2} é {number2 * 3}\n'
      f'A raiz quadrada de {number2} é {number2 ** (1/2):.2f}')

Escrever('Próximo desafio!!')
