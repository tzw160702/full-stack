#!usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import jsonify, render_template, redirect


def index():
    context = {'info': {'name': 'ylshini'}}
    # return jsonify({'info': {'name': 'ylshini'}})

    return render_template('index.html', context=context)
