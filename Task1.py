num = input('Введи трехзначное число: ')
res = 0
if len(num) == 3:
    for i in num:
        res += int(i)
    print(res)
else:
    print('Ты ввел не трехзначное число')
