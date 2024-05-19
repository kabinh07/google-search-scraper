import requests
import threading
import random
import queue

class IPValid():
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.valid_ips = []
        self.thread_list = []
        with open(self.input_dir, 'r') as f:
            self.proxies = f.read().split('\n')
        self.ip_segments = []

    def divide_ips(self):
        segment = []
        for idx, ip in enumerate(self.proxies):
            segment.append(ip)
            if (idx+1)%10 == 0:
                self.ip_segments.append(segment)
                segment = []

    def check_ip(self, ip):
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
        url = 'https://www.google.com/'
        response = requests.get(url=url, proxies={'http':ip,'https':ip}, headers= user_agent, timeout=2)
        try:
            if response.status_code == 200:
                self.valid_ips.append(ip)
                print()
                print(f"{ip} inserted")
                print()
            else:
                print(f"Error {response.status_code}")
        except:
            pass
    
    def thread_method(self):
        for ip_segment in self.ip_segments:
            q = queue.Queue()
            for ip in ip_segment:
                q.put(ip)
            while not q.empty():
                ip = q.get()
                thread = threading.Thread(target = self.check_ip, args= (ip, ))
                print(ip)
                thread.start()
                self.thread_list.append(thread)
                
            for thread in self.thread_list:
                thread.join()
    
    def start(self):
        self.divide_ips()
        self.thread_method()
        with open(self.output_dir, 'w') as f:
            print(self.valid_ips)
            ips = '\n'.join(self.valid_ips)
            f.write(ips)

