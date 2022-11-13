# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/3 18:05
@Auth ： tanghzhengwei
@File ：58tongcheng.py
@IDE ：PyCharm
"""


# 需求：58同城二手房源信息
import requests
from lxml import etree

url = "https://xa.58.com/ershoufang/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def hosts_info():
    """
    获取房源信息
    :return:
    """
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        label = etree.HTML(response.text)
        contents = label.xpath('//a[@class="property-ex"]')
        fp = open('58二手房信息.txt', 'w', encoding='utf-8')
        for content in contents:
            # 标题
            title = content.xpath(
                './/div[@class="property-content-title"]/h3/@title')[0]
            # 户型
            house_type = ''.join(content.xpath(
                './/div[@class="property-content-info"]/p/span/text()'))
            p = content.xpath(
                './/div[@class="property-content-info"]/p/text()')
            # 面积
            areas = p[-4]
            # 楼层
            floor_number = p[-2]
            # 朝向
            orientation = p[-3]
            # 建造
            build = p[-1]

            # 楼盘
            village_name = content.xpath(
                './/p[@class="property-content-info-comm-name"]/text()')

            # 位置
            address = ''.join(content.xpath(
                './/p[@class="property-content-info-comm-address"]/span/text()'))

            price = content.xpath('.//div[@class="property-price"]/p/text()')
            # 总价
            total_prices = ''.join(content.xpath(
                './/p[@class="property-price-total"]/span/text()'))
            # 均价
            average_prices = \
            content.xpath('.//p[@class="property-price-average"]/text()')[0]
            data = f"名称: {title} - 户型: {house_type} - 面积: {areas} - 楼层: {floor_number} - 朝向: {orientation} - 建造: {build} - + 楼盘: {village_name} - 位置: {address} - 总价: {total_prices} - 均价: {average_prices}\n\n"

            fp.write(data)
            print(f'房源【{title}】信息获取完成!')

    else:
        print('请求错误', response.status_code)


if __name__ == "__main__":
    hosts_info()