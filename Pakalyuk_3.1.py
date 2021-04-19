def num_translate(trans):
    numbers = {
                'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять',
                'zero': 'ноль'}
    return numbers.get(trans)


print(num_translate('one').title())