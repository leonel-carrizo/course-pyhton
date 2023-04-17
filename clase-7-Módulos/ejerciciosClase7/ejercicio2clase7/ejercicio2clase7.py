import datetime

horaActual = datetime.datetime.now()
print('Hora de Actual:', horaActual.time().strftime('%H:%M:%S'), '\n')
# horaActual = datetime.datetime(2022, 7, 21, 19, 45, 00)
# print('Hora de Actual:', horaActual.time(),'\n')

horaSalida = datetime.datetime(2022, 7, 21, 19, 00, 00)
print('Hora de salida:', horaSalida.time())

# Si la Hora Actual es entre las 9pm y las 9am, el programa no corre
if horaActual <= datetime.datetime(2022, 7, 21, 9, 00, 00) or horaActual >= datetime.datetime(2022, 7, 21, 21, 00, 00):
    print('¡Estas fuera de horario laboral!')
# se comprueba cuanto tiepo falta para terminar la jornada
elif horaActual < horaSalida:
    tRestante = horaSalida - horaActual
    print('Todavia no puedes irte quedan:', round(
        tRestante.seconds/3600, 2), 'Horas de trabajo.')
# si la hora es mayor de las 7pm, envia a casa
else:
    print('La Jornada ha terminado. Puedes irte a casa')
