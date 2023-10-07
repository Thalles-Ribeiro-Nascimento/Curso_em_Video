def Escrever(texto):
    print('-' * 65)
    print(texto)
    print('-' * 65)


Escrever('Seja bem-vindo ao terceiro desafio da aula 07 do Curso em Vídeo!!')

# Programa que leia duas notas de um aluno e calcule sua média
note1 = float(input('Insira a primeira nota: '))
note2 = float(input('Insira a segunda nota: '))

print(f'Sua média ficou: {(note1 + note2)/2:.1f}')

Escrever("Próximo desafio!!")
