#
#
# import os
#
# path = 'C:\\Movies'
#
#
# def obxodFile(path, level=1):
#     print('level=', level, 'Content:', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path + '\\' + i):
#             print('Спускаемся', path + '\\' + i)
#             obxodFile(path + '\\' + i, level + 1)
#             print('Возвращаемся', path)
#
#
# obxodFile(path)
# def calculate_structure_sum(data_structure):
#     summa = 0
#     # Прописываем условие при помощи цикла 1 summa для key и value
#     if isinstance(data_structure, dict):
#         for key, value in data_structure.items():
#             summa += calculate_structure_sum(key)
#             summa += calculate_structure_sum(value)
#             # иначе выполняеться цикл 2 add к summa - список,кортэж,множества
#     elif isinstance(data_structure, (list, tuple, set)):
#         for item in data_structure:
#             summa += calculate_structure_sum(item)
#             # иначе выполняеться действие 3 add к summa - целое число и число с плавающей запятой
#     elif isinstance(data_structure, (int, float)):
#         summa += data_structure
#         # иначе выполняеться действие 4 add k summa - фу-цию len
#     elif isinstance(data_structure, str):
#         summa += len(data_structure)
#         # возврат из функции значения summa
#     return summa
#
# # данные взятые из условия задачи
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# # вывод результата программы
# result = calculate_structure_sum(data_structure)
# print(result)


# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Задание "Раз, два, три, четыре, пять .... Это не всё?":


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    summa = 0
    if isinstance(data_structure, (int, float)):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    return summa


result = calculate_structure_sum(data_structure)
print(result)