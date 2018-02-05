#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author : yasin
# @time   : 2018/2/5 15:13
# @File   : requests_practice0.py

import requests
import json

# 总体功能的一个演示
def demo1():
    response = requests.get("https://www.baidu.com")
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)
    print(response.content)
    print(response.content.decode("utf-8"))

# 各种请求方式
def demo2():
    response = requests.post("http://httpbin.org/post")
    print(response.text)
    response = requests.put("http://httpbin.org/put")
    print(response.text)
    response = requests.delete("http://httpbin.org/delete")
    print(response.text)
    response = requests.head("http://httpbin.org/get")
    print(response.text)
    response = requests.options("http://httpbin.org/get")
    print(response.text)

# 基本GET请求
def demo3():
    data = {
        "name": "zhaofan",
        "age": 22
    }
    response = requests.get("http://httpbin.org/get", params=data)
    print(response.url)
    print(response.text)

# 解析json
def demo4():
    response = requests.get("http://httpbin.org/get")
    print(type(response.text))
    print(response.json())
    print(json.loads(response.text))
    print(type(response.json()))

# 添加headers
def demo5():
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.4 Safari/537.36"
    }
    response =requests.get("https://www.zhihu.com", headers= headers)
    print(response.text)

# 基本POST请求
def demo6():
    data = {
        "name": "zhaofan",
        "age": 23
    }
    response = requests.post("http://httpbin.org/post", data=data)
    print(response.text)

# 响应
# 我们可以通过response获得很多属性，例子如下
def demo7():
    response = requests.get("http://www.baidu.com")
    print(type(response.status_code), response.status_code)
    print(type(response.headers), response.headers)
    print(type(response.cookies), response.cookies)
    print(type(response.url), response.url)
    print(type(response.history), response.history)

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    demo7()