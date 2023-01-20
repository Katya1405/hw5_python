# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

some_string = input()
times = 1
for i in range(len(some_string)-1):
    if i <= len(some_string)-1:
        if some_string[i] == some_string[i + 1]:
            times += 1
        else:
            print(times, some_string[i], sep='', end='')
            times = 1
print(times, some_string[i+1], sep='')
