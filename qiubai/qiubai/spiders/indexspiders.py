import scrapy
from qiubai.items import QiubaiItem
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class QiuBaiSpider(CrawlSpider):
    name = "qiubai"
    start_urls = [
        "http://www.dianping.com/search/category/2/45/g147",
    ]


    def parse_name(self, response):
        extractor = LinkExtractor(allow="/shop/*", deny="[/shop/*/review, /shop/*?]")
        links = extractor.extract_links(response)
        for link in links:
            print link.url


'''

class QiuBaiSpider(scrapy.Spider):
    name = "qiubai"
    start_urls = [
        "http://www.qiushibaike.com",
    ]

    def parse(self, response):
        extractor = LinkExtractor(allow='article/*')
        links = extractor.extract_links(response)
        for link in links:
            req = Request(link.url, self.parse_detail_page)
            item = QiubaiItem()
            req.meta['item'] = item
            yield req

        #for href in response.xpath('//div[@class="stats"]/span[2]/a/@href').extract():
        #    detail_url = response.urljoin(href)
        #    req = Request(detail_url, self.parse_detail_page)
        #    item = QiubaiItem()
        #    req.meta['item'] = item
        #    yield req

    def parse_detail_page(self, response):
        item = response.meta['item']
        item['author'] = response.xpath('//div[@class="author clearfix"]/a[2]/h2/text()').extract()[0]
        item['content'] = response.xpath('//div[@class="content"]/text()').extract()[0]
        comments = []
        for comment in response.xpath('//div[starts-with(@class,"comment-block clearfix floor")]'):
            comment_authors = comment.xpath('./div[@class="replay"]/a/text()').extract()[0]
            comment_contents = comment.xpath('./div[@class="replay"]/span/text()').extract()[0]
            comments.append({'comment_authors': comment_authors, 'comment_contents': comment_contents})
        item['comment'] = comments
        yield item



    #def parse(self, response):
	#	for ele in response.xpath('//div[@class="article block untagged mb15"]'):
	#		authors = ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
	#		contents = ele.xpath('./div[@class="content"]/text()').extract()
	#		yield QiubaiItem(author=authors, content=contents)
    #

'''
