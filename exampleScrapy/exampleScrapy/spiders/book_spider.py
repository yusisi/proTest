# -*- coding: utf-8 -*-

import scrapy

class BooksSpider(scrapy.Spider):
	# 每一个爬虫的唯一标识
	name = "books"

	# 定义爬虫爬取的起始点，起始点可以是多个，这里只有一个
	start_urls = ['http://mebook.cc/']

	def parse(self, response):

		for book in response.css('div.content'):
			name = book.xpath('./h2/a/@title').extract_first()

			auther = book.xpath('./h2/a/@href').extract_first()
			yield {
					'name': name,
					'auther': auther,
			}

		# 提取链接
		# 下一页的url 在ul.pager > li.next > a 里面
		# 例如: <li class="next"><a href="catalogue/page-2.html">next</a></li>
		next_url = response.css(
			'div.pagenavi a::attr(href)').extract_first()
		if next_url:
			# 如果找到下一页的URL，得到绝对路径，构造新的Request 对象
			next_url = response.urljoin(next_url)
			yield scrapy.Request(next_url, callback=self.parse)
