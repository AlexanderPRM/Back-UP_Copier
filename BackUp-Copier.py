import requests
from pprint import pprint
from time import sleep
from alive_progress import alive_bar
from system_files import more_option, write

class CopyPhotoToYandex:
    """Класс для резервного копирования фото с соц сети на облако"""
    url = 'https://api.vk.com/method/'
    with open('vk_token.txt', 'r') as file:
        vk_token = file.read().strip()

    # Инициализация
    def __init__(self, id, yandex_token, count_photos, dir, album):
        self.params = {'access_token': self.vk_token,
                       'owner_id': id,
                       'v': 5.131,
                       }
        self.yandex_token = yandex_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.yandex_token}'
        }
        self.dir = dir
        self.count_photos = count_photos
        self.album = album


    # Получение фото с профиля
    def get_photos(self):
        get_photos_url = self.url + 'photos.get'
        get_photos_params = {'album_id': self.album,
                            'extended': 1,
                             'count': self.count_photos}
        response = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()
        return response

    # Отсеивание ссылок и размера
    def url_photos(self):
        photos = self.get_photos()['response']['items']
        info_all_photos = []
        for post in photos:
            list_info_photos = []
            max_height = 0
            max_width = 0
            # pprint(post)
            sizes_photo = post['sizes']
            # pprint(len(sizes_photo))
            counter = 0
            flag = True
            for size in sizes_photo:
                if size['height'] >= max_height and size['width'] >= max_width:
                    max_height = size['height']
                    max_width = size['width']
            for size in sizes_photo:
                counter += 1
                if (size['height'] == max_height and size['width'] == max_width) and size['height'] != 0:
                    list_info_photos.append(size['url'])
                    list_info_photos.append(size['type'])
                    flag = False
                    break
                elif flag and counter == len(sizes_photo):
                    list_info_photos.append(sizes_photo[-1]['url'])
                    list_info_photos.append(sizes_photo[-1]['type'])

            info_all_photos.append(list_info_photos)
        return info_all_photos

    # Наименование фото и размер фото
    def name_photo(self):
        photos = self.get_photos()['response']['items']
        list_photos = []
        count = -1

        for photo in photos:

            photo_info = {}
            count += 1
            flag = True
            photo_name = str(photo['likes']['count']) + '.jpg'
            if count != 0:
                for file_info in list_photos:
                        if file_info['filename'] == photo_name:
                            photo_info['filename'] = photo_name + f' \ndate - {photo["date"]}'
                            flag = False
                        if flag:
                            photo_info['filename'] = photo_name
            else:
                photo_info['filename'] = photo_name
            photo_info['size'] = self.url_photos()[count][1]
            list_photos.append(photo_info)
        return list_photos

    # Создание папки
    def create_dir(self, name_dir):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url, params={'path': name_dir}, headers=self.headers)
        return name_dir

    # Загрузка фото
    def upload_photos(self):
        mark = '-'
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        count = -1
        dir_name = self.create_dir(self.dir)
        info_photos = self.name_photo()
        for url in self.url_photos():
            count += 1
            filename = info_photos[count]['filename']
            params = {'path': f'{dir_name}/{filename}', 'url': url[0]}
            response1 = requests.post(upload_url, headers=self.headers, params=params).json()
        # progress bar
        with alive_bar(len(self.url_photos()), bar='bubbles', force_tty=True) as bar:
           for i in range(len(self.url_photos())):
              sleep(0.5)
              bar()
        print(mark * 30)

if __name__ == '__main__':
    mark = '-'
    # Hello Words
    write(f'\nПРИВЕТСТВУЮ, ЭТО РЕЗЕРВНЫЙ КОПИРОВАЛЬЩИК.\n{mark * 30}\n')
    # vk =
    # yandex_ =
    id_vk = int(input('Введите пожалуйста ID аккаунта VK: '))
    yandex = input('''\nТеперь вам нужно будет ввести токен своего YANDEX-DISK,
Это нужно для того чтобы мы знали куда вам отправить файл. Узнать свой токен можно тут - https://yandex.ru/dev/disk/poligon/
Ввод: ''')
    #user_params = [7, 'тесты', 'profile']
    user_params = more_option()
    Me = CopyPhotoToYandex(id=id_vk, yandex_token=yandex,
                           count_photos=user_params[0], dir=user_params[1], album=user_params[2])
    print(f'{mark * 30}\nЗагрузка фото...\n{mark * 30}')
    Me.upload_photos()
    print('Ваши фото:\n')
    pprint(Me.name_photo(), width=1, indent=2)
    write(f'{mark * 30}\nПрограмма сработала успешно, проверьте диск.\n')
    input('Введите ENTER для выхода: ')



