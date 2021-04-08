hw_2 = [i ** 3 for i in range(1, 1001, 2)]
print(hw_2)
components = 0
first_list = []
second_list = []
for n in hw_2:
    while n != 0:
        components = components + n % 10
        n = n // 10
        first_list.append(components)
print(first_list)
for component in first_list:
    while component % 7 == 0:
        second_list.append(component)
        break
print(second_list)

print(sum(i for i in second_list))

# уверен что неверно, но не смог разобраться с циклами(








