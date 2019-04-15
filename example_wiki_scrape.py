from bs4 import BeautifulSoup
import requests
from gensim.summarization import summarize

def read_plot(title):
    url = 'https://en.wikipedia.org/wiki/{}'.format(title)
    response = requests.get(url)
    full_text = ''
    soup = BeautifulSoup(response.content, 'html.parser')
    for header in soup.find_all('h2'):
        if len(header.find_all('span', text='Plot')) != 0:
            paragraphs = header.find_next_siblings('p', limit=10)
            for p in paragraphs:
                full_text += ('\n'+ p.text)
    print('Complete Text: ' + '\n' + full_text +'\n\n')
    return full_text
input_text = read_plot('Moby-Dick')
print('Summarized Text: \n' + summarize(input_text))