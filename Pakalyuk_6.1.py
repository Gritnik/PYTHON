parsing_1 = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for strings in f:
        ln = strings.split()
        parsing_1.append((ln[0], ln[5], ln[6]))

print(parsing_1)

# как убрать-то " перед GET  ???(((
