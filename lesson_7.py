#1
def read_last(lines, file):
    if lines > 0:
        with open(file, encoding="utf-8") as text:
            file_str = text.readlines()[-lines:]
        for line in file_str:
            print(line.strip())
    else:
        print('Введено неверное количество строк')
read_last(2, 'article.txt')

import os
def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f' В папке {catalog[0]} содержится:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
print_docs('C:/Program Files/JetBrains')

#2
def longest_words(file):
    with open(file, encoding="utf-8") as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
    return sought_words
print(longest_words('article.txt'))

name = input("Введите имя файла: ")
with open(f'{name}.txt', 'w') as file:
    file.write('\n'.join(iter(input, '')))
