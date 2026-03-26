import scrapy
from scrapy_playwright.page import PageMethod
from arizonarealestate.items import ArizonarealestateItem


class ArizonaSpider(scrapy.Spider):
    name = "arizona"
    allowed_domains = ["arizonarealestate.com"]

    async def start(self):
        yield scrapy.Request(
            url="https://www.arizonarealestate.com/",
            callback=self.parse_places,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_timeout", 3000),
                ],
            },
        )

    def parse_places(self, response):
        links = response.xpath(
            '//h2[contains(., "Get To Know Arizona")]/following-sibling::ul[1]//a/@href'
        ).getall()

        for link in set(links):
            if link and "/cities/" not in link:
                yield response.follow(
                    link,
                    callback=self.parse_listings,
                    meta={"playwright": True},
                )

    def parse_listings(self, response):
        cards = response.xpath('//div[contains(@class,"si-listing")]')

        for card in cards:
            item = ArizonarealestateItem()

            item["listing_id"] = card.xpath('./@id').get()
            item["detail_url"] = response.urljoin(card.xpath('./@data-url').get() or "")

            item["mls_id"] = card.xpath(
                './/button[contains(@class,"si-listing__like")]/@data-mlsid'
            ).get()

            item["mls_region_id"] = card.xpath(
                './/button[contains(@class,"si-listing__like")]/@data-mlsregionid'
            ).get()

            item["price_raw"] = card.xpath(
                './/button[contains(@class,"si-listing__like")]/@data-price'
            ).get()

            item["mls_number"] = card.xpath(
                './/button[contains(@class,"si-listing__like")]/@data-mls'
            ).get()

            item["image_url"] = card.xpath(
                './/div[contains(@class,"si-listing__photo-img")]//img/@src'
            ).get()

            item["image_alt"] = card.xpath(
                './/div[contains(@class,"si-listing__photo-img")]//img/@alt'
            ).get()

            item["price"] = (
                card.xpath('.//div[contains(@class,"si-listing__photo-price")]//span/text()').get()
                or ""
            ).strip()

            item["photo_count"] = (
                card.xpath('.//div[contains(@class,"si-listing__photo-count")]/text()').get()
                or ""
            ).strip()

            item["title_main"] = (
                card.xpath('.//div[contains(@class,"si-listing__title-main")]/text()').get()
                or ""
            ).strip()

            item["title_description"] = (
                card.xpath('.//div[contains(@class,"si-listing__title-description")]/text()').get()
                or ""
            ).strip()

            item["neighborhood"] = (
                card.xpath('.//span[contains(@class,"si-listing__neighborhood-place")]/text()').get()
                or ""
            ).strip()

            info_values = [
                t.strip()
                for t in card.xpath(
                    './/div[contains(@class,"si-listing__info-value")]//text()'
                ).getall()
                if t.strip()
            ]

            item["beds"] = info_values[0] if len(info_values) > 0 else ""
            item["baths"] = "".join(info_values[1:4]) if len(info_values) > 1 else ""
            item["sqft"] = info_values[4] if len(info_values) > 4 else ""

            item["footer"] = " ".join(
                t.strip()
                for t in card.xpath(
                    './/div[contains(@class,"si-listing__footer")]//text()'
                ).getall()
                if t.strip()
            )

            item["source_page"] = response.url

            yield item

        next_page = response.xpath(
            '//a[contains(@class,"next") or contains(.,"Next")]/@href'
        ).get()

        if next_page:
            yield response.follow(
                next_page,
                callback=self.parse_listings,
                meta={"playwright": True},
            )