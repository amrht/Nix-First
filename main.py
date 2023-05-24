import requests
from bs4 import BeautifulSoup
import re

def scrape_wikipedia(query):
    # Format the query to be used in the Wikipedia URL
    formatted_query = query.replace(' ', '_')
    url = f"https://en.wikipedia.org/wiki/{formatted_query}"

    # Send a GET request to the Wikipedia URL
    response = requests.get(url)
    
    # Make a soup 
    soup = BeautifulSoup(response.text,'lxml')
    soup

    # Extract the plain text content from paragraphs
    paras = []
    for paragraph in soup.find_all('p'):
        paras.append(str(paragraph.text))

    # Extract text from paragraph headers
    heads = []
    for head in soup.find_all('span', attrs={'mw-headline'}):
        heads.append(str(head.text))

    # Interleave paragraphs & headers
    text = [val for pair in zip(paras, heads) for val in pair]
    text = ' '.join(text)

    # Drop footnote superscripts in brackets
    text = re.sub(r"\[.*?\]+", '', text)

    # Replace '\n' (a new line) with '' and end the string at $1000.
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
