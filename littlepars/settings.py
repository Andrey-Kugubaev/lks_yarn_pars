BOT_NAME = "littlepars"

SPIDER_MODULES = ["littlepars.spiders"]
NEWSPIDER_MODULE = "littlepars.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


FEEDS = {
    'knits_list.json': {
        'format': 'json',
        'fields': ['title', 'link'],
        'overwrite': True
    },
}
