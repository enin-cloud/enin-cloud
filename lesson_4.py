#1
s = input("Введите строчку: ")
k=m=0
for i in range(len(s)):
    if s[i]=='н':
        k += 1
    else:
        m=max(m,k)
        k=0
s=s.replace('н','!')
print("Максимальное каличество <<н>> подряд: ", m,"\n Новая строчка: ", s)

#2
s = input("Введите строчку: ")
for i in range(len(s)):
    if s[i] == "{" or s[i] == "[" or s[i] == "(":
        x = i
    elif s[i] == "}" or s[i] == "]" or s[i] == ")":
        y = i
print(s[x+1:y])
s=input("Введите строчку: ").split()
for i in s:
    if i[0]=="а" and i[-1]=="я":
        print("Слова: ", i)
