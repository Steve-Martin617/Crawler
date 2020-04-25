# -*- coding: utf-8 -*-

#Importing Packages
import logging
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Defining Functions in Package
def getLinks(pageUrl):
    """
    Scraping all links on the input webpage. Status: working
    """
    logging.info('Opening URL for links')
    html = urlopen(pageUrl)
    logging.info('Parsing HTML for links')
    bs = BeautifulSoup(html, 'html.parser')
    logging.info('Identifying Links')
    site_links = bs.find_all('a')
    return site_links

def getText(pageUrl):
    """
    Scraping all text on the input webpage. Status: working
    """
    logging.info('Opening URL for text')
    html = urlopen(pageUrl)
    logging.info('Parsing HTML for text')
    bs = BeautifulSoup(html, 'html.parser')
    logging.info('Identifying Text')
    site_text = bs.get_text()
    return site_text

def getTitle(pageUrl):
    """
    Scraping the title on the input webpage. Status: working
    """
    logging.info('Opening URL for titles')
    html = urlopen(pageUrl)
    logging.info('Parsing HTML for titles')
    bs = BeautifulSoup(html, 'html.parser')
    logging.info('Identifying Titles')
    site_title = bs.find('h1').get_text()
    return site_title

def getParagraphs(pageUrl):
    """
    Scraping the paragraphs on the input webpage. Status: working
    """
    logging.info('Opening URL for paragraphs')
    html = urlopen(pageUrl)
    logging.info('Parsing HTML for paragraphs')
    bs = BeautifulSoup(html, 'html.parser')
    logging.info('Identifying Paragraphs')
    site_paragraph = ''
    article = bs.find("div", {"class":"story-body__inner"}).findAll('p')
    for element in article:
        site_paragraph += '\n' + ''.join(element.findAll(text = True))
    return site_paragraph

def scrape_sites(pageUrl, LogFile):
    """
    Holistic scraper of titles, links, text and paragraphs looping through all connected webpages. Status: working
    """
    global links, text, title
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=log_file_location, level=logging.DEBUG)
    logging.info('Start Title Extraction')
    title = getTitle()
    logging.info('End Title Extraction')
    time.sleep(1)
    logging.info('Start Text Extraction')
    text = getText()
    logging.info('End Text Extraction')
    time.sleep(1)
    logging.info('Start Link Extraction')
    links = getLinks()
    logging.info('End Link Extraction')
    time.sleep(1)
    logging.info('Start Paragraph Extraction')
    paragraphs = getParagraphs()
    logging.info('End Paragraph Extraction')
    time.sleep(1)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        scrape_single_site(newArticle)
    return title, links, paragraphs, text
