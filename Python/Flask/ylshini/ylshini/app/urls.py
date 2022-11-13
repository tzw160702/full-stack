#!usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Blueprint
from .views import index

# user = Blueprint('user', __name__)
user = Blueprint('user', __name__, url_prefix='/v1')

# 用户
user.add_url_rule(
    '/index', view_func=index, methods=['GET'], endpoint='index', )
