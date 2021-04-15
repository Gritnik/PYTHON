prices = [57.8, 46.51, 97, 56.78, 89.76, 32.45, 12.78, 83.84, 26.89, 67.87, 34.68, 23.45, 34.6]
new_list = []
# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп

for price in prices:
    roubles = int(price)
    kop = round((price - roubles) * 100)
    new_list.append(f'{roubles} руб {kop} коп')
print(", ".join(new_list))
print(new_list)
# Вывести цены, отсортированные по возрастанию,
# новый список не создавать (доказать, что объект списка после сортировки остался
# тот же).
print(id(new_list)) #проверка айди
new_list.sort()
print(new_list)
print(id(new_list))   #проверка айди №2. совпадают!
new_list = sorted(prices, reverse = True) #сортировка наоборот, от большего к меньшему
print(sorted(new_list))
