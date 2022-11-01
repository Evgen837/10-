# -*- coding: utf-8 -*-

# # Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем
# # Обернуть код и обработать исключительные ситуации для произвольных входных параметров
# # - ValueError - невозможно преобразовать к числу
# # - IndexError - выход за границы списка
# # - остальные исключения
# # для каждого типа исключений написать на консоль соотв. сообщение
#
#
# BRUCE_WILLIS = 42
# input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
# try:
#     leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * leeloo
#     print(f"- Leeloo Dallas! Multi-pass № {result}!")
# except ValueError:
#     print(f'введенное значение {input_data} невозможно преобразовать к числу')
# except IndexError:
#     print(f'введенное значение {input_data} выходит за границы списка: должно быть минимум 4 цифры')
# except Exception:
#     print(f'Закралась очередная ошибка!')


# # День сурка
# #
# # Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# # и может выкидывать исключения:
# # - IamGodError
# # - DrunkError
# # - CarCrashError
# # - GluttonyError
# # - DepressionError
# # - SuicideError
# # Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
# #
# # Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# # кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# # При создании собственных исключений максимально использовать функциональность
# # базовых встроенных исключений.
#
# import random
#
#
# ENLIGHTENMENT_CARMA_LEVEL = 777
#
# class IamGodError(Exception):
#     pass
#
# class DrunkError(Exception):
#     pass
#
# class CarCrashError(Exception):
#     pass
#
# class GluttonyError(Exception):
#     pass
#
# class DepressionError(Exception):
#     pass
#
# class SuicideError(Exception):
#     pass
#
# def one_day():
#     choise = random.randint(1, 13)
#     if choise == 13:
#         groundhog_action = [
#             IamGodError('почувствовал себя богом. Это неправильный выбор. Попробуй-ка снова'),
#             DrunkError('решил выпить весь алкоголь. Эта миссия невыполнима. Пробуй еще'),
#             CarCrashError('решил обогнать ракету? Ну-ну... '),
#             GluttonyError('правда захотел всё это съесть? Надо еще что-нибудь придумать.'),
#             DepressionError('что-то пригрустнул. Держись и крепись.'),
#             SuicideError('так просто не соскочишь! Давай еще!')
#         ]
#         raise random.choice(groundhog_action)
#     else:
#         karma_day_level = random.randint(1, 7)
#     return karma_day_level
#
# karma_level = 0
# groundhog_day = 0
#
# with open(file='groundhog_log.log', mode='w', encoding='utf8') as log_file:
#     while karma_level < ENLIGHTENMENT_CARMA_LEVEL:
#         groundhog_day += 1
#         try:
#             karma_level += one_day()
#         except IamGodError as exc:
#             log_file.write(f'На {groundhog_day}-й день ты... {exc} \n')
#         except GluttonyError as exc:
#             log_file.write(f'На {groundhog_day}-й день ты... {exc} \n')
#         except DrunkError as exc:
#             log_file.write(f'На {groundhog_day}-й день ты... {exc} \n')
#         except CarCrashError as exc:
#             log_file.write(f'На {groundhog_day}-й день ты... {exc} \n')
#         except DepressionError as exc:
#             log_file.write(f'На {groundhog_day}-й день ты... {exc} \n')
#         except SuicideError as exc:
#             log_file.write(f'На {groundhog_day}-й день ты... {exc} \n')


# # Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# # Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# # Например:
# # Василий test@test.ru 27
# #
# # Надо проверить данные из файла, для каждой строки:
# # - присутсвуют все три поля
# # - поле имени содержит только буквы
# # - поле емейл содержит @ и .
# # - поле возраст является числом от 10 до 99
# #
# # В результате проверки нужно сформировать два файла
# # - registrations_good.log для правильных данных, записывать строки как есть
# # - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
# #
# # Для валидации строки данных написать метод, который может выкидывать исключения:
# # - НЕ присутсвуют все три поля: ValueError
# # - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# # - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# # - поле возраст НЕ является числом от 10 до 99: ValueError
# # Вызов метода обернуть в try-except.
#
#
bad_items = 0
good_items = 0


def writing_in_bad_log(bad_items, line, message):
    if bad_items == 0:
        mode = 'w'
    else:
        mode = 'a'
    with open(file='registrations_bad.log', mode=mode, encoding='utf8') as file_for_bad_enter:
        file_for_bad_enter.write(f'{message} в строке {line}')
    bad_items += 1
    return bad_items


with open(file='registrations.txt', mode='r', encoding='utf8') as entered_file:
    for line in entered_file:
        try:
            name, email, age = line.split(' ')
            if not name.isalpha():
                writing_in_bad_log(bad_items=bad_items, line=line, message='поле имени содержит НЕ только буквы')
            elif ('@' not in email) or ('.' not in email):
                writing_in_bad_log(bad_items=bad_items, line=line, message='поле емейл НЕ содержит @ и .(точку)')
                bad_items += 1
            elif int(age) > 99 or int(age) < 10:
                writing_in_bad_log(bad_items=bad_items, line=line,
                                   message='поле возраст НЕ является числом от 10 до 99')
            else:
                if good_items == 0:
                    mode = 'w'
                else:
                    mode = 'a'
                with open(file='registrations_good.log', mode=mode, encoding='utf8') as file_for_enter:
                    file_for_enter.write(line)
                good_items += 1


        except ValueError:
            if bad_items == 0:
                mode = 'w'
            else:
                mode = 'a'
            with open(file='registrations_bad.log', mode=mode, encoding='utf8') as file_for_bad_enter:
                file_for_bad_enter.write(f'НЕ присутсвуют все три поля в строке {line}')
            bad_items += 1
