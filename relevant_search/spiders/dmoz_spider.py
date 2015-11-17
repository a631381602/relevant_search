#coding:utf-8

import scrapy,re,urllib,os
from relevant_search.items import RelevantSearchItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["www.baidu.com"]

	start_urls = []
	for word in open('/Users/sunjian/Desktop/relevant_search/word'):
		word = word.strip()
		url = 'http://www.baidu.com/s?wd=%s&tn=baidurs2top' % urllib.quote(word) 
		start_urls.append(url)

	def __get_url_query(self, url):
		m =  re.search("wd=(.*?)&tn=baidurs2top", url).group(1)
		return m

	def parse(self,response):
		query = urllib.unquote(self.__get_url_query(response.url))
		text = response.body
		for word in text.split(','):
			word = word.strip()

			item = RelevantSearchItem()
			item['word'] = word
			item['query'] = query

			yield item

			