# -*- coding: utf-8 -*-

# Importing Packages
import sys, logging
from apscheduler.scheduler import Scheduler
sys.path.append("\\Users\\Steve Martin\\Documents\\Personal\\Python Scripts\\Crawler\\")
import spider_library as sl

#Configure Parameters
pageUrl = 'https://www.wikipedia.org/'

#Define Main
def main(Url):
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='\\Users\\Steve Martin\\Documents\\Personal\\Python Scripts\\Crawler\\Logs\\spider.log', level=logging.DEBUG)
    sl.scrape_sites(Url)



# Create two threads as follows
# =============================================================================
# try:
#    _thread.start_new_thread(scrape_multi_site, ('Thread 1', '/wiki/Kevin_Bacon',))
#    _thread.start_new_thread(scrape_multi_site, ('Thread 2', '/wiki/Monty_Python',))
# except:
#    print ('Error: unable to start threads')
# 
# while 1:
#     pass
# =============================================================================

# =============================================================================
# session = requests.Session()
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
#            'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
#            'Accept':'text/html,application/xhtml+xml,application/xml;'
#            'q=0.9,image/webp,*/*;q=0.8'}
# url = ''
# req = session.get(url, headers=headers)
# =============================================================================
