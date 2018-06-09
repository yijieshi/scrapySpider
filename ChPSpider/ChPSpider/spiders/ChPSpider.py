# -*- coding: utf-8 -*-
import scrapy
from ChPSpider.items import ChPSpiderItem

class ChPSpider(scrapy.Spider):

    # scrapy爬虫名称
    name = "ChPSpider"

    allowed_domains = ["http://www.yaobiaozhun.com"]

    start_urls = ["http://www.yaobiaozhun.com/yd2015/"]


    def parse(self, response):

        for box in response.xpath('//div[@class="cms_list"]/table/tr[position()>1]'):
            # 实例化item
            item = ChPSpiderItem()
            # 获取完整的第二级中药名详情url
            item['url'] = 'http://www.yaobiaozhun.com/yd2015/' + box.xpath('./td[1]/a/@href').extract()[0]
            # 提取第一级页面中需要的信息
            item['nameCHN'] = box.xpath('./td[1]/a/text()').extract()
            item['laiYuan'] =box.xpath('./td[2]/text()').extract()
            item['fenLei'] =box.xpath('./td[3]/text()').extract()
            item['yeMa'] = box.xpath('./td[4]/text()').extract()
            # 传入参数到第二级页面处理函数
            # 把item的元数据传入子页面的request中
            # 关闭Scrapy的自动去重机制
            yield scrapy.Request(url=item['url'], meta={'item':item},callback=self.parse_detail,dont_filter=True)


        # 翻页处理
        # 定位网站翻页的超链接
        url = response.xpath("//a[contains(text(),'下页')]/@href").extract()
        # 判定是否存在下一页
        if url :
            # 拼接url
            page = 'http://www.yaobiaozhun.com/yd2015/' + url[0]
            # 迭代
            yield scrapy.Request(page, callback=self.parse,dont_filter=True)

    # 第二级页面处理函数
    def parse_detail(self,response):
        # 导入第一级页面item的元数据
        item = response.meta['item']
        # 提取第二级页面中需要的信息
        item['namePY'] = response.xpath('//div[@class="cms_list"]/pre/center[2]/b/text()').extract()
        item['nameENG'] = response.xpath('//div[@class="cms_list"]/pre/center[3]/b/text()').extract()
        # 去除/r/n
        # item['detail'] = response.xpath('normalize-space(//div[@class="cms_list"]/pre/div[@id="content_text"]/text())').extract()
        item['detail'] = response.xpath('//div[@class="cms_list"]/pre/div[@id="content_text"]/text()').extract()
        # 在终极目录yield
        yield item