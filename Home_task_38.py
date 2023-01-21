# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
str = "абвгедейка бывает  абв разная абвазная"
str_lst = list(str.split())
print(str)

out = []

# # VAR-1--------------------
# for word in str_lst:
#     if 'абв' not in word:
#         out.append(word)

# print(' '.join(out))
# # VAR-2---------------------------
# # for i in range(len(str_lst)):
# #     if str_lst[i].find("абв"):
# #         out.append(str_lst[i])

# # print(' '.join(out))

# # VAR-3------------------------
str = ' '.join(list(filter(lambda slovo: not 'абв' in slovo, str.split())))
print(str)
