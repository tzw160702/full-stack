import re

content = """
    <div class="art-list-content">
        <a href="/t/1119260" target="_blank">
        <p>真，女汉子啊，这藐视的眼神，这开瓶盖的手法</p><p></p>
        <div id="gif-box-1" class="img-box" style="display:inline-block">  <img src="https://img.6jianshi.com/2021120710344344.gif" id="gif-img-1" class="dgif" tsrc="https://img.6jianshi.com/2021120710344344_s.gif">  
        <div class="img-loading-box" id="gif-loading-div-1" style="display: none;">    
        <i class="img-loading" id="gif-loading-1" style="display: none;"></i>    
        <i class="img-play sgif" id="1" style="display: none;"></i>  
        </div></div><br><p></p></a>                            
    </div>
    
    <div class="art-list-content">
        <a href="/t/1119235" target="_blank">
        <p>小子眼光不错，本性就这样暴露出来了吧！</p><p></p>
        <div id="gif-box-3" class="img-box" style="display:inline-block">  <img src="https://img.6jianshi.com/2021120303224185.gif" id="gif-img-3" class="dgif" tsrc="https://img.6jianshi.com/2021120303224185_s.gif">  
        <div class="img-loading-box" id="gif-loading-div-3" style="display: none;">    
        <i class="img-loading" id="gif-loading-3" style="display: none;"></i>    
        <i class="img-play sgif" id="3" style="display: none;"></i> 
        </div></div><br><p></p></a>                            
    </div>
"""


# re_label = '<div class="art-list-content">.*?<img src="(.*?)" id=.*?</div>'
# re_label = '<div id="gif-box-.*?".*?<img src="(.*?)" id=".*?</div>'
# res = re.findall(re_label, content, re.S)
# print(res)


# url = "https://www.6jianshi.com/page-%d"
# for page_number in range(1, 10):
#     print(page_number)
#     new_url = format(url%page_number)
#     print(new_url)


# url = "https://www.6jianshi.com/page-{0}"
# for page_number in range(1, 10):
#     print(page_number)
#     new_url = format(url.format(page_number))
#     print(new_url)


# import requests
# url = "https://www.6jianshi.com/"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
#
# }
#
# response = requests.get(url=url, headers=headers)
# print(response.status_code)
# if response.status_code == 200:
#     # Requests库的自身编码为: r.encoding = ‘ISO-8859-1’
#     """
#         r.text返回的是Unicode型的数据。
#         使用r.content返回的是bytes型的数据。
#         也就是说，如果你想取文本，可以通过r.text。
#         如果想取图片，文件，则可以通过r.content。
#     """
#     html_doc = response.content.decode("utf-8", "ignore")
#     print(html_doc)
#     re_label = '<div id="gif-box-.*?".*?<img src="(.*?)" id=".*?</div>'
#     images = re.findall(re_label, html_doc, re.S)
#     print(images)

content1 = """
<iframe src="/e/api/web/web.php?act=set_web_js&id=53341039" style="height:0;width:0;"></iframe><!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no">
    <meta name="renderer" content="webkit|ie-stand"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>验证页面</title>
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <script src="/e/js/jquery.js"></script>
    <script src="/e/js/layer/layer.js"></script>
    <style>
        body {background-color:#fff;}
        .main-box {position:fixed;top:0;left:0;right:0;bottom:200px;display:flex;justify-content:center;align-items:center;padding:12px;  font-size:22px; text-align: center;}
        a{color:red;text-decoration: none}
    </style>
</head>

<body>
<div class="main-box">
    <div class="main-box">
        <div>
            <div style="font-size: 22px;">为保证您的正常访问，请进行如下的验证：<br>
                点击下面的文字，找到出路</div><br><br>
            <a href="/pic/page-1">趣图</a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="/txt/page-1">笑话</a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://www.6jianshi.com/">继续访问</a>
        </div>
    </div>
    <div style="visibility: hidden"><script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1260705385'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s11.cnzz.com/z_stat.php%3Fid%3D1260705385' type='text/javascript'%3E%3C/script%3E"));</script>


<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?f7492ca72b93113a4f82b0cf60ad9515";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script></div>
</div>
</body>
</html>
"""

