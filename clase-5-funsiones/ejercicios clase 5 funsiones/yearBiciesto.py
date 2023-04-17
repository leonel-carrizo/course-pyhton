year = 2024

def yearBiciesto(year):
    if year % 4 == 0:
        return True
    else:
        return False

esBiciesto = yearBiciesto(year)
if esBiciesto == True:
    print('El año ' + str(year) + ' es Biciesto'+'\n')
else:
    print('El año ' + str(year) + ' NO es Biciesto'+'\n')
