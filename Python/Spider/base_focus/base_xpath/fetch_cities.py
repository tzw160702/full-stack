# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/5 20:05
@Auth ： tanghzhengwei
@File ：fetch_cities.py
@IDE ：PyCharm
"""

import requests
from lxml import etree

url = "https://www.aqistudy.cn/historydata/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def city():
    """
    获取城市
    :return:
    """
    data = {'热门城市': None, '全部城市': dict()}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        label = etree.HTML(response.text)
        # 热门城市
        hot_city = label.xpath('//div[@class="hot"]//a/text()')
        data['热门城市'] = hot_city

        # 全部城市
        all_city = label.xpath('//div[@class="all"]//ul')
        for city in all_city:
            sort = city.xpath('./div/b/text()')[0]
            provincial_capital = city.xpath('./div/li/a/text()')
            data['全部城市'][sort] = provincial_capital

        return data

    else:
        print('请求发生错误，', response.status_code)


if __name__ == "__main__":
    result = city()
    print(result)