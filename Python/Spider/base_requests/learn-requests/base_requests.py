#!usr/bin/python3
# -*- coding: UTF-8 -*-

# 目标站点 https://www.vmgirls.com/12985.html
"""爬虫的分类
    - 通用爬虫:
        抓取系统重要组成部分。抓取的是一整张页面。
    - 聚焦爬虫:
        是建立在爬虫基础之上。抓取的是页面中特定的局部内容。
    - 增量式爬虫:
        检测网站中数据更新的情况。只会抓取网站中最新更新出来的数据。
"""

# requests 基于网络请求的模块
#     - 指定url
#     - 发起请求
#     - 获取响应数据
#     - 持久化存储

import requests

url = "https://www.sogou.com/web"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}


def to_search():
    search = input('请输入查询内容:')
    return {
        'query': search
    }


def get_sougou(url, param, headers):
    """发起网络请求"""
    try:
        response = requests.get(url=url, params=param, headers=headers)
        print(response)
        content = response.text
        print(content)
        file_name = param.get('query') + '.html'
        with open(file_name, 'w', encoding='utf8') as f:
            f.write(content)
        print(param.get('query'), '获取数据完成！')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    search_word = to_search()
    get_sougou(url, search_word, headers)

