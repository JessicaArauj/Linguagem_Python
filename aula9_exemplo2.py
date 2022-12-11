"""
Operadores Relacionais: retorna valor booleano, pois, realiza comparação entre duas expressões.
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente de
"""
nome = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))

'''idade_minima = 18

if idade >= idade_minima:
    print(f'{nome} pode pegar o empréstimo!'.capitalize())
else:
    print(f'{nome} não pode pegar o empréstimo!'.capitalize())'''

idade_minima = 20
idade_maxima = 30

if idade >= idade_minima  and idade <= idade_maxima:
    print(f'{nome} pode pegar o empréstimo!'.capitalize())

else:
    print(f'{nome} não pode pegar o empréstimo!'.capitalize())
    
