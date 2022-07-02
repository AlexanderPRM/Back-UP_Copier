import sys
from time import sleep


def write(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
# --------------------------
def more_option():
    mark = '-'
    params = []
    question = input('Хотите указать дополнительные параметры? ДА\НЕТ: ')
    print(mark * 30)
    while question.strip() != 'ДА' or question.strip() != 'НЕТ':
        if question.upper().strip() == 'ДА':
            count_photos = input('''\nКакое количество фото хотите загрузить?
            Можете нажать ENTER и будет выставленно значение - 5: ''')
            if count_photos == '':
                count_photos = 5
            params.append(count_photos)
            dir = input('Как назвать папку на вашем диске?: ')
            params.append(dir)
            album = input('Что будем загружать, аватарки или фото со стены? АВЫ\СТЕНА: ')
            if album.lower().strip() == 'авы':
                params.append('profile')
            elif album.lower().strip() == 'стена':
                params.append('wall')
            return params
        elif question.upper().strip() == 'НЕТ':
            count_photos = 5
            params.append(count_photos)
            dir = 'BackUp-Program'
            params.append(dir)
            album = 'profile'
            params.append(album)
            print(f'''Выставлены значения по умолчания.
            Количество фото - {count_photos}
            Наименование папки - {dir}
            Альбом загрузки - {album}''')
            return params
        else:
            print('Разработчик не реализовал другие варианты, так что следуйте инструкции :)')
            question = input('Хотите указать дополнительные параметры? ДА\НЕТ: ')
