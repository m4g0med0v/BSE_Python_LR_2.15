#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант - 12
# Автоматическая проверка орфографии не помешала бы многим из нас. 
# В данном упражнении мы напишем простую программу, сверяющую слова из текстового файла со словарем. 
# Неправильно написанными будем считать все слова, которых не нашлось в словаре. 
# Имя файла, в котором требуется выполнить орфографическую проверку, пользователь должен передать при помощи аргумента командной строки. 
# В случае отсутствия аргумента должна выдаваться соответствующая ошибка. 
# Сообщение об ошибке также должно появляться, если не удается открыть указанный пользователем файл. 
# Также Вам следует игнорировать регистр символов при выполнении проверки.

import sys


def load_dictionary(file_name):
    dictionary = set()
    try:
        with open(file_name, 'r', encoding='windows-1251') as file:
            for line in file:
                dictionary.add(line.strip().lower())
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")
        sys.exit(1)
    return dictionary


def spell_check(file_name, dictionary):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.strip().split()
                for word in words:
                    if word.lower() not in dictionary:
                        print(f"Ошибка в строке {line_number}: слово '{word}' не найдено в словаре.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Использование: python individual_task_2.py <имя_файла>")
        sys.exit(1)

    file_name = sys.argv[1]

    dictionary = load_dictionary("dictionary.txt")

    spell_check(file_name, dictionary)


if __name__ == "__main__":
    main()
