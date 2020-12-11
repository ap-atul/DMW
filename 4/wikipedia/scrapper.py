from urllib.request import urlopen

from bs4 import BeautifulSoup as BS
from joblib import dump, load
from tqdm import tqdm
import re


def getAllLinks():
    # 3795 links stored
    url = ["https://mr.wikipedia.org/w/index.php?title=%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%87%E0%A4%B7:%E0%A4%B8%E0%A4%B0"
           "%E0%A5%8D%E0%A4%B5_%E0%A4%AA%E0%A4%BE%E0%A4%A8%E0%A5%87&from=%E0%A4%85%E0%A4%81%E0%A4%9C%E0%A5%87%E0%A4"
           "%B2%E0%A4%BF%E0%A4%95+%E0%A4%95%E0%A4%B0%E0%A5%8D%E0%A4%AC%E0%A4%B0"]
    homeURL = 'https://mr.wikipedia.org'

    allLinks = []
    DATA_LEN = 10
    counter = 0
    for link in url:
        while link:
            if counter > DATA_LEN:
                break
            htmlDoc = ''
            with urlopen(link) as response:
                for line in tqdm(response):
                    line = line.decode('utf-8')
                    htmlDoc = htmlDoc + line.replace('\n', '')
                soup = BS(htmlDoc, 'html.parser')
                div = soup.find('div', {'class': 'mw-allpages-body'})
                if div:
                    anchors = div.find_all('a')
                    allLinks = allLinks + [homeURL + anchor['href'] for anchor in anchors]
                navDiv = soup.find('div', {'class': 'mw-allpages-nav'})
                if navDiv and len(navDiv.find_all('a')) == 2:
                    link = homeURL + navDiv.find_all('a')[1]['href']
            counter += 1
        dump(allLinks, "storage/allLink.joblib")
    print(len(allLinks))
    print("Done..............................")


def getAllArticlesFromTheLink():
    # read 851 links only
    allLinks = load("storage/allLink.joblib")
    PATH = "storage/articles/"
    allLinks = allLinks[451:]
    for i in tqdm(range(451, 3795)):
        counter = i
        link = allLinks[i]
        htmlDoc = ""
        with urlopen(link) as response:
            for line in response:
                line = line.decode('utf-8')
                htmlDoc = htmlDoc + line.replace('\n', '')
            soup = BS(htmlDoc, 'html.parser')
            paras = soup.find_all('p')
            article = ""
            for para in paras:
                article = article + para.text + "\n"

            article = re.sub(r'\([^)]*\)', r'', article)
            article = re.sub(r'\[[^\]]*\]', r'', article)
            article = re.sub(r'<[^>]*>', r'', article)
            article = re.sub(r'^https?:\/\/.*[\r\n]*', r'', article)
            article = article.replace(u'\ufeff', '')
            article = article.replace(u'\xa0', u'')
            article = article.replace('  ', ' ')
            article = article.replace(' , ', ', ')

            fileName = PATH + str(counter) + '.joblib'
            dump(article, fileName)
            # print(f"{fileName} created with {len(article)} words")


getAllArticlesFromTheLink()
