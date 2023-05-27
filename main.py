import requests
from bs4 import BeautifulSoup
import re

def scrape_wikipedia(query):
    formatted_query = query.replace(' ', '_')
    url = f"https://en.wikipedia.org/wiki/{formatted_query}"

    response = requests.get(url)
    
    soup = BeautifulSoup(response.text,'lxml')
    soup

    paras = []
    for paragraph in soup.find_all('p'):
        paras.append(str(paragraph.text))

    heads = []
    for head in soup.find_all('span', attrs={'mw-headline'}):
        heads.append(str(head.text))

    text = [val for pair in zip(paras, heads) for val in pair]
    text = ' '.join(text)

    text = re.sub(r"\[.*?\]+", '', text)

    text = text.replace('\n', '')[:-11]
    print(text,"\n\n")
    links = (
    soup
    .select_one("#See_also")
    .parent
    .find_next_sibling("div")
    .find_all("a", href=True)
    )
    print([x["href"] for x in links])
a=input("Enter Wikipedia search: ")
print(scrape_wikipedia(a))
