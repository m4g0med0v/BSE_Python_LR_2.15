#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант - 12
# Написать программу, которая считывает английский текст из файла и выводит его на экран,
# заменив каждую первую букву слов, начинающихся с гласной буквы, на прописную.

import sys


def capitalize_vowels(text):
    words = text.split()
    for i in range(len(words)):
        if words[i] and (words[i][0] in 'aeiouAEIOU'):
            words[i] = words[i].capitalize()
    return ' '.join(words)

def main():
    try:
        with open(sys.argv[1], 'r') as file:
            text = file.read()
            modified_text = capitalize_vowels(text)
            print(modified_text)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{sys.argv[1]}' не найден.")

if __name__ == "__main__":
    main()

    
