import sys
from time import sleep
import os



def write(text):
    """Функция создаёт эффект печатания букв"""
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


def more_option():
    """Функция спрашивает у пользователя о дополнительных настройках программы"""

    mark = '-'
    params = []
    question = input('Хотите указать дополнительные параметры? ДА\НЕТ: ').upper().strip()
    print(mark * 30)
    while question.strip() != 'ДА' or question.strip() != 'НЕТ':
        if question == 'ДА':
            count_photos = input('''Какое количество фото хотите загрузить?
        Можете нажать ENTER и будет выставленно значение - 5: ''')
            if count_photos == '':
                count_photos = 5
            params.append(count_photos)
            dir = input('\nКак назвать папку на вашем диске?: ')
            params.append(dir)
            album = input('\nЧто будем загружать, аватарки или фото со стены? АВЫ\СТЕНА: ').lower().strip()
            # Проверка правильного ввода альбома
            while album not in ['авы', 'стена']:
                print(mark * 30)
                write('Пожалуйста, введите АВЫ или СТЕНА.\nЕсть еще альбом с сохраненными фото, он будет добавлен в будущем\n')
                album = input('\nЧто будем загружать, аватарки или фото со стены? АВЫ\СТЕНА: ').lower().strip()
            else:
                if album == 'авы':
                    params.append('profile')
                elif album == 'стена':
                    params.append('wall')
            return params
        elif question == 'НЕТ':
            count_photos = 5
            params.append(count_photos)
            dir = 'BackUp-Program'
            params.append(dir)
            album = 'profile'
            params.append(album)
            print(f'''Выставлены значения по умолчанию.
            Количество фото - {count_photos}
            Наименование папки - {dir}
            Альбом загрузки - {album}''')
            return params
        else:
            print('Разработчик не реализовал другие варианты, так что следуйте инструкции :)')
            question = input('Хотите указать дополнительные параметры? ДА\НЕТ: ').upper().strip()



def check_tokens():
    """
    Функция проверяет наличие ID Профиля ВК и токена Яндекс.Диск в файлах папки Tokens.
    Если они отсутствуют, происходит запись введенных данных в файлы.

    Если файл пустой, то os.stat().st_size == 0 будет возвращать True
    """

    tokens = []
    mark = '-'

    # Проверка ID ВК в файле Tokens/VK_ID.txt
    if os.stat("Tokens/VK_ID.txt").st_size == 0:
        id_vk = input('Введите пожалуйста ID аккаунта VK: ').strip()
        while not id_vk.isdigit():
            print('ID VK должен быть числом, пожалуйста введите еще раз.')
            print(mark * 30)
            id_vk = input('Введите пожалуйста ID аккаунта VK: ')
        else:
            with open('Tokens/VK_ID.txt', 'w') as vk:
                vk.write(id_vk)
            tokens.append(id_vk)
            print(mark * 30)
    else:
        with open('Tokens/VK_ID.txt', 'r') as token:
            reader = token.read()
            print(f'Ваш ID профиля VK сохраненный в файле "Tokens/VK_ID.txt"\n:{reader}:\n')
        question = input('Оставляем введённый ID VK? ДА/НЕТ: ').lower().strip()
        while question != 'да' or question != 'нет':
            if question == 'да':
                with open('Tokens/VK_ID.txt', 'r') as token:
                    reader = token.read()
                    tokens.append(reader)
                print(mark * 30)
                break
            elif question == 'нет':
                id_vk = input('Введите новый ID - ')
                while not id_vk.isdigit():
                    print('ID VK должен быть числом, пожалуйста введите еще раз.')
                    print(mark * 30)
                    id_vk = input('Введите пожалуйста ID аккаунта VK: ')
                else:
                    with open('Tokens/VK_ID.txt', 'w') as vk:
                        vk.write(id_vk)
                        tokens.append(id_vk)
                break
            else:
                print('\nПожалуйста, ответьте снова.')
                question = input('Оставляем введённый ID VK? ДА/НЕТ: ').lower().strip()

    # Проверка токена Яндекс.Диск в файле Tokens/Yandex_Token.txt
    if os.stat("Tokens/Yandex_Token.txt").st_size == 0:
        yandex_token = input(f'''Введите пожалуйста свой токен Яндекс.Диска
----Узнать его можно по этой ссылке - "https://yandex.ru/dev/disk/poligon/" 
----Ввод: ''', )

        with open('Tokens/Yandex_Token.txt', 'w') as yandex:
            yandex.write(yandex_token)
            tokens.append(yandex_token)
    else:
        with open('Tokens/Yandex_Token.txt', 'r') as token:
            reader = token.read()
            print(f'Ваш токен сохраненный в файле "Tokens/Yandex_Token.txt"\n:{reader}:\n')

        question = input(f'Оставляем введённый вами токен Яндекс.Диска? ДА/НЕТ: ').lower().strip()
        while question != 'да' or question != 'нет':
            if question == 'да':
                with open('Tokens/Yandex_Token.txt') as token:
                    reader = token.read()
                    tokens.append(reader)
                print(mark * 30)
                break
            elif question == 'нет':
                yandex_token = input('Введите новый токен - ')
                with open('Tokens/Yandex_Token.txt', 'w') as yandex:
                    yandex.write(yandex_token)
                    tokens.append(yandex_token)
                print(mark * 40)
                break
            else:
                print('Пожалуйста, ответьте снова.')
                question = input('Оставляем введённый токен Яндекс.Диска? ДА/НЕТ: ').lower().strip()
    print('\n' * 20)




    return tokens

