def Escrever(texto):
      print('-' * 65)
      print(texto)
      print('-' * 65)


# Algoritmo que ler um número e dê o seu Sucessor e o seu Antecessor
Escrever("Seja bem-vindo ao primeiro desafio da aula 07 do Curso em Vídeo!!")

number = int(input('Insira um número: '))

print(f'Seu sucessor é {number + 1}\n'
      f'Seu antecessor é {number - 1}')

Escrever('Próximo desafio!')
