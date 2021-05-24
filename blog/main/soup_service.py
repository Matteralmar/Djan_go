import requests
from bs4 import BeautifulSoup


def soup_service(links, soup, titles):
    for link in soup.find_all('div', attrs={'class': "txt"}):
        link = link.a['href']
        links.append(link)
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_title = soup.find("h1", {"itemprop": "headline"})
        try:
            article_t = article_title.text
        except Exception:
            continue
        print(article_t)
        titles.append(article_t)
        article_title.text.strip()
        article_content = soup.find("div", {"class": "content"})
    print(titles)