задание 1
x, y = input().split()
if not x.isdigit() or not y.isdigit():
    print('Вводи числа')
else:
    x, y = map(int, (x, y))
    if y == 0:
      print('Деление на ноль')
    else:
      print(x/y)

задание 2
print("Введите стоимость товара")
b=20
k=0.35
x = input()
if not x.isdigit():
  print("Деньги давай")
else:
  x = int(x)
  if x > b:
    print(round(x-x*k, 2))
    print(round(x*k, 2))
  else:
    print(x)

задание 3
print("введи число месяца")
x = input()
if not x.isdigit():
  print("это не число")
else:
  x = int(x)
  if 0<x<13:
    if x == 12 or x == 1 or x==2:
      if x==12: print("зима, декабрь")
      if x==1: print("зима, январь")
      if x==2: print("зима, февраль")
    elif x==3 or x==4 or x==5:
      if x==3: print("весна, март")
      if x==4: print("весна, апрель")
      if x==5: print("весна, май")
    elif x==6 or x==7 or x==9:
      if x==6: print("лето, июнь")
      if x==7: print("лето, июль")
      if x==8: print("лето, август")
    elif x==9 or x==10 or x==11:
      if x==9: print("осень, сентябрь")
      if x==10: print("осень, октябрь")
      if x==11: print("осень, ноябрь")
  else:
    print("нет такого месяца")
