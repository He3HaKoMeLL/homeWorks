text = ('Килограмм асфильта')
print('Килограмм асфильта')
print('1)Слого на обород:', text[::-1])
g = input()
print('2)Пердпоследняя символ:', g[-2])
print('3)Первые 5 символов:', g[:4])
print('4)вся строка кроме последней 2 символ:', g[:-2])
print('5)Вывод четных индексов:', g[1::2])
print('6)Вывод нечетных индексов:', g[0::2])
print('7)Вывод всех символов в обратном порядке индексов:', g[::-1])
print('8)Вывод символов в обратном порядке индексов через 1:', g[::-2])
print('9)Вывод длины строки:', len(g))
text = g.split(' ')
r=text[1]
z=text[0]
print('10)Вывод меняем слова местами:',r,z)