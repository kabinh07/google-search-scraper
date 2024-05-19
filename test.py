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