# import re
# label_re = '<a href="(.*?)">.*?</a>'
# url = re.findall(label_re, content1, re.S)[-1]
# print(url)

# 深浅拷贝
import copy
# ls1 = [1, 2, 3, ['name', 'age']]
# als = ls1
# ls1.append(4)
# print(id(ls1), id(als))
# print(ls1, als)

# 浅拷贝
# ls2 = copy.copy(ls1)
# ls2.append(4)
# ls2[3].append('sex')
# print(id(ls1), id(ls2))
# print(ls1, ls2)


# 元组
# tu = (1, "哈哈", [], "呵呵")
# tu[2].append("first")  # 可以更改没报错
# print(tu)


# import os
#
# env = os.getenv('niaghdiosa')
# print(env)


# a = [{1:1, 2:2, 3:3}, {1:1, 2:2, 3:3}, {1:1, 2:2, 3:3}]
# bs = [{5:5, 6:6, 7:7}, {4:5, 6:6, 7:7}, {23:5, 6:6, 7:7}]
# data = list()
# for i in a:
#     for b in bs:
#         i['result'] = b
#         data.append(i)
#         bs.remove(b)
#         break
# print(data)

# s = " 123456789056479874354 313   24679 79 "
# # fp = open('test.txt', 'w', encoding='utf-8')
# # for i in range(int(len(s)//5 + 2)):
# #     print(repr(s[i*5:(i+1)*5] + '\n'))
# #     fp.write('\x20\x20\x20\x20' + s[5*i:5*(i+1)] + '\n')
# ls = s.strip()
# print(repr(ls))


