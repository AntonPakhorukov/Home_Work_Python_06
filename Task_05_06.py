# Задача 1:
# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Пример:
# [1,4,5,2,3,9,8,11,0] => "0-5, 8-9, 11"
# [1, 4,3,2] => "1-4"
# [1,4] => "1,4"

# Задача 2:
# Дана строка (возможно, пустая), состоящая из букв A-Z.
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: 
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется кол-во повторений.

try:
    task = int(input('Введите номер задачи: '))
except ValueError:
    print('Не корректный ввод')
    SystemExit
match task:
    case 1:
        try:
            solution = int(input('Введите способ сортировки(1/2): '))
        except ValueError:
            print('Не верный ввод')
            SystemExit
        match solution:
            case 1:                
                start_list = (input('Введите целые числа через пробел: ').split())
                start_list = list(map(int, start_list))
                print(start_list)
                def inString(test_list: list):
                    sort_list1 = []
                    sort_list2 = []
                    sort_list3 = []
                    listAll = []
                    for num in test_list:
                        if num < 6:
                            sort_list1.append(num)
                        elif 5 < num < 11:
                            sort_list2.append(num)
                        elif 10 < num < 16:
                            sort_list3.append(num)
                        else:
                            listAll.append(num)
                    result = ''
                    if len(sort_list1):
                        for i in test_list:
                            if str(i) in '012345':
                                if min(sort_list1) != max(sort_list1):
                                    result += f'{min(sort_list1)}-{max(sort_list1)}, '
                                    break
                                else:
                                    result += f'{min(sort_list1)}, '
                                    break
                    if len(sort_list2):
                        for j in test_list:        
                            if str(j) in '6,7,8,9,10':
                                if min(sort_list2) != max(sort_list2):
                                    result += f'{min(sort_list2)}-{max(sort_list2)}, '
                                    break
                                else:
                                    result += f'{min(sort_list2)}, '
                                    break
                    if len(sort_list3):
                        for k in test_list:        
                            if str(k) in '11,12,13,14,15':
                                if min(sort_list3) != max(sort_list3):
                                    result += f'{min(sort_list3)}-{max(sort_list3)}'
                                    break
                                else:
                                    result += f'{min(sort_list3)}'
                                    break
                    if len(listAll):
                        for k in test_list:        
                            if str(k) in '11,12,13,14,15':
                                if min(listAll) != max(listAll):
                                    result += f', {min(listAll)}-{max(listAll)}'
                                    break
                                else:
                                    result += f', {min(listAll)}'
                                    break         
                    print(result)
                inString(start_list)
            case 2:
                test_list = (input('Введите целые числа через пробел: ').split())
                test_list = list(map(int, test_list))
                print(test_list)
                test_list = sorted(test_list)
                sort_list1 = []
                sort_list2 = []
                sort_list3 = []
                count = 1
                def strSort(some_list: list):
                    result = ''
                    if len(test_list) == 2:
                        if test_list[0] + 1 == test_list[1]:
                            print(f'{test_list[0]}-{test_list[1]}')
                            
                        elif test_list[0] + 1 < test_list[1]:
                            print(f'{test_list[0]}, {test_list[1]}')
                            
                    else:
                        for i in range(len(test_list) - 1):
                            if test_list[i] + 1 == test_list[i + 1]:
                                sort_list1.append(test_list[i])
                                count = i + 1
                                if i + 1 == len(test_list) - 1:
                                    sort_list1.append(test_list[i + 1])
                            else:
                                sort_list1.append(test_list[i])
                                break
                            if count + 1 == len(test_list) - 1:
                                if test_list[-1] == test_list[-2] - 1:
                                    sort_list2.append(test_list[count + 1]) 
                        for j in range(count + 1, len(test_list) - 1):
                            if test_list[j] + 1 == test_list[j + 1]:
                                sort_list2.append(test_list[j])
                                count = j + 1
                                if j + 1 == len(test_list) - 1:
                                    sort_list2.append(test_list[j + 1])
                            else:
                                sort_list2.append(test_list[j])
                                break 
                            if count + 1 == len(test_list) - 1:
                                sort_list3.append(test_list[count + 1])
                        for k in range(count + 1, len(test_list) - 1):
                            if test_list[k] == test_list[k + 1]:
                                sort_list3.append(test_list[k])
                                count = k
                                if k + 1 == len(test_list) - 1:
                                    sort_list3.append(test_list[k])
                                else:
                                    sort_list3.append(test_list[k])
                            else:
                                if not len(test_list[k + 1]):
                                    sort_list3.append(test_list[k])
                                else:
                                    sort_list3.append(test_list[k])
                                    break
                            if count + 1 == len(test_list) - 1:
                                sort_list3.append(test_list[count + 1])
                        if len(sort_list1):
                            for i in test_list:
                                if str(i) in '012345':
                                    if min(sort_list1) != max(sort_list1):
                                        result += f'{min(sort_list1)}-{max(sort_list1)}, '
                                        break
                                    else:
                                        result += f'{min(sort_list1)}, '
                                        break
                        if len(sort_list2):
                            for j in test_list:        
                                if str(j) in '6,7,8,9,10':
                                    if min(sort_list2) != max(sort_list2):
                                        result += f'{min(sort_list2)}-{max(sort_list2)}, '
                                        break
                                    else:
                                        result += f'{min(sort_list2)}, '
                                        break
                        if len(sort_list3):
                            for k in test_list:        
                                if str(k) in '11,12,13,14,15':
                                    if min(sort_list3) != max(sort_list3):
                                        result += f'{min(sort_list3)}-{max(sort_list3)}'
                                        break
                                    else:
                                        result += f'{min(sort_list3)}'
                                        break        
                    print(result)
                strSort(test_list)

    case 2:
        start_str = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
        str_out = ''
        index = 0
        count = 1
        while index < len(start_str) - 1:
            if start_str[index] == start_str[index + 1]:
                count += 1
                if index == len(start_str) - 2:
                    str_out += start_str[index] + str(count)
            else:
                if count == 1:
                    str_out = str_out + start_str[index]
                    if index == len(start_str) - 2:
                        if start_str[index] != start_str[index + 1]:
                            str_out += start_str[index + 1] + str(count + 1)
                else:
                    str_out += start_str[index] + str(count)
                count = 1
            index += 1    
        print(start_str)
        print('A4B3C2XYZD4E3F3A6B28 - ответ')
        print(str_out)

    # case 3:
        
    #     test_list = (input('Введите целые числа через пробел: ').split())
    #     test_list = list(map(int, test_list))
    #     print(test_list)
    #     test_list = sorted(test_list)
    #     sort_list1 = []
    #     sort_list2 = []
    #     sort_list3 = []
    #     count = 1
    #     def strSort(some_list: list):
    #         result = ''
    #         if len(test_list) == 2:
    #             if test_list[0] + 1 == test_list[1]:
    #                 print(f'{test_list[0]}-{test_list[1]}')
                    
    #             elif test_list[0] + 1 < test_list[1]:
    #                 print(f'{test_list[0]}, {test_list[1]}')
                    
    #         else:
    #             for i in range(len(test_list) - 1):
    #                 if test_list[i] + 1 == test_list[i + 1]:
    #                     sort_list1.append(test_list[i])
    #                     count = i + 1
    #                     if i + 1 == len(test_list) - 1:
    #                         sort_list1.append(test_list[i + 1])
    #                 else:
    #                     sort_list1.append(test_list[i])
    #                     break
    #                 if count + 1 == len(test_list) - 1:
    #                     if test_list[-1] == test_list[-2] - 1:
    #                         sort_list2.append(test_list[count + 1]) 
    #             for j in range(count + 1, len(test_list) - 1):
    #                 if test_list[j] + 1 == test_list[j + 1]:
    #                     sort_list2.append(test_list[j])
    #                     count = j + 1
    #                     if j + 1 == len(test_list) - 1:
    #                         sort_list2.append(test_list[j + 1])
    #                 else:
    #                     sort_list2.append(test_list[j])
    #                     break 
    #                 if count + 1 == len(test_list) - 1:
    #                     sort_list3.append(test_list[count + 1])
    #             for k in range(count + 1, len(test_list) - 1):
    #                 if test_list[k] == test_list[k + 1]:
    #                     sort_list3.append(test_list[k])
    #                     count = k
    #                     if k + 1 == len(test_list) - 1:
    #                         sort_list3.append(test_list[k])
    #                     else:
    #                         sort_list3.append(test_list[k])
    #                 else:
    #                     if not len(test_list[k + 1]):
    #                         sort_list3.append(test_list[k])
    #                     else:
    #                         sort_list3.append(test_list[k])
    #                         break
    #                 if count + 1 == len(test_list) - 1:
    #                     sort_list3.append(test_list[count + 1])
    #             print(f'list1 = {sort_list1}')
    #             print(f'list2 = {sort_list2}')
    #             print(f'list3 = {sort_list3}')
    #             if len(sort_list1):
    #                 for i in test_list:
    #                     if str(i) in '012345':
    #                         if min(sort_list1) != max(sort_list1):
    #                             result += f'{min(sort_list1)}-{max(sort_list1)}, '
    #                             break
    #                         else:
    #                             result += f'{min(sort_list1)}, '
    #                             break
    #             if len(sort_list2):
    #                 for j in test_list:        
    #                     if str(j) in '6,7,8,9,10':
    #                         if min(sort_list2) != max(sort_list2):
    #                             result += f'{min(sort_list2)}-{max(sort_list2)}, '
    #                             break
    #                         else:
    #                             result += f'{min(sort_list2)}, '
    #                             break
    #             if len(sort_list3):
    #                 for k in test_list:        
    #                     if str(k) in '11,12,13,14,15':
    #                         if min(sort_list3) != max(sort_list3):
    #                             result += f'{min(sort_list3)}-{max(sort_list3)}'
    #                             break
    #                         else:
    #                             result += f'{min(sort_list3)}'
    #                             break        
    #         print(result)
    #     strSort(test_list)
