nome = 'Luiz Otávio'
idade = 32  #int
altura = 1.80  #float
e_maior = idade > 18  #bool
peso = 80
imc = peso/(altura*altura)

print (nome,'têm', idade,'anos de idade e seu imc é',imc,'.')
print(f'{nome} têm {idade} anos de idade e seu imc é {imc:.2f}.')  #f-strings
print('{} têm {} anos de idade e seu imc é {:.2f}.'.format(nome, idade, imc))
