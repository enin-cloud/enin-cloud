#1
import re
from re import compile
pat = compile(r"^(?P<Private>\w\d\d\d\w\w\d\d\d?)|(?P<Taxi>\w\w\d\d\d\d\d\d?)|(?P<Fail>.*)$")
def f(number):
    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', number):
        return 'Private'
    if re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', number):
        return 'Taxi'
    else:
        return 'Fail'
assert f("С227НА777") == "Private"
assert f("КУ22777") == "Taxi"
assert f("Т22В7477") == "Fail"
assert f("М227К19У9") == "Fail"

 #2
from functools import reduce
file = open('hometask8.txt', 'r', encoding = 'utf-8')
s = file.readlines()
words = reduce(lambda x,y: x[:-1]+' '+y,s).split()
print(words)
print(list(filter(lambda x: re.fullmatch(r'\b[А-Я]+[-]?[А-Я]+\b',x))))

s = 'Уважаемые! Если вы к 09:00 не вернете чемодан, то уже в 09:00:01 я за себя не отвечаю.'
s = s.split()
x = list(filter(lambda x: re.search(r'\b(0[0-9]│1[0-9]│2[0-4])[:](0[0-9]│[0-9]{2}\b', x), s))
s = reduce(lambda x,y: x+' '+y, s)
for i in x:
    s = s.replace(i,'(TBD)',1)
print(s)

s = 'Владисир устроился на работу'
x = re.findall((r'\b[А-Я][А-Я]*[А-Я]\b', s))
print(x)
