#Escreva um programa que leia uma temperatura em º Celsius e imprima o equivalente em º Fahrenheit
tempCelsius = float(input("Indique uma temperatura em celsius: "))
tempFarenheit = 1.8 * tempCelsius + 32
print("%f °C equivale a %f F "%(tempCelsius,tempFarenheit))