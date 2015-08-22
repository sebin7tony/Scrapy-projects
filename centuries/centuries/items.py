# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CenturiesItem(Item):
	number = Field()
	runs = Field()
	balls = Field()
	against = Field()
	date = Field()
	venue = Field()
	link = Field()
	