import os

TEMP = '__template__.tex'

def cpy_to(dst, src, *lines):
    dst = open(dst, 'w', encoding='utf8')
    src = open(src, 'r', encoding='utf8')

    for s in src:
        if s.rstrip() == '%':
            for i in lines:
                dst.write(i)
                print(i, end='')
        else:
            dst.write(s)

qfile = iter(open('q.txt', encoding='utf8'))
for i in range(1, 46):
    q = next(qfile)[4:]
    cpy_to('%02d.tex' % i, TEMP, '\\qtitle{%02d}\n' % i, q, '\n')
