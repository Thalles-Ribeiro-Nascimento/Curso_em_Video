# Fazer um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ela!

thing = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(thing)}\nSó tem espaços? {thing.isspace()}\nÉ um número? {thing.isnumeric()}\n'
      f'É alfabético? {thing.isalpha()}\nÉ alfanumérico? {thing.isalnum()}\nEstá em maiúscula? {thing.isupper()}\n'
      f'Está em minúscula? {thing.islower()}\nEstá capitalizada? {thing.istitle()}\n'
      f'Fim!')
