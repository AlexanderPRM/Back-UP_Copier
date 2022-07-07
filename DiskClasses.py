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

    # Создание папки
    def create_dir(self, name_dir):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url, params={'path': self.dir}, headers=self.headers)
        return name_dir

    # Загрузка фото
    def upload_photos(self, network):
        mark = '-'
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        count = -1
        dir_name = self.create_dir(self.dir)
        if isinstance(network, VK):
            info_photos = network.name_photo()
            for url in network.url_photos():
                count += 1
                filename = info_photos[count]['filename']
                params = {'path': f'{dir_name}/{filename}', 'url': url[0]}
                response1 = requests.post(upload_url, headers=self.headers, params=params).json()
            # progress bar
            with alive_bar(len(network.url_photos()), bar='bubbles', force_tty=True) as bar:
               for i in range(len(network.url_photos())):
                  sleep(0.5)
                  bar()
        print(mark * 30)