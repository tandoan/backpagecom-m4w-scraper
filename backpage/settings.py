# Scrapy settings for backpage project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'backpage'

SPIDER_MODULES = ['backpage.spiders']
NEWSPIDER_MODULE = 'backpage.spiders'

ITEM_PIPELINES = {
  'scrapy.contrib.pipeline.images.ImagesPipeline': 1
}

IMAGES_STORE = '/home/vagrant/m4w'
DOWNLOAD_DELAY = 0.25
COOKIES_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'backpage (+http://www.yourdomain.com)'
