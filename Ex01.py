#Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
#A fórmula de conversão é F ← C * 9 / 5 + 32,
#sendo F a temperatura em Fahrenheit e C a temperatura em Celsius

print('Digite uma temperatura em graus Ceusius: ')
temperatura_Ceusius = int(input())
print(type(temperatura_Ceusius))
temperatura_Fahrenheit = ((temperatura_Ceusius * 9) / 5) + 32
print(temperatura_Ceusius, 'em graus Ceusius é igual a ', temperatura_Fahrenheit,
      ' graus Fahrenheit')
