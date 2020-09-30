list = [109, 234, 532, 32, 43, 12, 54, 54, 23, 12]
new_list = [fnum for fnum, snum in zip(list[1:], list[:-1]) if fnum > snum]

print(f'Исходный список {list}')
print(f'Новый список {new_list}')