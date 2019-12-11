from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import urllib
import time
import re

class SimpleCrawler:
    def __init__(self, seed, fwriter, saveHandler, frontier = [], visited = set()):
        self.fwriter = fwriter
        self.saveHandler = saveHandler
        if(self.saveHandler.hasSavedData()):
            self.__load()
        else:
            self.frontier = [seed];
            self.visited = set()

    def __save(self):
        self.saveHandler.dump((self.frontier, self.visited))

    def __load(self):
        self.frontier, self.visited = self.saveHandler.load()

    def getWebPage(self, url):
        return urlopen(url)

    def getLinks(self, htmlPage):
        links = re.findall('"((http|ftp)s?://.*?)"', htmlPage)
        links = [i[0] for i in links]
        return links

    def isText(self, response):
        return response.info().get_content_maintype() == 'text';

    def saveHtml(self, htmlPage):
        bs = BeautifulSoup(htmlPage, features = "html.parser")
        try:
            title = bs.title.text
            title = re.sub('[^\w\-_\. ]', '_', title)
            self.fwriter.write(title + ".html", htmlPage)
            return True
        except:
            return False

    def addToFrontier(self, links):
        for link in links:
            if link not in self.visited and link not in self.frontier and self.validLink(link):
                self.frontier.append(link)

    def validLink(self, link):
        '''Defines the filter for links when adding to frontier.

        Currently filters out queries, images, css, and js files
        '''
        if ".css" in link or ".jpg" in link or ".png" in link or ".js" in link:
            return False
        return '?' not in link

    def startCrawl(self, limit):
        while(len(self.visited) < limit):
            next_url = self.frontier[0]
            print("Visiting " + next_url + "...")
            try:
                response = self.getWebPage(next_url)
                if self.isText(response):
                    htmlPage = response.read().decode(response.headers.get_content_charset())
                    links = self.getLinks(htmlPage)
                    self.addToFrontier(links)
                    if self.saveHtml(htmlPage):
                        self.visited.add(next_url)
                        print("Saved document.")
                    else:
                        print("Document not saved.")
                else:
                    print("Content type is not text.")
            except urllib.error.HTTPError as e:
                print("Invalid response code {}... Moving on to next url".format(e.code))
            except Exception as e:
                print(e)
            self.frontier = self.frontier[1:]
            self.__save()
            time.sleep(5)
