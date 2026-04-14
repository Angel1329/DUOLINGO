
valor = float(input('Ingrese la temperatuta'))

convercion = input('Fahrenheit (F) O Celsius (C)?: ').lower()



if convercion == 'c':
    Celsius = (valor-32)*5/9
    print (Celsius)

elif convercion == 'f':
    Fahrenheit = (valor * 1.8)+ 32
    print (Fahrenheit) 

else :
   print('datos invalidos' )    