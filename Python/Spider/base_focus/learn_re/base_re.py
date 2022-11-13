# -----------------------------------------------------------------------------
# 聚焦爬虫：爬取页面中制定页面内容
#   - 流程:
#         - 指定 URL
#         - 发起请求
#         - 获取响应数据
#         - 数据解析
#         - 持久化存储
# 数据解析分类:
#   - 正则
#   - bs4
#   - xpath

# 数据解析原理概述:
#   - 解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
#       1. 进行指定标签的定位
#       2. 标签或者标签对应的属性中存储的数据值进行提取（解析）
# -----------------------------------------------------------------------------

import os
import re
import requests

if __name__ == "__main__":
    # 目标网址：《6见事》
    url = "https://www.6jianshi.com/page-%d"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
    }
    for page_number in range(1, 10):
        new_url = format(url%page_number)
        response = requests.get(url=new_url, headers=headers)
        print(f'正在加载第{page_number}页!')
        if response.status_code == 200:
            # Requests库的自身编码为: r.encoding = ‘ISO-8859-1’
            """
                r.text返回的是Unicode型的数据。
                使用r.content返回的是bytes型的数据。
                也就是说，如果你想取文本，可以通过r.text。
                如果想取图片，文件，则可以通过r.content。
            """
            html_doc = response.content.decode("utf-8", "ignore")
            re_label = '<div id="gif-box-.*?".*?<img src="(.*?)" id=".*?</div>'

            images = re.findall(re_label, html_doc, re.S)
            try:
                images = re.findall(re_label, html_doc, re.S)
                for image_url in images:
                    try:
                        image_data = requests.get(url=image_url, headers=headers)
                        if image_data.status_code == 200:
                            if not os.path.exists('6jianshi_image'):
                                os.mkdir('6jianshi_image')
                            # 图片名称
                            image_name = image_url.split('/')[-1]
                            with open('./6jianshi_image/'+image_name, 'wb') as f:
                                f.write(image_data.content)
                                print(f'文件 {image_name} 开始下载, 下载成功！！！')
                        else:
                            print('请求图片地址失败!!!')
                    except Exception as e:
                        print('请求图片异常', e)
            except Exception as e:
                print('请求网页异常', e)

            # 卡顿，防止请求太频繁
            import time
            time.sleep(0.5)
        else:
            print('请求6见事失败！！！')