from ip_scraper import IPScraper
from ip_validation import IPValid

scraper = IPScraper()
valid = IPValid(input_dir = 'data/scraped_ips.txt', output_dir='data/valid_ips.txt')
scraper.scrape()
valid.start()