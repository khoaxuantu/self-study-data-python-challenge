BOT_NAME = "indeed"

SPIDER_MODULES = ["indeed.spiders"]
NEWSPIDER_MODULE = "indeed.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

## ScrapeOps API Key
### Really? You hardcoded the API key in the code? Please don't do this in production code. And also you should let the users know about this in the README file.
SCRAPEOPS_API_KEY = (
    "<APIKEY_MASK>"  ## Get Free API KEY here: https://scrapeops.io/app/register/main
)


# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {
    "scrapeops_scrapy.extension.ScrapeOpsMonitor": 500,
}


DOWNLOADER_MIDDLEWARES = {
    ## ScrapeOps Monitor
    "scrapeops_scrapy.middleware.retry.RetryMiddleware": 550,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    ## Proxy Middleware
    "indeed.middlewares.ScrapeOpsProxyMiddleware": 725,
}

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1
