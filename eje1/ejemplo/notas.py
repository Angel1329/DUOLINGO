puntaje = input('ingrese la nota:')
nota = float(puntaje)

if 4.5 <= nota <=5:
    print('Aprovo con exelecia')
elif 3 <= nota < 4.5:
    print('aprovo')    
elif 0 <= nota < 3  :
    print('reprovo')
else  :
    print ('nota invalida');