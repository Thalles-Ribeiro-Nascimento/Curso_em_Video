# Aluguel de carro

qtde_dias = int(input('Quantos dias voce ficou com o carro? '))
km_percorridos = float(input('Quantos Km voce andou com o carro? '))
print(f'Voce ira pagar R${qtde_dias * 60 + km_percorridos * 0.15:.2f}')
