n = int(input('Введи число:'))
m = int(input('Введи еще одно число:'))
k = int(input('И еще одно:'))   
if k <= m*n and (k%m==0 or k%n==0):
    print('Да')
else:
    print('Нет')