"""
* Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa.
* Criar variável com o ano atual (int)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Jessica'
idade = 25
altura = 1.63
peso = 87.5
ano_atual = 2021
imc = (peso/altura**2)
ano_nascimento = ano_atual - idade

print('{} têm {} anos, {} de altura e pesa {}kg.'.format(nome, idade, altura, peso))
print('O IMC de {} é {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.'.format(nome,ano_nascimento))

