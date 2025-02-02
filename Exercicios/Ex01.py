#Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
#A fórmula de conversão é F ← C * 9 / 5 + 32,
#sendo F a temperatura em Fahrenheit e C a temperatura em Celsius

# edit: a função input permite digitar um texto
#então nao precisa necessariamente utilizar o print

temperatura_Ceusius = float(input('Digite uma temperatura em graus Ceusius: '))
#float convertendo o input (que é uma string) para um numero ponto flutuante.

temperatura_Fahrenheit = ((temperatura_Ceusius * 9) / 5) + 32

#formatando o output no caso de a temperatura ser um inteiro, e não o float
if temperatura_Ceusius == int(temperatura_Ceusius):
      temperatura_Ceusius = int(temperatura_Ceusius)

print(temperatura_Ceusius, 'em graus Ceusius é igual a ', temperatura_Fahrenheit,
      ' graus Fahrenheit')


