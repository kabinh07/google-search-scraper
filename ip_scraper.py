from bs4 import BeautifulSoup
import requests

class IPScraper():
    def __init__(self):
        self.url1 = 'https://free-proxy-list.net/'
        self.url2 = 'https://proxyscrape.com/free-proxy-list'

    def scrape(self):
        ip_addresses = []
        response = requests.get(self.url1)
        if response.status_code == 200:   
            try:
                soup = BeautifulSoup(response.content, 'html.parser')
                div = soup.find('div', class_ = 'fpl-list')
                table = div.find('table', class_ = 'table-striped')
                rows = table.find_all('tr')
                
                for row in rows:
                    for idx, data in enumerate(row):
                        if idx == 0:
                            ip_addresses.append(data.text)

            except Exception as e:
                print(f'Exception: {e}')


            with open('data/scraped_ips.txt', 'w') as f:
                ips = '\n'.join(ip_addresses[1:-1])
                f.write(ips)
        





