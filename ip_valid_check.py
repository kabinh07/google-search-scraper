import requests
import queue
import threading

with open('data/scraped_ips.txt', 'r') as f:
    ip_list = f.read().split('\n')
q = queue.Queue()
for ip in ip_list:
    q.put(ip)
url = 'https://www.google.com/'
valid_ips = []
def check_ip():
    while not q.empty():
        ip = q.get()
        response = requests.get(url = url, proxies={'http':ip, 'https': ip}, timeout=5)
        if response.status_code == 200:
            valid_ips.append()
            print(ip)
        print(valid_ips)

for _ in range(10):
    threading.Thread(target=check_ip).start()