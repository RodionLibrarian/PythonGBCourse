file = open('taskone.txt', 'w', encoding='utf-8')
line = input('Enter text: ')
while line:
    file.writelines(line)
    line = input('Enter text: ')
    if not line:
        break

file.close()
file = open('taskone.txt', 'r', encoding='utf-8')
content = file.readlines()
print(content)
file.close()
