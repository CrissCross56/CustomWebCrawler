# we import path to be able to write data to a file on the computer
from pathlib import Path
#import scrapy to use scrapy, must reference scrapy obj to use scrapy fucntions and classes such as spiders and requests
import scrapy

#defin a spider class that inherits from scrapy.Spider, gives our spider the ability to log and request pages
class QuotesSpider(scrapy.Spider):
    #all spdiers must have a name, this is how we will reference the spider when we run it
    name = "quotes"

    #every spider has an async generator, scrapy calls this  whenever the spider starts running, it creates the first set of requests
    async def start(self):
        #the list of urls the spider will crawl on
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        # for every url in the list of urls, we yield a scrapy request to that url, and we tell scrapy to call the parse method with the response it gets back
        #the yield is what returns the request to scrapy, it is an async generator
        for url in urls:
            #subsequent requests will be generated frmo these initial requests
            #we ask scrapy to make a request to the url, and call the parse method with that response in order to parse the data scrapy got from the url
            yield scrapy.Request(url=url, callback=self.parse)

    #the parse method
    def parse(self, response):
        #we get the page number from the url, we split the url by / and get the second to last element, which is the page number
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

       