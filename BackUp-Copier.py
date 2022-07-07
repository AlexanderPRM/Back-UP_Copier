
from pprint import pprint
from system_files import more_option, write
from NetworkClasses import VK
from DiskClasses import YandexDisk
import json


if __name__ == '__main__':
    mark = '-'
    # Hello Words
    write(f'\nПРИВЕТСТВУЮ, ЭТО РЕЗЕРВНЫЙ КОПИРОВАЛЬЩИК.\n{mark * 30}\n')
    # vk =
    yandex_ = ''
#     id_vk = int(input('Введите пожалуйста ID аккаунта VK: '))
#     yandex = input('''\nТеперь вам нужно будет ввести токен своего YANDEX-DISK,
# Это нужно для того чтобы мы знали куда вам отправить файл. Узнать свой токен можно тут - https://yandex.ru/dev/disk/poligon/
# Ввод: ''')
#     #user_params = [7, 'тесты', 'profile']
    user_params = more_option()
    Me_VK = VK(397101429, user_params[0], user_params[2])
    Me = YandexDisk(yandex_token=yandex_, dir=user_params[1])
    print(f'{mark * 30}\nЗагрузка фото...\n{mark * 30}')
    Me.upload_photos(Me_VK)
    print('Ваши фото:\n')
    name_photos = Me_VK.name_photo()
    pprint(name_photos, width=1, indent=2)
    with open('name_files.json', 'w') as writer:
        json.dump(name_photos, writer)
    write(f'{mark * 30}\nПрограмма сработала успешно, проверьте диск.\n')
    input('Введите ENTER для выхода: ')



