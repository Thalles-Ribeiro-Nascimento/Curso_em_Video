def Escrever(texto):
    print('-' * 65)
    print(texto)
    print('-' * 65)


Escrever('Seja bem-vindo ao sétimo desafio da aula 07 do Curso em Vídeo!!')

# Calcular a área
width = float(input('Insira a largura da parede(métros): '))
heigth = float(input('Insira a altura da parede(métros): '))

area = width * heigth
tinta = float(area /2)

print(f'Sua parede possui uma área de {area:.3f}m² e você precisará de {tinta}l de tinta!')

Escrever("Próximo desafio!!")
