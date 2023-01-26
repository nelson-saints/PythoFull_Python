#Receba uma temperatura em farenheit e exiba em graus celsius.

farenheit = float(input('Digite a temperatura em Farenheit: '))
celsius = ((farenheit - 32) * 5) /9

print(f'Essa temperatura em graus celsius é: {celsius}°')
