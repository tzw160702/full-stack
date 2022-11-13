## 项目简介
**【媛来是你】**

**语言：** python

**框架：** Flask 框架

**数据库：** Mysql


## 项目目录结构
```python
├─extensions        # 注册插件
│  ├─ email.py      
│  ├─ models.py     # orm模型
│  └─ __init__.py  
│  
├─static            # 静态文件
├─templates         # 模板文件
│
├─ylshini
│  ├─app                # 应用
│  │  │  urls.py    
│  │  │  views.py       
│  │  │  __init__.py
│  └─__init__.py       
│
├─config.py        # 项目配置文件
├─manage.py        # 项目启动
└─readme.md        # 项目相关介绍

```

## 项目运行
```python
python manage.py runserver
```
