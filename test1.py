import requests
from lxml import etree

# url='https://read.douban.com/kind/100'
url='http://www.yaobiaozhun.com/yd2015'
r=requests.get(url)
# r.encoding='utf-8'

content=etree.HTML(r.content)
for box in content.xpath('//div[@class="cms_list"]/table/tr[position()>1]'):
    box.xpath('./td[1]/a/@href').extract()



# res=content.xpath('//div[@class="cms_list"]/table/tr')
# ur=content.xpath("//a[contains(text(),'下页')]/@href")
# page = 'http://www.yaobiaozhun.com/yd2015/' + ur[0]
# print(page)

# for i in range(2, 22):
#     print(content.xpath('//div[@class="cms_list"]/table/tr[%d]/td[1]/a/text()' % i))
#     n=n+1
# print(n)
# print(content.xpath('//div[@class="cms_list"]/table/tbody/tr[2]/td[1]/a'))
# print(content.xpath("/html/body/div/div[3]/div[3]/table/tbody/tr[2]/td[1]/a"))
# print(content.xpath('/html/body/div/div/article/div[2]/div[1]/ul/li[1]/div[2]/div[2]/a/text()'))
# print(content.xpath('//ul[@class="list-lined ebook-list column-list"]/li[1]/div[2]/div[2]/a/text()'))
# open('/Users/shiyijie/Desktop/1.txt','w').write(result)
# //*[@id="wrap"]/div[3]/div[2]/div[3]/pre/center[1]