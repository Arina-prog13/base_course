a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
if b==0:
    print('математику учи')
elif a//b==0:
    print('частное', a//b)
    print('делится')
elif a%b!=0:
    print('остаток', a%b)
else:
    print('не делится')