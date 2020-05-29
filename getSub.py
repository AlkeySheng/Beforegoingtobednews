#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File: getSub.py
@Description: 爬取《睡前消息》节目简介中的新闻事件
@Time: 2020/05/29 14:32:17
@Author: 盛亚琪
@Blog: i.2017.work
'''

import requests
import xlwt


def main():
    li = []
    for n in range(1, 13):
        print("保存第", n, "页")
        root = getJson(n)
        getCon(root, li)
    saveXl(li)


def getJson(n=1):  # 获取单页JSON数据
    re = requests.get(
        "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=54992199&pagesize=100&page={}".format(n))
    re.encoding = ("utf-8")
    root = re.json()
    return root


def getCon(root, li):  # 传入JSon解析内容进列表
    for v in root["data"]["vlist"]:
        if "睡前消息" in v["title"]:
            li.append([v["title"], v["description"], v["play"], v["aid"]])


def saveXl(li):
    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("sheet1")
    col = ["标题", "简介", "播放量", "aid"]
    for i in range(len(col)):
        ws.write(0, i, col[i])
    for i in range(1, len(li)+1):
        ws.write(i, 0, li[i-1][0])
        ws.write(i, 1, li[i-1][1])
        ws.write(i, 2, li[i-1][2])
        ws.write(i, 3, li[i-1][3])
    wb.save("《睡前消息》节目往期新闻事件索引.xls")


def priIt(li):
    pr = ""
    for i in li:
        pr += ("\n"+"## "+str(i[0])+"\n" + "------"+"\n"+str(i[1]))
    print(pr)


if __name__ == "__main__":
    main()
