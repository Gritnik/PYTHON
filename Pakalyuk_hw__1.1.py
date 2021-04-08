duration = 400153
month = (duration // 2629743)
days = (duration // 86400 ) % 30   # dозьму среднее значение дней
hours = (duration // 3600) % 24
minuts = (duration // 60) % 60
seconds = duration % 60
if duration <= 3599 and duration >= 0:
    print(duration, 'это: ', minuts, 'm ', seconds, 's')
elif duration >= 3600 and duration < 86400:
    print(duration, 'это:', hours, 'h', minuts, 'm', seconds, 's')
elif duration >= 86400 and duration < 604800:
    print(duration, 'это:', days,'d', hours, 'h', minuts, 'm', seconds, 's')
elif duration >= 604800:
    print(duration, 'это:', month, 'month',  days, 'd', hours, 'h', minuts, 'm', seconds, 's')
else:
    print('Ну снова накосячил, ай молодец!')