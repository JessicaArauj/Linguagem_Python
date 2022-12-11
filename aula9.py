"""
Entrada de dados - Aula 9
input - mostra na tela para usuário
input ("Qual o seu nome?")
Essa função sempre retorna dado como formato de string (str).
"""

nome = input ("Qual o seu nome?")
"""print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')"""
idade = input("Qual a sua idade?")
ano_nascimento = 2021 - int(idade)  #cast  transformei dado str em int

print()
print(f'{nome} têm {idade} anos.'
      f'{nome} nasceu em {ano_nascimento}')


