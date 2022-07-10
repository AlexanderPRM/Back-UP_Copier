from pprint import pprint
from system_files import more_option, write, check_tokens
from NetworkClasses import VK
from DiskClasses import YandexDisk
import json


if __name__ == '__main__':
    mark = '-'
    write(f'\nПРИВЕТСТВУЮ, ЭТО РЕЗЕРВНЫЙ КОПИРОВАЛЬЩИК.\n{mark * 30}\n')

    # Функции в файле system_files.py
    main_info = check_tokens()
    user_params = more_option()

    # Создание классов
    Me_VK = VK(main_info[0], user_params[0], user_params[2])
    Me_Yandex = YandexDisk(yandex_token=main_info[1], dir=user_params[1])

    # Работа программы
    print(mark * 30)
    write(f'Загрузка фото...\n{mark * 30}\n')
    Me_Yandex.upload_photos(Me_VK)
    print('Ваши фото:\n')
    name_photos = Me_VK.name_photo()
    pprint(name_photos, width=1, indent=2)
    with open('info_files.json', 'w') as writer:
        json.dump(name_photos, writer)
        print('\nИнформация по вашим фото записана в файл - info_files.json')
    write(f'{mark * 30}\nПрограмма сработала успешно, проверьте диск.\n')
    input('Введите ENTER для выхода: ')