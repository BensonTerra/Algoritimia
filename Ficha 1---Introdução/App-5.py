segundos=int(input("Escreva um tempo em segundos: "))
horas=segundos/3600
minutos=(segundos%3600)/60
segundos=segundos%60
print("%i Horas/%i Minutos/%i Segundos"%(horas,minutos,segundos))