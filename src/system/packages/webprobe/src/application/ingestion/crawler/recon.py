


from crawl4ai import *

# TODO: Implement crawlPage function to use crawl4ai to crawl a page
async def CrawlPage(target_page: str) -> None:
    async with AsyncWebCrawler() as crawler:
        await crawler.crawl(target_page)


# TODO: Implement crawlPage function to use crawl4ai to crawl a page
# https://github.com/unclecode/crawl4ai
async def CrawlSiteForPages(target_site: str) -> None:
    async with AsyncWebCrawler() as crawler:
        await crawler.crawl(target_site)

