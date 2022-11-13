# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/29 22:45
@Auth ： tanghzhengwei
@File ：shicimingju.py
@IDE ：PyCharm
"""

import requests
from bs4 import BeautifulSoup

target_url = "https://www.shicimingju.com/book/sanguoyanyi.html"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }


def request():
    """
    请求数据
    :return:
    """
    res = requests.get(url=target_url, headers=headers)
    if res.status_code == 200:
        page_text = res.content.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page_text, 'lxml')
        li_a = soup.select('.book-mulu a')
        fp = open('./三国演义.txt', 'w', encoding='utf-8')
        for a in li_a:
            # 章节名称
            title = a.string
            detail_url = "https://www.shicimingju.com/" + a['href']
            detail_response = requests.get(url=detail_url, headers=headers)
            if detail_response.status_code == 200:
                detail_text = detail_response.content.decode('utf-8', 'ignore')
                detail_soup = BeautifulSoup(detail_text, 'lxml')
                # 章节内容
                contents = detail_soup.find('div', class_='chapter_content').text

                import math
                rows = math.ceil(len(contents)/90)      # math.ceil 向上取整
                fp.write(f"章节:【{title}】" + '\n')
                for row in range(rows):
                    fp.write('    ' + contents[row*90:(row+1)*90] + '\n')      # x20 ascii 中是空格字符
                print(f'章节:【{title}】下载完成!')
                print('=======================================================')
            else:
                return '请求详情页发生错误: %', detail_response.status_code
        print('全部下载完成!')
    else:
        return '请求发生错误: %', res.status_code


if __name__ == "__main__":
    request()

