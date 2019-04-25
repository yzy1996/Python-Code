# 爬谷歌的图片
# keyword是关键词

from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': '111'})
google_crawler.crawl(keyword='cat', max_num=10)