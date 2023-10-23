def Escrever(texto):
      print('-' * 65)
      print(texto)
      print('-' * 65)


Escrever("Seja bem-vindo ao último desafio da aula 07 do Curso em Vídeo!!")
# Aumento de salário
sal = float(input('Insira seu salário: R$ '))
aum = sal + (sal * 15/100)


print(f'Seu salário de R$ {sal:.2f} recebeu um aumento de 15%\n'
      f'Seu novo salário é de R$ {aum:.2f}')

Escrever('Muito obrigado!')
