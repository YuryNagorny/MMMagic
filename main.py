import vkapi
import vk
import time
from urllib.request import urlretrieve
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic, QtWidgets
import sys


class Authorize_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vk_app.ui', self)
        self.pushButton.clicked.connect(self.authorize)

    def authorize(self):
        global vk_token
        self.client_id = self.lineEdit.text()
        self.redirect_uri = f'https://vk.com/editapp?id={self.client_id}'
        session = f'https://oauth.vk.com/authorize?client_id={self.client_id}&display=page&redirect_uri={self.redirect_uri}&scope=notifications,friends&response_type=code&v=5.131'
        self.lineEdit_2.setText(session)
        self.vk_code = self.lineEdit_3.text()
        self.service_key = self.lineEdit_4.text()
        self.pushButton_2.clicked.connect(self.final)

    def final(self):
        self.client_id = self.lineEdit.text()
        self.redirect_uri = f'https://vk.com/editapp?id={self.client_id}'
        self.vk_code = self.lineEdit_3.text()
        self.service_key = self.lineEdit_4.text()
        print(self.client_id, self.redirect_uri, self.vk_code, self.service_key)
        self.session_2 = f'https://oauth.vk.com/access_token?client_id={self.client_id}&client_secret={self.service_key}&redirect_uri={self.redirect_uri}&code={self.vk_code}'
        self.lineEdit_5.setText(self.session_2)


class Main_menu(QWidget):


vk_token = None
client_id = None


def download_photo_album(path, token, owner_id, album_id):
    vkapi = vk.API(token)
    photos = vkapi.photos.get(owner_id=owner_id, album_id=album_id, count=1000, v=5.131, photo_sizes=1) # получаем список фото
    number_photo = 0
    for photo in photos['items']: # проходимся по фото
        max_size_photo = photo['sizes']
        max_size_photo.sort(key=lambda x: 'height') # берем фото с самым высоким разрешением
        f = open(f'{path[:]}\\album_{number_photo}.jpg', 'w') # создаем файл
        url = max_size_photo[-1]['url'] # получаем запрос изображения
        urlretrieve(url, f"{path[:]}\\album_{number_photo}.jpg") # скачиваем фото
        number_photo += 1
        f.close()


def delete_banned_friends():
    friends_list = vkapi.friends.get(v=5.81, fields='last_seen')
    for i in friends_list['items']:
        if 'deactivated' in i:
            vkapi.friends.delete(user_id=i['id'], v=5.81)
            time.sleep(0.25)


def delete_afk_friends():
    friends_list = vkapi.friends.get(v=5.81, fields='last_seen')
    for i in friends_list['items']:
        if 'last_seen' in i:
            if time.time() - i['last_seen']['time'] >= 31536000:
                vkapi.friends.delete(i['id'])
                time.sleep(0.25)


def download_wall_photo(path, owner_id, start, end):
    photos_count = end - start
    number_photo = 0
    photos = vkapi.photos.get(owner_id=owner_id, v=5.131, album_id='wall', offset=start, count=photos_count)['items'][::-1]
    for photo in photos:
        max_size_photo = photo['sizes']
        max_size_photo.sort(key=lambda x: 'height')
        f = open(f'{path[:]}\\wall_{number_photo}.jpg', 'w')
        url = max_size_photo[-1]['url']
        urlretrieve(url, f"{path[:]}\\wall_{number_photo}.jpg")
        number_photo += 1
        f.close()


def delete_afk_groups(owner_id):
    for i in vkapi.groups.get(owner_id=owner_id, v=5.81)['items']:
        checker = (vkapi.wall.get(owner_id=-i, v=5.81, count=2))
        time.sleep(0.25)
        if time.time() - checker['items'][0]['date'] >= 31536000 and time.time() - checker['items'][1]['date'] >= 31536000:
            vkapi.groups.leave(owner_id=checker['items'][0]['from_id'])


def del_notifications():
    vkapi.notifications.markAsViewed(v=5.81)


def set_status(text):
    vkapi.status.set(text=text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Authorize_Window()
    main_window.show()
    vk_token = 'vk1.a.uWldt5nQXFm4zCl1wOe6ITag4pwvKfpoOpboLILOocRBc4eai_AvkVmVZKoSIz679PP3U5JPqh4qWcph0YFyRCthn_qPc_260VLHey3npGdT9VKBc6VDHZz_NXxysuj8KIfsRkk65AbTXntlMnAwwgr_3jL2hP-TD3ZodEXEgMiWyy_MdnfzAQotvxC5zXeZ'
    vkapi = vk.API(vk_token)
    del_notifications()
    sys.exit(app.exec_())
