# -*- coding: utf-8 -*-

import urllib2
import bs4
from urlparse import urljoin

stopwords = set(
    ['the', 'of', 'a', 'an', 'this', 'that', 'I', 'is', 'to', 'and', 'in', 'it'])


class crawler:

    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbCommit():
        pass

    def getEntryId(self, table, field, valuer, createnew=True):
        return None

    def addToIndex(self, url, soup):
        print 'Indexing %s' % url

    def getTextOnly(self, soup):
        return None

    def separateWords(self, text):
        return None

    def isIndexed(self, url):
        return False

    def addLinkRef(self, urlFrom, urlTo, linkText):
        pass

    def crawl(self, pages, depth=2):
        for x in xrange(depth):
            newpages = set()
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print "Page %s couldn't open" % page
                    continue
                soup = bs4.BeautifulSoup(c.read())
                self.addToIndex(page, soup)
                # 返回页面里的所有tag
                links = soup('a')
                for link in links:
                	# href 是指链接的网址
                    if('href' in dict(link.attrs)):
                        url = urljoin(page, link['href'])
                        if(url.find("'") != -1): 
                            continue
                        url = url.split('#')[0]
                    if url[0:4] == "http" and not self.isIndexed(url):
                        newpages.add(url)
                    linkText = self.getTextOnly(link)
                    self.addLinkRef(page, url, linkText)
                self.dbCommit()
            pages = newpages # 再一次的for循环中使用新的pages，就是我们这一次获取的这些新的页面
                             # 感觉这种写法灰常好

    def createIndexTables(self):
        pass
c = urllib2.urlopen('http://www.baike.baidu.com/ziran')
soup = bs4.BeautifulSoup(c.read(), 'html.parser')
print type(soup.a)

uu = urljoin("http://www.baidu.com/adha.html","ccc.html")
print uu.find("'")
