# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChPSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #详情页面url
     url = scrapy.Field()

    # 中药中文名
     nameCHN = scrapy.Field()

    # 中药名拼音
     namePY = scrapy.Field()

    # 中药英文名
     nameENG = scrapy.Field()

    # 来源
     laiYuan = scrapy.Field()

    # 分类
     fenLei = scrapy.Field()

    # 页码
     yeMa = scrapy.Field()

    # 详情
     detail = scrapy.Field()
'''
    # 性状
    xingZhuang = scrapy.Field()

    # 鉴别
    jianBie = scrapy.Field()

    # 检查
    jianCha = scrapy.Field()

    # 浸出物
    jinChuWu = scrapy.Field()

    # 含量测定
    hanLiangCeDing = scrapy.Field()

    # 炮制
    paoZhi = scrapy.Field()

    # 性味与归经
    xingWeiYuGuiJing = scrapy.Field()

    # 功能与主治
    gongNengYuZhuZhi = scrapy.Field()

    # 用法与用量
    yongFaYuYongLiang = scrapy.Field()

    # 贮藏
    zhuCang = scrapy.Field()
'''

