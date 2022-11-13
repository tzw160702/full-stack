#!usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import requests


class FanyiBaidu:
    URL = "https://fanyi.baidu.com/sug"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }

    def __init__(self):
        self.word = input('输入搜索词：')

        if isinstance(self.word, str):
            self.data = {
                'kw': self.word
             }
        elif not self.word :
            print('请输入搜索词，当前为空！')
            self.word = input('输入搜索词：')
        self.fetch_res()

    def fetch_res(self):
        response = requests.post(url=self.URL, data=self.data, headers=self.HEADERS)
        json_obj = response.json()
        print(json_obj)
        filename = self.word+'.json'
        fp = open(filename, 'x', encoding='utf-8')
        json.dump(json_obj, fp=fp, ensure_ascii=False)
        print('翻译完成！')


if __name__ == "__main__":
    translate = FanyiBaidu()