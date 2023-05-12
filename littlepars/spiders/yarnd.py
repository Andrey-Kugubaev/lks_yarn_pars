import scrapy

from littlepars.items import LittleparsItem


class YarndSpider(scrapy.Spider):
    name = "yarnd"
    start_urls = [
        "https://www.yarndatabase.com/a-z-designers/",
        "https://www.yarndatabase.com/a-z-dyers/",
        "https://www.yarndatabase.com/a-z-spin/",
        "https://www.yarndatabase.com/a-z-accessories/",
        "https://www.yarndatabase.com/tech-editors-a-z/"
    ]

    def parse(self, response):
        all_links_common = response.css('div.items-inner').css('li')
        all_links = all_links_common.css('a::attr(href)').getall()
        for yarnd_link in all_links:
            yield response.follow(yarnd_link, self.parse_links)

    def parse_links(self, response):
        title_css = response.css('div.post-header')
        link_css = response.css('div.post-content')
        title = title_css.xpath('//h1/text()').get()
        link_header = title_css.css('a:contains("http")::text').getall()
        link_content = link_css.css('a:contains("http")::text').getall()
        link = []
        if link_header is not None:
            for i in link_header:
                link.append(i)
        if link_content is not None:
            for j in link_content:
                link.append(j)

        data = {
            'title': title,
            'link': link,
        }
        yield LittleparsItem(data)
