#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask, request, Response
from weather import get_weather_by_ip

app = Flask(__name__)
app.config['FLASK_DEBUG'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'


# 根据IP地理位置获取天气
@app.route('/getweather')
def get_weather():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        json_data = get_weather_by_ip(str(x_forwarded_for))
        return Response(json_data, mimetype='application/json')
    return 'ip错误'


# 获取IP地址
@app.route('/getip')
def get_ip():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        return str(x_forwarded_for)
    return 'ip错误'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
