nome = input('Insira seu nome:')
salario = float(input('Insira o valor do seu Salario:'))
bonus = float(input('Insira o valor do Bonus:'))
calculo = 1000 + salario * bonus
print(f"Olá {nome}, o seu bônus foi de R$ {calculo:.2f}")


