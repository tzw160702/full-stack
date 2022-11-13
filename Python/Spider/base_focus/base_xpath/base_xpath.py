# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/2 23:56
@Auth ： tanghzhengwei
@File ：base_xpath.py
@IDE ：PyCharm
"""
"""
xpath进行数据解析：(最常用且最便捷高效的一种解析方式。通用性。)

    - xpath解析原理：
        - 1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
        - 2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。
    - 环境的安装：
        - pip install lxml
    - 如何实例化一个etree对象:from lxml import etree
        - 1.将本地的html文档中的源码数据加载到etree对象中：
            etree.parse(filePath)
        - 2.可以将从互联网上获取的源码数据加载到该对象中
            etree.HTML('page_text')
        - xpath('xpath表达式')
    - xpath表达式:
        - /:表示的是从根节点开始定位。表示的是一个层级。
        - //:表示的是多个层级。可以表示从任意位置开始定位。
        - 属性定位：//div[@class='song'] tag[@attrName="attrValue"]
        - 索引定位：//div[@class="song"]/p[3] 索引是从1开始的。
        - 取文本：
            - /text() 获取的是标签中直系的文本内容
            - //text() 标签中非直系的文本内容（所有的文本内容）
        - 取属性：
            /@attrName     --> <img src="xxxxxx" />

"""

import requests
from lxml import etree


url = "http://www.baoxiaobaike.com/"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }


if __name__ == "__main__":
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        label = etree.HTML(response.text)        # etree.tostring方法可以自动修正HTML文本, 结果是bytes类型

        # 【 /】从根节点开始寻找
        # print(label.xpath('/html/body/div/div/div'))

        # 【 //】从任意位置开始寻找
        # print(label.xpath('//div/div/div'))

        # 【tag[@attrName="attrValue"]】通过属性定位
        # print(label.xpath('//div[@class="title"]/a'))

        # 【tag[index]】通过索引定位
        # print(label.xpath('//div[@class="col1"]/div[2]/div[2]/a/'))

        # 【/text()】获取直系标签文本内容
        # print(label.xpath('//div[@id="qiushi_tag_65388"]/div[@class="content"]/a/p[2]/text()'))

        # 【//text()】 获取标签下所有文本内容
        # print(label.xpath('//div[@id="qiushi_tag_65388"]/div[@class="content"]/a//text()'))

        # 【/@attrName]】 获取标签属性值
        # print(label.xpath('//div[@class="content"]/a/@href')[0])




