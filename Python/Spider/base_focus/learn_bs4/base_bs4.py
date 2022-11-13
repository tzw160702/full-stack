"""
bs4进行数据解析
    - 数据解析的原理：
        - 1.标签定位
        - 2.提取标签、标签属性中存储的数据值
    - bs4数据解析的原理：
        - 1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
        - 2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    - 环境安装：
        - pip install bs4
        - pip install lxml
    - 如何实例化BeautifulSoup对象：
        - from bs4 import BeautifulSoup
        - 对象的实例化：
            - 1.将本地的html文档中的数据加载到该对象中
                    fp = open('./test.html','r',encoding='utf-8')
                    soup = BeautifulSoup(fp,'lxml')
            - 2.将互联网上获取的页面源码加载到该对象中(常用)
                    page_text = response.text
                    soup = BeatifulSoup(page_text,'lxml')
        - 提供的用于数据解析的方法和属性：
            - soup.tagName:返回的是文档中第一次出现的tagName对应的标签
            - soup.find():
                - find('tagName'):等同于soup.div
                - 属性定位：
                    -soup.find('div',class_/id/attr='song')
            - soup.find_all('tagName'):返回符合要求的所有标签（列表）
        - select：
            - select('某种选择器（id，class，标签...选择器）'),返回的是一个列表。
            - 层级选择器：
                - soup.select('.tang > ul > li > a')：>表示的是一个层级
                - soup.select('.tang > ul a')：空格表示的多个层级
        - 获取标签之间的文本数据：
            - soup.a.text/string/get_text()
            - text/get_text():可以获取某一个标签中所有的文本内容
            - string：只可以获取该标签下面直系的文本内容
        - 获取标签中属性值：
            - soup.a['href']
"""

from bs4 import BeautifulSoup

if __name__ == "__main__":
    f = open('./qiushibaike.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(f, 'lxml')

    # 获取<a>标签
    # 1.【通过BeautifulSoup 对象.标签名去获取】
    # print(soup.a)    # 获取的是html中 <a> 标签第一次出现的结果
    # 2.【通过BeautifulSoup 对象.find()方法去获取】
    # print(soup.find('a'))    # 和 soup.a 作用一样
    # 3.【find()可以加上标签属性定位】
    # print(soup.find('a', id="download_h5_link"))
    # 4.【通过BeautifulSoup 对象.findall()方法去获取】
    # print(len(soup.find_all('a')))  # 获取的是html中所有的 <a> 标签结果, 同样findall()方法也可以属性定位
    # print(soup.find_all('div', id="wrap"))

    # Select 层级选择器
    # 1.不跨级别
    # print(soup.select('#h5_footer > p > span'))     # 使用 > 区分层级
    # 2. 跨级别
    # print(soup.select('#h5_footer span'))  # 使用 空格 区分层级

    # 获取直系标签文本内容
    # print(soup.span.string)
    # 获取标签中所有文本内容
    # print(soup.find('div', id="pc_footer").text)
    # print(soup.find('div', id="pc_footer").get_text())

    # 获取标签中属性值
    # print(soup.link['href'])




