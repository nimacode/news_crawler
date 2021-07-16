import scrapy
from news.items import NewsItem

class newsSpider(scrapy.Spider):
    name = 'news'

    def start_requests(self):
        yield scrapy.Request(
            url ='https://www.mashreghnews.ir/page/archive.xhtml',
            callback = self.parse
        )

    def parse(self, response):
        news = response.xpath("/html/body/main/div/div/div/div/section/div/ul/li")
        # print (len(news))
        for i in news:
            item = NewsItem()
            item['title'] = i.css("h3 a::text").get()
            item['link'] = i.css("a::attr(href)").get()
            # yield {
                # 'title': item.xpath("/html/body/main/div[1]/div/div/div/section/div/ul/li/div/h3/a").get(),
                # 'link': item.xpath("/html/body/main/div[1]/div/div/div/section/div/ul/li/div/h3/a/@href").get()
            # print (item.css("a::attr(href)").get())
            # print (item.css("h3 a::text").get())

            # }
            print(item)
  
        print()
        print("Next page")
        print()
        next_page = response.xpath("/html/body/main/div[1]/div/div/div/section/footer/div/ul/li[13]/a/@href").get()
        if next_page:
            abs_url = f"https://www.mashreghnews.ir/{next_page}"
            yield scrapy.Request(
                url = abs_url,
                callback = self.parse
            )
        else:
            print()
            print('No Page Left')
            print()
