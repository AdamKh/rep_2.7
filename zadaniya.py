#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # 1
    vowels = set('AaEeIiOoYy')
    a = input('Введите строку\n')
    s = set(a.replace(' ', ''))

    # 2
    a = input('Введите строку\n')
    s1 = set(a.replace(' ', ''))
    a = input('Введите строку\n')
    s2 = set(a.replace(' ', ''))
    print(s1.intersection(s2))