label = """
    <div tongji_tag="fcpc_ersflist_gzcount" class="property" data-v-f11722e6="" data-v-7ba6f82f="">
        <a href="https://xa.58.com/ershoufang/50872026772232x.shtml?auction=200&amp;hpType=60&amp;entry=102&amp;position=0&amp;kwtype=filter&amp;now_time=1659521330&amp;typecode=200&amp;lg=https%3A%2F%2Flegoclick.58.com%2Fjump%3Ftarget%3Dszq3mi3draOWUvYfugF1pAqduh78uztdnj9LnWTzPW0LnWc1nM980v6YUykKuadBuhFBnyF6mzYQPH-WsHw-mhcVmhE3uBYLm1n3PvEOmWbOmWEKrj0OPHn3n1mzPHTvPHEKTHcdrjbdP10LPjcvrj0zn1bKnHcLnjTKnHcLnjTKnikQnkDYrjnKnHmdrHNznHn1njT1nkD1rE7AEdq7NYuxHD-HR7qEEkDQTHDKTiYQTEDQPHNYP1NLPWEdn1ELn10LnHNzTHmKTHDKuHDzmvc1PhEVPvPhmBYYPjcLsHbOrHNVn1K6uhnknHEQnW9kTHDdPHELPH0vPjNYPWE3njbYP1nKnHNdPj0dP1mYPHnkrHm1nWNQnkDKTEDKTiYKTEDKwbEQE17AwHNVrDDvPiYYPDFAsN7jEYcVwbcOEHPjENuAPjEYTHcYnjblrADLnjGBP1mlPvn1njCduAFBrhmkuAcluWRBrHGhPvmvTHTKnTDKnikQnk7exEDQnjT1n9DQnjTQrjn3THmOrH66mWFBsHN3ryNVPjw-midBryN3sHDzPvcvPHw6ryRbuEDKnTDKTHTKPj91sjE3Pzk3n1NvTHDKUMR_UT7-uWmzuju6rAN3PWn1PWbY&amp;spread=filtersearch&amp;from=from_esf_List_search&amp;index=0" data-action="esf_list" target="_blank" data-ep="{&quot;exposure&quot;:{&quot;entry_source&quot;:&quot;Anjuke_Hp_View&quot;,&quot;from_id&quot;:&quot;1&quot;,&quot;project_id&quot;:&quot;200&quot;,&quot;source_type&quot;:1,&quot;hp_type&quot;:&quot;2&quot;,&quot;ax_type&quot;:&quot;1000010&quot;,&quot;search_type&quot;:&quot;filter&quot;,&quot;vpid&quot;:&quot;50872026772232&quot;,&quot;v&quot;:&quot;2.0&quot;,&quot;hp_page&quot;:&quot;Anjuke_Hp_View&quot;,&quot;channel&quot;:&quot;1&quot;,&quot;community_id&quot;:&quot;100469244&quot;,&quot;area_id&quot;:&quot;487&quot;,&quot;esf_id&quot;:50872026772232,&quot;isauction&quot;:200,&quot;pos&quot;:0,&quot;trading_area_ids&quot;:0,&quot;found&quot;:0,&quot;prop_expire&quot;:0,&quot;entry&quot;:0,&quot;tradeType&quot;:&quot;2&quot;,&quot;esf_list&quot;:1,&quot;broker_id&quot;:&quot;202434669&quot;}}" data-cp="{&quot;broker_id&quot;:&quot;202434669&quot;}" data-lego="{&quot;entity_id&quot;:&quot;2589577742687239&quot;,&quot;tid&quot;:&quot;6998ab2b-589e-44ea-b9e8-127b654a9ede&quot;}" class="property-ex" data-v-f11722e6="" data-exposure="true">
            <div class="property-image" data-v-f11722e6="">
                <img alt="" src="https://pic1.ajkimg.com/display/58ajk/dddb1d7652a0b219726e39cbcac59535/640x420c.jpg?t=1" class="lazy-img cover" data-v-28819723="" data-v-f11722e6="" data-src="https://pic1.ajkimg.com/display/58ajk/dddb1d7652a0b219726e39cbcac59535/640x420c.jpg?t=1" lazy="loaded"> 
                <!---->
            </div> 
            <div class="property-content" data-v-f11722e6="">
                <div class="property-content-detail" data-v-f11722e6="">
                    <div class="property-content-title" data-v-f11722e6="">
                        <h3 title="2室1厅 满二 81平 精装修 诚心出售 价格可议" class="property-content-title-name" style="max-width:501px;" data-v-f11722e6="">2室1厅 满二 81平 精装修 诚心出售 价格可议
                        </h3> 
                        <img src="https://pages.anjukestatic.com/usersite/site/img/broker_detail/esf_list_img_anxuangolden@2x.png" class="property-content-title-anxuan" style="width:38px;height:24px;" data-v-f11722e6="">  
                        <span class="property-content-title-othertag-ad" data-v-f11722e6="">广告</span>
                    </div> 
                    <section data-v-f11722e6="">
                        <div class="property-content-info" data-v-f11722e6="">
                            <p class="property-content-info-text property-content-info-attribute" data-v-f11722e6="">
                                <span data-v-f11722e6="">2</span> 
                                <span data-v-f11722e6="">室</span> 
                                <span data-v-f11722e6="">1</span> 
                                <span data-v-f11722e6="">厅</span> 
                                <span data-v-f11722e6="">1</span> 
                                <span data-v-f11722e6="">卫</span>
                            </p> 
                            <p class="property-content-info-text" data-v-f11722e6="">81.4㎡</p> 
                            <p class="property-content-info-text" data-v-f11722e6="">西南</p> 
                            <p class="property-content-info-text" data-v-f11722e6="">低层(共18层)</p> 
                            <p class="property-content-info-text" data-v-f11722e6="">2005年建造</p>
                        </div> 
                        <div class="property-content-info property-content-info-comm" data-v-f11722e6="">
                            <p class="property-content-info-comm-name" data-v-f11722e6="">幸福时光</p> 
                            <p class="property-content-info-comm-address" data-v-f11722e6="">
                                <span data-v-f11722e6="">雁塔</span>
                                <span data-v-f11722e6="">电子正街</span>
                                <span data-v-f11722e6="">电子二路,近电子东路</span>
                            </p>
                        </div> 
                        <div class="property-content-info" data-v-f11722e6="">
                            <span class="property-content-info-tag" data-v-f11722e6="">满二年</span>
                            <span class="property-content-info-tag" data-v-f11722e6="">新上</span>
                        </div>
                    </section> 
                    <div class="property-extra-wrap" data-v-f11722e6="">
                        <div class="property-extra" data-v-f11722e6="">
                            <div class="property-extra-photo" data-v-f11722e6="">
                                <img alt="" src="https://spic1.ajkimg.com/6oGvxlrmWqI-Ir1yXyhAKgMVIz_wuhhsji-wruLkwQhr10OpQLzWc2SwJzHfMTQgqAY_VK6qrYZrG3dAQGQX-AP8GAe02qVORndoKr1y6UPgfd3Gzt4VhscwfE3TE5sRQT4PWJoe0Et2zPDamwaMfT_rPTBlKN-gqoBaZw77qvOGZr_m51in3AqV4uCUkCZG" class="lazy-img cover" data-v-28819723="" data-v-f11722e6="" data-src="https://spic1.ajkimg.com/6oGvxlrmWqI-Ir1yXyhAKgMVIz_wuhhsji-wruLkwQhr10OpQLzWc2SwJzHfMTQgqAY_VK6qrYZrG3dAQGQX-AP8GAe02qVORndoKr1y6UPgfd3Gzt4VhscwfE3TE5sRQT4PWJoe0Et2zPDamwaMfT_rPTBlKN-gqoBaZw77qvOGZr_m51in3AqV4uCUkCZG" lazy="loaded">
                            </div> 
                            <span class="property-extra-text" data-v-f11722e6="">党晓伟</span>
                            <div class="property-extra-anxuan" data-v-f11722e6="">
                            <img alt="" src="https://pages.anjukestatic.com/usersite/site/img/prop_list/esf_list_img_wuyoujiaoyi@2x.png" class="lazy-img cover" data-v-28819723="" data-v-f11722e6="" data-src="https://pages.anjukestatic.com/usersite/site/img/prop_list/esf_list_img_wuyoujiaoyi@2x.png" lazy="loaded">
                            </div> 
                            <span class="property-extra-text" data-v-f11722e6="">4.6分</span> 
                            <span class="property-extra-text" data-v-f11722e6="">合和致远</span> 
                            <span class="property-extra-text verification-tag" data-v-f11722e6="">本房由我首次实勘，熟悉房屋信息和特色</span>
                        </div> 
                        <!---->
                    </div> 
                    <!---->
                </div> 
                <div class="property-price" data-v-f11722e6="">
                    <p class="property-price-total" data-v-f11722e6="">
                        <span class="property-price-total-num" data-v-f11722e6="">116</span> 
                        <span class="property-price-total-text" data-v-f11722e6="">万</span>
                    </p> 
                    <p class="property-price-average" data-v-f11722e6="">14246元/㎡</p>
                </div>
            </div>
        </a>
    </div>

"""

from lxml import etree

contents = etree.HTML(label)

# for content in contents:
#     # 标题
#     title = content.xpath('.//div[@class="property-content-title"]/h3/@title')
#     # 户型
#     house_type = ''.join(content.xpath('.//div[@class="property-content-info"]/p/span/text()'))
#
#     p = content.xpath('.//div[@class="property-content-info"]/p/text()')
#     # 面积
#     areas = p[-4]
#     # 楼层
#     floor_number = p[-2]
#     #朝向
#     orientation = p[-3]
#     # 建造
#     build = p[-1]
#
#     # 楼盘
#     village_name = content.xpath('.//p[@class="property-content-info-comm-name"]/text()')
#
#     # 位置
#     address = ''.join(content.xpath('.//p[@class="property-content-info-comm-address"]/span/text()'))
#
#     price = content.xpath('.//div[@class="property-price"]/p/text()')
#     # 总价
#     total_prices = ''.join(content.xpath('.//p[@class="property-price-total"]/span/text()'))
#     # 均价
#     average_prices = content.xpath('.//p[@class="property-price-average"]/text()')[0]

# for page in range(2, 59):
#     print(page)











