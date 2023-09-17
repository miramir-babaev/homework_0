def poem(str):
    str = str.split()
    list = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

print('Введите стих =>')
str = input()
if poem(str):
    print('Парам пам-пам')
else:
    print('Пам парам')