#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    c = input('c = ')
    m = input('m = ')
    n = input('n = ')
    o = input('o = ')
    q = input('q = ')
    d = input('d = ')
    w = input('w = ')
    p = input('p = ')

    mn_a = {c, m, n, o, q}
    mn_b = {c, d, m, w}
    mn_c = {m, n, q}
    mn_d = {c, m, p}
    mn_u = mn_a.union(mn_b.union(mn_c.union(mn_d)))
    print('Множество A = ', mn_a)
    print('Множество B = ', mn_b)
    print('Множество C = ', mn_c)
    print('Множество D = ', mn_d)

    mn_x = mn_c.intersection(mn_a.union(mn_b))
    print('\nМножество X = ', mn_x)

    mn_y = mn_a.intersection(mn_u.difference(mn_b))\
        .union(mn_c.difference(mn_d))
    print('Множество Y = ', mn_y)
