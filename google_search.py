import requests
import random
from bs4 import BeautifulSoup
from newsplease import NewsPlease
useragent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
]
user_agent = {
    "User-Agent": random.choice(useragent_list)
    }

with open('data/valid_ips.txt', 'r') as f:
    proxies = f.read().split('\n')

base_url = 'https://www.google.com/search?q='
content = input('Enter the topic: ')
domain_list = '''
(site:https://www.ucanews.com OR site:https://www.thestatesman.com OR site:https://www.thenews.com.pk OR site:https://www.telegraphindia.com OR site:https://www.taiwannews.com.tw OR site:https://www.sentinelassam.com OR site:https://www.opindia.com OR site:https://www.ndtv.com OR site:https://www.irrawaddy.com OR site:https://www.indiatoday.in OR site:https://www.hindustantimes.com OR site:https://www.deccanherald.com OR site:https://www.dawn.com OR site:https://www.dailypioneer.com OR site:https://www.cnbctv18.com OR site:https://www.bnionline.net/en OR site:https://www.altnews.in OR site:https://www.aa.com.tr/en OR site:https://tribune.com.pk OR site:https://timesofindia.indiatimes.com OR site:https://thepeninsulaqatar.com OR site:https://thehimalayantimes.com OR site:https://scroll.in OR site:https://nenow.in/north-east-news OR site:https://myrepublica.nagariknetwork.com OR site:https://menafn.com OR site:https://indiablooms.com OR site:https://focustaiwan.tw OR site:https://economictimes.indiatimes.com OR site:https://bangaloremirror.indiatimes.com OR site:https://asumetech.com OR site:http://www.tribuneindia.com OR site:http://www.thehindu.com OR site:http://www.newindianexpress.com OR site:http://www.dnaindia.com OR site:http://www.dailymirror.lk OR site:http://www.aljazeera.com OR site:http://indianexpress.com OR site:http://www.amadershomoy.com/ OR site:https://www.thedailystar.net/bangla/ OR site:https://bangla.dhakatribune.com/ OR site:http://www.jjdin.com/ OR site:http://www.prothomalo.com/ OR site:http://www.mzamin.com/ OR site:http://www.kalerkantho.com/ OR site:http://www.ittefaq.com.bd/ OR site:http://www.bd-pratidin.com/ OR site:https://samakal.com/ OR site:https://www.ajkerpatrika.com/ OR site:https://kalbela.com/ OR site:http://www.dailyinqilab.com/ OR site:https://www.dailyjanakantha.com/ OR site:https://www.deshrupantor.com/epaper/ OR site:https://www.thedailystar.net OR site:https://en.prothomalo.com/ OR site:https://www.observerbd.com/ OR site:https://bdnews24.com/ OR site:https://thefinancialexpress.com.bd/ OR site:https://www.daily-sun.com/ OR site:https://www.dhakatribune.com/ OR site:https://unb.com.bd/ OR site:https://en.ntvbd.com/ OR site:https://www.tbsnews.net/ OR site:https://www.banglanews24.com/english/ OR site:https://www.ajkerpatrika.com/ OR site:https://www.deshrupantor.com/ OR site:https://www.bd-journal.com/ OR site:https://www.dailyjanakantha.com/ OR site:https://bonikbarta.net/)
'''

query = base_url+content+domain_list

proxy_ip = random.choice(proxies)
proxy = {
    'http':proxy_ip,
    'https':proxy_ip
}

print(query)
print()

urls = []
response = requests.get(url=query, timeout= 30, headers= user_agent)
if response.status_code==200:
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find_all('div', class_ = 'g')
    for result in div:
        url = result.find("a", href = True)
        urls.append(url['href'])

for url in urls:
    article = NewsPlease.from_url(url)
    print(article.title)
    print(article.description)
    print()





































# from urllib import response
# import requests
# import time
# import random
# from bs4 import BeautifulSoup
# from googlesearch import search

# with open('data/valid_ips.txt', 'r') as f:
#     proxy_ips = f.read().split('\n')

# domains = [
#     "https://www.ucanews.com",
#     "https://www.thestatesman.com",
#     "https://www.thenews.com.pk",
#     "https://www.telegraphindia.com",
#     "https://www.taiwannews.com.tw",
#     "https://www.sentinelassam.com",
#     "https://www.opindia.com",
#     "https://www.ndtv.com",
#     "https://www.irrawaddy.com",
#     "https://www.indiatoday.in",
#     "https://www.hindustantimes.com",
#     "https://www.deccanherald.com",
#     "https://www.dawn.com",
#     "https://www.dailypioneer.com",
#     "https://www.cnbctv18.com",
#     "https://www.bnionline.net/en",
#     "https://www.altnews.in",
#     "https://www.aa.com.tr/en",
#     "https://tribune.com.pk",
#     "https://timesofindia.indiatimes.com",
#     "https://thepeninsulaqatar.com",
#     "https://thehimalayantimes.com",
#     "https://scroll.in",
#     "https://nenow.in/north-east-news",
#     "https://myrepublica.nagariknetwork.com",
#     "https://menafn.com",
#     "https://indiablooms.com",
#     "https://focustaiwan.tw",
#     "https://economictimes.indiatimes.com",
#     "https://bangaloremirror.indiatimes.com",
#     "https://asumetech.com",
#     "http://www.tribuneindia.com",
#     "http://www.thehindu.com",
#     "http://www.newindianexpress.com",
#     "http://www.dnaindia.com",
#     "http://www.dailymirror.lk",
#     "http://www.aljazeera.com",
#     "http://indianexpress.com",
#     "http://www.amadershomoy.com/",
#     "https://www.thedailystar.net/bangla/",
#     "https://bangla.dhakatribune.com/",
#     "http://www.jjdin.com/",
#     "http://www.prothomalo.com/",
#     "http://www.mzamin.com/",
#     "http://www.kalerkantho.com/",
#     "http://www.ittefaq.com.bd/",
#     "http://www.bd-pratidin.com/",
#     "https://samakal.com/",
#     "https://www.ajkerpatrika.com/",
#     "https://kalbela.com/",
#     "http://www.dailyinqilab.com/",
#     "https://www.dailyjanakantha.com/",
#     "https://www.deshrupantor.com/epaper/",
#     "https://www.thedailystar.net",
#     "https://en.prothomalo.com/",
#     "https://www.observerbd.com/",
#     "https://bdnews24.com/",
#     "https://thefinancialexpress.com.bd/",
#     "https://www.daily-sun.com/",
#     "https://www.dhakatribune.com/",
#     "https://unb.com.bd/",
#     "https://en.ntvbd.com/",
#     "https://www.tbsnews.net/",
#     "https://www.banglanews24.com/english/",
#     "https://www.ajkerpatrika.com/",
#     "https://www.deshrupantor.com/",
#     "https://www.bd-journal.com/",
#     "https://www.dailyjanakantha.com/",
#     "https://bonikbarta.net/"
# ]

# base = 'https://www.google.com/search?q='
# query = 'obaidul kader'
# domain_list = ' OR '.join([f"site:{domain}" for domain in domains])

# search_query = base+query+'('+domain_list+')'
# print(search_query)
# random_proxy = random.choice(proxy_ips)
# # random_proxy = proxy_ips[0]
# proxy = f'http://{random_proxy}'
# print(proxy)
# try:
#     links = search(search_query, proxy=proxy, advanced= True, num_results=5, timeout=10)
#     for link in links:
#         url = link.url
#         print(url)
        


# except Exception as e:
#     print(e)