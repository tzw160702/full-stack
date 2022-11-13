# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/5 21:07
@Auth ： tanghzhengwei
@File ：resume.py
@IDE ：PyCharm
"""

import os
import requests
from lxml import etree

# 站长免费简历
url = "https://sc.chinaz.com/jianli/free.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def download_resume():
    """
    下载简历
    :return:
    """
    if not os.path.exists('./resume'):
        os.mkdir('./resume')

    response = requests.get(url=url, headers=headers)
    if response.status_code:
        label = etree.HTML(response.text)
        all_p = label.xpath('//div[@id="container"]/div/p')
        for p in all_p:
            link = "https:" + p.xpath('./a/@href')[0]

            # 文件名称
            name = p.xpath('./a/text()')[0]
            name = name.encode('iso-8859-1').decode('utf-8')

            detail_response = requests.get(url=link, headers=headers)
            if detail_response.status_code == 200:
                detail_label = etree.HTML(detail_response.text)
                download_link = detail_label.xpath('//ul[@class="clearfix"]/li/a/@href')[0]
                contents = requests.get(url=download_link, headers=headers).content

                # 文件类型
                file_type = download_link.split('.')[-1]
                with open('./resume/' + name + '.' + file_type, 'wb') as fp:
                    fp.write(contents)
                    print(f'简历【{name}】 下载完成！！！')
            else:
                print('请求详情页发生错误，', detail_response.status_code)
        print('------------------------当前页简历模板下完完成-------------------')
    else:
        print('请求发生错误，', response.status_code)


if __name__ == "__main__":
    download_resume()