#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая сканирует заданную директорию и выводит список всех файлов и папок в этой директории,
# а также их размеры. Затем программа должна определить общий размер всех файлов в директории.

import os, sys


def get_directory_contents(directory):
    contents = []
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            contents.append((item, "File", size))
        elif os.path.isdir(full_path):
            contents.append((item, "Directory", "-"))
    return contents

def calculate_total_size(directory):
    total_size = 0
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            total_size += os.path.getsize(full_path)
    return total_size

def main():
    directory = sys.argv[1]

    if not os.path.exists(directory):
        print(f"Ошибка: Директория '{directory}' не существует.")
        return

    contents = get_directory_contents(directory)

    print("Содержимое директории:")
    print("{:<30} {:<10} {:<10}".format("Имя", "Тип", "Размер"))
    for item in contents:
        print("{:<30} {:<10} {:<10}".format(item[0], item[1], item[2]))

    total_size = calculate_total_size(directory)
    print(f"\nОбщий размер всех файлов в директории: {total_size} байт")

if __name__ == "__main__":
    main()
