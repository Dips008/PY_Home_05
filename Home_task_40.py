# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек,
# далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных,
# получить строку входных данных.
from itertools import groupby


def encode(text):
    return [(len(list(group)), key) for key, group in groupby(text)]


def decode(encode_list):
    decoded_message = ""
    i = 0
    while (i <= len(encode_list) - 1):
        decoded_message += encode_list[i][1] * encode_list[i][0]
        i += 1
    return decoded_message


def prt(e):
    str_e = ''
    for i in range(len(e)):
        str_e += str(e[i][0]) + str(e[i][1])
    return (str_e)


in_str1 = '1111122223344455'
in_str2 = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'

e1 = encode(in_str1)
e2 = encode(in_str2)

d1 = decode(e1)
d2 = decode(e2)


print(f"Original string: [ {in_str1} ]")
print(f"Encoded string: [ {prt(e1)}  ]")
print(f"Decoded string: [ {d1} ]")

print(f"Original string: [ {in_str2} ]")
print(f"Encoded string: [ {prt(e2)}  ]")
print(f"Decoded string: [ {d2} ]")
