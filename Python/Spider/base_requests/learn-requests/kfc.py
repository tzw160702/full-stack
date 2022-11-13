#!usr/bin/python3
# -*- coding: UTF-8 -*-

"""经验
    - 如果页面点击之后，url随之改变就不是一个ajax请求，反之则是
"""
import csv
import requests

url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
data = {
    'cname': '',
    'pid': '',
    'keyword': '西安',
    'pageIndex': 1,
    'pageSize': 10
}
content = list()


def response_data():
    response = requests.post(url=url, data=data, headers=headers)
    text = response.text
    dic_obj = eval(text.replace('null', '').replace('"pro":,', ''))
    return dic_obj


def pages():
    """总页数"""
    dic_obj = response_data()
    global total
    total = dic_obj['Table'][0]['rowcount']
    pages = (total // 10 + (0 if total % 10 == 0 else 1))
    return pages


def extract():
    for page in range(1, pages()+1):
        data['pageIndex'] = page
        text = response_data()
        for rows in text['Table1']:
            row = dict()
            row['餐厅名称'] = rows['storeName'] + '餐厅'
            row['餐厅详细地址'] = \
                rows['provinceName'] + rows['cityName'] + rows['addressDetail']
            content.append(row)


if __name__ == "__main__":
    extract()
    if len(content) == total:
        print('数据获取完成！！！')
    title = list(content[0].keys())
    file_name = 'kfc_canteen_info_xian.csv'
    try:
        with open(file_name, 'w', encoding='utf-8', newline='') as fp:
            dict_write = csv.DictWriter(fp, fieldnames=title)
            dict_write.writeheader()
            dict_write.writerows(content)
    except Exception as e:
        print(e)



