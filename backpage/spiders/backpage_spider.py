from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from time import sleep
from scrapy import log

from backpage.items import BackPageImage

class BackPageSpider(BaseSpider):
  name = "backpage"
  allowed_domains = ["backpage.com"]
  start_urls = [
    "http://losangeles.backpage.com/MenSeekWomen/",
    "http://sf.backpage.com/MenSeekWomen/",
    "http://vancouver.backpage.com/MenSeekWomen/",
    "http://manhattan.backpage.com/MenSeekWomen/",
  ]

  def parse(self, response):
    sel = Selector(response)
    posts = sel.xpath('//div[@class="cat summary"]')
    for post in posts:
      link_array = post.xpath('a/@href').extract()
      link = link_array[0]
      yield Request(url=link, callback=self.parse_post, errback=self.parse_post_err)

  def parse_post_err(self, response):
    print 'ERROR!'
    yield

  def parse_post(self, response):
    sel = Selector(response)
    links = sel.xpath('//ul[@id="viewAdPhotoLayout"]/li/a')
    for link in links:
      link_text = link.xpath('text()').extract()
      if link_text:
        pic_page = link.xpath('@href').extract()
        yield Request(url = pic_page[0], callback=self.parse_pic_page)

  def parse_pic_page(self, response):
    sel = Selector(response)
    imgs = sel.xpath('//img')
    for img in imgs:
      img_src = img.xpath('@src').extract()
      item = BackPageImage()
      item['image_urls'] = img_src
      return item
    
