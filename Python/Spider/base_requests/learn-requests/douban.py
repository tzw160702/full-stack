#!usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import requests

url = "https://movie.douban.com/j/search_subjects"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

param = {
    'type': 'movie',
    'tag': '热门',
    'sort': 'recommend',
    'page_start': 0,
    'page_limit': 20
}


def douban_movie():
    response = requests.get(url=url, params=param, headers=headers)
    json_obj = response.json()
    movie_info = []
    for data in json_obj['subjects']:
        info = {'电影名称': '', '评分': '', '是否是新电影': ''}
        info['电影名称'] = data['title']
        info['评分'] = data['rate']
        info['是否是新电影'] = '新' if data['is_new'] is True else '老'
        image = requests.get(url=data['cover'], headers=headers)
        suffix = file_format(data['cover'])
        with open(f'./images/{data["title"]}.{suffix}', 'wb') as f1:
            f1.write(image.content)
        movie_info.append(info)
    return movie_info


def file_format(url):
    """
    提取文件格式
    :param url: 资源地址
    :return:
    """
    if isinstance(url, str):
        layout = url.split('/')[-1].split('.')[-1]
        return layout
    else:
        print('非法字符！')


if __name__ == "__main__":
    results = douban_movie()
    for result in results:
        with open('movie_info.txt', 'a+', encoding='utf-8') as f:
            f.write(str(result)+'\n')
    print('保存！')


