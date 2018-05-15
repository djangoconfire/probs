'''
Author  : RituRaj 
Date    : May 15, 2018 
'''

import requests
from bs4 import BeautifulSoup
import sys

class Scrape:
    KW = ""
    PG = 0
    query1 = "http://www.shopping.com/products~PG-"
    query2 = 'http://www.shopping.com/products?KW='

    def __init__(self,kw="",pg=0):
        self.KW = kw
        self.PG = pg

    def getAllResults(self,keyword, page):
        """
        :param self - class instance
        :param keyword - keyword , say Tshirt
        :param page - page Number
        :return - all results for a given keywords on a specified page.
        """
        url = self.query1 + page + "?KW=" + keyword
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        elementid = 1
        while 1:
            value = soup.findAll('', {'id': 'nameQA' + str(elementid)})
            if value:
                print value[0].get('title')
                print soup.findAll('span', {'id': 'priceClickableQA' + str(elementid)})[0].text
            else:
                print "Sorry, There were no matches for your search " + keyword + " on page number" + page
            elementid += 1
            if not soup.findAll('', {'id': 'nameQA' + str(elementid)}):
                break
        return soup


    def countResults(self,keyword):
        """
        :param self - class instance
        :param keyword - keyword - say , Tshirt
        :return total number of results for a input keyword
        """
        url = self.query2 + keyword
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        value = soup.findAll('span', {'class': 'numTotalResults'})
        if value:
            return soup.findAll('span', {'class': 'numTotalResults'})[0].text.split('of')[1]
        else:
            return "No result"


scraper = Scrape()
try:
    if len(sys.argv) == 2:
        print scraper.countResults(sys.argv[1])
    if len(sys.argv) == 3:
        scraper.getAllResults(sys.argv[1], sys.argv[2])
except:
    print "Invalid input"