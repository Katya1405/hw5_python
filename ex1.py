# Напишите программу, удаляющую из текста все слова, содержащие а, б, в 

data = open('text.txt', 'r', encoding='utf-8')
list = data.read().split()
new_list = [i for i in list if 'а' in i or 'А'  in i or 'б' in i or 'Б' in i or 'в' in i or 'В' in i]
for i in list:
    for j in new_list:
        if j in list:
            list.remove(j)
print(list)

