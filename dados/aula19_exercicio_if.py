"""
Criar um programa que leia 2 números digitados pelo usúario;
Descobrir qual valor é o maior;
Exiba na tela qual valor é maior 

Exemplo a ser exibido no terminal: 
Digite um valor:
Digite outro valor:

primeiro_valor=3 é maior do que segundo_valor=2
"""

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual que {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}')
