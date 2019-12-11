from SimpleFileWriter import SimpleFileWriter
from SaveHandler import SaveHandler
from SimpleCrawler import SimpleCrawler
import os

#SETTINGS
CWD = os.getcwd()
WEBPAGES_DIR = os.path.join(CWD, "WebPages")
SAVEFILE_NAME = os.path.join(CWD, "crawler_save")
SEED = "https://www.google.com/"
LIMIT = 30

def createDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    createDir(WEBPAGES_DIR)
    fwriter = SimpleFileWriter(WEBPAGES_DIR)
    saveHandler = SaveHandler(SAVEFILE_NAME)
    crawler = SimpleCrawler(SEED, fwriter, saveHandler)
    crawler.startCrawl(LIMIT)

if __name__ == "__main__":
    main()
