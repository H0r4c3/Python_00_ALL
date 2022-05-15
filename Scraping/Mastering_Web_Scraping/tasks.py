'https://betterprogramming.pub/mastering-web-scraping-in-python-scaling-to-distributed-crawling-34017a1322c7'

'https://www.zenrows.com/blog/mastering-web-scraping-in-python-scaling-to-distributed-crawling?utm_source=medium&utm_medium=blog&utm_campaign=distributed_crawling'


from celery import Celery 
import requests 
from bs4 import BeautifulSoup 
from urllib.parse import urljoin 
 
app = Celery('tasks', broker_url='redis://127.0.0.1:6379/1') 
 
@app.task 
def crawl(url): 
	html = get_html(url) 
	soup = BeautifulSoup(html, 'html.parser') 
	links = extract_links(url, soup) 
	print(links) 
 
def get_html(url): 
	try: 
		response = requests.get(url) 
		return response.content 
	except Exception as e: 
		print(e) 
 
	return '' 
 
def extract_links(url, soup): 
	return list({ 
		urljoin(url, a.get('href')) 
		for a in soup.find_all('a') 
		if a.get('href') and not(a.get('rel') and 'nofollow' in a.get('rel')) 
	}) 
 
#starting_url = 'https://scrapeme.live/shop/page/1/' 
#crawl.delay(starting_url)