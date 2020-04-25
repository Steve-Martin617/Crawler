# -*- coding: utf-8 -*-

# Importing Packages
import sys, logging
from apscheduler.scheduler import Schedulera
sys.path.append("\\Users\\Steve Martin\\Documents\\Personal\\Python Scripts\\Crawler\\")
import spider_library as sl

#Configure Parameters
Url = 'https://www.wikipedia.org/'
log_file_location = "\\Users\\Steve Martin\\Documents\\Personal\\Python Scripts\\Crawler\\Logs\\spider.log"
output_location = "\\Users\\Steve Martin\\Documents\\Personal\\Python Scripts\\Crawler\\Output\\"

#Define Main
def main(pageUrl, LogLocation, OutputLocation):
    sl.scrape_sites(pageUrl, LogLocation)
    title.to_csv('title_output.csv',output_location)
    links.to_csv('links_output.csv',output_location)
    paragraph.to_csv('paragraph_output.csv',output_location)
    text.to_csv('text_output.csv',output_location)

main(Url,log_file_location,output_location)
