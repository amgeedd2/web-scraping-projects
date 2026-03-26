# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# import re
# from itemloaders.processors import MapCompose


# def description_input_processor(text):
#
#     # text = re.sub(r',+', '', text)
#     # text.replace(r',+', '')
#     return text.replace(',', '').strip()

# def description_output_processor(value):
#     return value
class ArizonarealestateItem(scrapy.Item):
     listing_id = scrapy.Field()
     detail_url = scrapy.Field()
     mls_id = scrapy.Field()
     mls_region_id = scrapy.Field()
     price_raw = scrapy.Field()
     mls_number = scrapy.Field()
     image_url = scrapy.Field()
     image_alt = scrapy.Field()
     price = scrapy.Field()
     photo_count = scrapy.Field()
     title_main = scrapy.Field()
     title_description = scrapy.Field()
     neighborhood = scrapy.Field()
     beds = scrapy.Field()
     baths = scrapy.Field()
     sqft = scrapy.Field()
     footer = scrapy.Field()
     source_page = scrapy.Field()



