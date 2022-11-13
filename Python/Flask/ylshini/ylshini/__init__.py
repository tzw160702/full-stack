#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask
import config
# from flask_migrate import Migrate
# from extensions import db


def create_app():
    """
    工厂模式创建应用
    :return:
    """
    app = Flask(__name__)

    # 加载配置项
    app.config.from_object(config)

    # 数据迁移
    # migrate = Migrate(app, db)

    # db.init_app(app)

    # 注册蓝图
    from .app.urls import user
    app.register_blueprint(user)

    return app


