
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from centuries.items import CenturiesItem


class centurySpider(BaseSpider):
	name = "century"
	allowed_domains = ["en.wikipedia.org"]
	start_urls = ["https://en.wikipedia.org/wiki/List_of_international_cricket_centuries_by_Sachin_Tendulkar"]



	def parse(self,response):
		print "parsing started !!"
		xps = HtmlXPathSelector(response)
		centuries = xps.select('//*[@id="mw-content-text"]/table[3]/tr/td')
		#print "centuries",centuries

		for idex,century in enumerate(centuries, start=1):
			print "inside loop ",idex,century
			item = CenturiesItem()
			item['number'] = xps.select('//*[@id="mw-content-text"]/table[3]/tr/td[2]/text()').extract()[idex]
			print item['number']
			#item['runs']  = century.select('//tr/td[1]/text()')
			#item['balls'] = century.select('//tr/td[5]/text()')
			#item['against']  = century.select('//tr/td[2]/a/text()')
			#item['date'] = century.select('//tr/td[9]/span[2]/text()')
			#print item['number']
			#print item['runs']
			#print item['against']
