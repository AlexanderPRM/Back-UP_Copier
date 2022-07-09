import requests
from pprint import pprint

class VK:
    url = 'https://api.vk.com/method/'
    token = ''''''

    def __init__(self, id, count_photos, album):
        self.params = {'access_token': self.token,
                       'owner_id': id,
                       'v': 5.131,
                       }
        self.count_photos = count_photos
        self.album = album


    def get_photos(self):
        '''Получааем фото с альбома профиля VK введенного пользователем'''
        get_photos_url = self.url + 'photos.get'
        get_photos_params = {'album_id': self.album,
                             'extended': 1,
                             'count': self.count_photos}
        response = requests.get(get_photos_url, params={**self.params, **get_photos_params})
        if response.status_code // 100 in [2, 3]:
            return response.json()
        else:
            print('Произошла ошибка.')

    # Отсеивание ссылок и размера
    def url_photos(self):
        '''Отсеиваем нужные ссылки и размер максимального размера каждого фото'''
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
        '''Создаём инфо с именем и размером каждого фото'''
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

