import requests
#request info from a webpage
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.kixify.com/search?page="+str(page)+"&gender[0]=Men"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.find_all('a',{'class': "col-xs-6 col-sm-3 col-md-3 product-teaser"}):
            href = link.get('href')
            print(href)
        page +=1


trade_spider(1)
