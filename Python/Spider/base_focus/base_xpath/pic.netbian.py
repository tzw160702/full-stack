# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/4 17:08
@Auth ： tanghzhengwei
@File ：pic.netbian.py
@IDE ：PyCharm
"""

# 那些妹子们
import os
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def girl_download(url):
    """
    获取房源信息
    :return:
    """
    if not os.path.exists('./picnetbian_images'):
        os.mkdir('./picnetbian_images')

    response = requests.get(url=url, headers=headers)
    print('请求状态码', response.status_code)
    if response.status_code == 200:
        response.encoding = "gbk"
        # print(response.text)
        label = etree.HTML(response.text)
        li_list = label.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            src = li.xpath('./a/img/@src')[0]
            uri = "https://pic.netbian.com" + src
            str_src = str(src)
            suffix = str_src.split('.')[-1]
            # 文件名称
            file_name = li.xpath('./a/b/text()')[0] + '.' + suffix
            image = requests.get(url=uri, headers=headers).content
            with open('./picnetbian_images/' + file_name, 'wb') as fp:
                fp.write(image)
                print(f"【图片:'{file_name}】下载成功！")
        print('=======================当前页下载完成==============================')

    else:
        print('请求页面发送错误', response.status_code)


# 取总页数
def get_page(url):
    """
    获取总页数
    :return:
    """
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        response.encoding = "gbk"
        label = etree.HTML(response.text)
        a_label = label.xpath('//div[@class="page"]/a/text()')
        pages = list()
        for a in a_label:
            try:
                a = int(a)
                if isinstance(a, int):
                    pages.append(a)
            except:
                break
        print('最大页数', max(pages))
        for page in range(1, max(pages)+1):
            if page == 1:
                next_page = "https://pic.netbian.com/4kmeinv/index.html"
            else:
                next_page = f"https://pic.netbian.com/4kmeinv/index_{page}.html"
            print('======================开始下载第%d页图片...=====================' % page)
            girl_download(next_page)


if __name__ == "__main__":
    get_page("http://pic.netbian.com/4kmeinv/")