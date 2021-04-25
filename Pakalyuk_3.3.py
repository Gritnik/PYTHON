def thesaurus(*args):
    names = dict()
    for name in args:
        first_simbol = name[0]
        if first_simbol not in names:
            names[first_simbol] = []
            print(names)
        names[first_simbol].append(name)
    return names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

