def Escrever(texto):
    print('-' * 65)
    print(texto)
    print('-' * 65)


Escrever('Seja bem-vindo ao quarto desafio da aula 07 do Curso em Vídeo!!')
# Programa que leia um valor em metros e o exiba em centímetro e milímetros!
value = float(input('Insira um valor: '))

print(f'{value}m passando para quilômetros fica {value / 1000}km\n'
      f'{value}m passando para centímetros fica {value * 100}cm\n'
      f'{value}m passando para milímetros fica {value * 1000}mm')

Escrever("Próximo desafio!!")
