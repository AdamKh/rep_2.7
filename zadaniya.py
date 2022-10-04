#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # 1
    str_in = input("Введите строку: ").lower()
    a = set(str_in.replace(' ', ''))
    vowels = set("aeiouyаоуыэеёиюяи")
    count = 0
    for i in str_in:
        if i in vowels:
            count += 1
    print('Количество глассных в предложении = ', count)

    # 2
    a = input('Введите строку\n')
    s1 = set(a.replace(' ', ''))
    a = input('Введите строку\n')
    s2 = set(a.replace(' ', ''))
    print('Количество общих символов = ', s1.intersection(s2))
