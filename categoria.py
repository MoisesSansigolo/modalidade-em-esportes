from datetime import date
atual = date.today().year
nascimento = int(input('Qual é o ano de nascimento do atlete: '))
idade = atual - nascimento
print('O atleta tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('O atleta é MIRIM')
elif idade <= 14:
    print('O atleta é INFANTIL')
elif idade <= 19:
    print('O atleta é JUNIOR')
elif idade <= 25:
    print('O atleta é SÊNIOR')
else:
    print('O atleta é MASTER')