#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# HOST
HOSTNAME = "127.0.0.1"
# PORT
HOSTPORT = 8080

# SECRET
SECRET_KEY = "5aqb5p2l5piv5L2g"

# MYSQL
HOST_NAME = "120.55.58.140"
PORT = 3307
DATABASE = "ylshini"
USERNAME = "root"
PASSWORD = "root"
BD_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST_NAME}/{DATABASE}?charset=utf8"
SQLALCHEMY_URI = BD_URI

