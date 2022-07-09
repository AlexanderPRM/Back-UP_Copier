import requests
from pprint import pprint
from alive_progress import alive_bar
from NetworkClasses import VK
from time import sleep



class YandexDisk:
    """Класс для резервного копирования фото с соц сети на Яндекс.Диск"""

    # Инициализация
    def __init__(self, yandex_token, dir):
        self.yandex_token = yandex_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.yandex_token}'
        }
        self.dir = dir
        self.mark = '-'

    def create_dir(self, name_dir):
        """Функция создает папку на Яндекс.Диске"""

        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url, params={'path': self.dir}, headers=self.headers)
        if response.status_code in [409]:
            print(f'''Произошел незначительный конфликт, скорее всего указанная вами папка уже есть на Яндекс.Диске.
В таком случае фото будут записаны уже в существующую папку\n{self.mark * 30}''')
        elif response.status_code // 100 in [5]:
            print('Ошибка сервера.')
            print(f'Код ошибка - {response.status_code}')

        return name_dir

    def upload_photos(self, network):
        """Функция загружает фото с указанного профиля сети на Яндекс.Диск"""
        mark = '-'
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        count = -1
        headers = self.headers
        dir_name = self.create_dir(self.dir)
        if isinstance(network, VK):
            info_photos = network.name_photo()
            for url in network.url_photos():
                count += 1
                filename = info_photos[count]['filename']
                params = {'path': f'{dir_name}/{filename}', 'url': url[0]}
                response = requests.post(upload_url, headers=headers, params=params)
                if response.status_code // 100 == 5:
                    print(f'Ошибка сервера.\nПопробуйте еще раз\n{mark * 30}')
                    print(f'Ошибка - {response.status_code}')
                elif response.status_code // 100 == 4:
                    print(f'Произошла ошибка со стороны пользователя.\nПопробуйте еще раз\n{mark * 30}')
                    print(f'Ошибка - {response.status_code}')
            # Beautiful Progress Bar
            with alive_bar(len(network.url_photos()), bar='bubbles', force_tty=True) as bar:
               for i in range(len(network.url_photos())):
                  sleep(0.5)
                  bar()
        print(mark * 30)

