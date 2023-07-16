# Задание 1
import requests

def main():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    heroes = requests.get(url=url + '/all.json', headers={'Content-Type': 'application/json; charset=utf-8'})
    my_heroes = ['Hulk', 'Captain America', 'Thanos']
    intelligence = {}
    for hero in heroes.json():
        if hero['name'] in my_heroes:
            intelligence[hero['name']] = hero['powerstats']['intelligence']
    intelligence_heroes = dict([max(intelligence.items(), key=lambda k_v: k_v[1])])
    print(intelligence_heroes)

main()

# Задание 2

import requests


class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")
        responce = requests.put(href, data=open(file_path, 'rb'))
        responce.raise_for_status()
        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    path_to_file = '/home/gpgr/Загрузки/tasks-math-4-11-sch-msk-20-21.pdf'
    token = ''
    uploader = YaUploader(token)
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)