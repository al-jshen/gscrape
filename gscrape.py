from requests import get
from bs4 import BeautifulSoup as bs
from string import punctuation
from collections import Counter
from nltk.corpus import stopwords

query = input().lower()
search = query.replace(' ', '+')
resp = get(f'https://www.google.com/search?q={search}').text

soup = bs(resp, 'html.parser')
for script in soup(['script', 'style']):
    script.decompose()

text = soup.get_text().lower()
cleaned = ''.join([c for c in text if c not in punctuation])

stop = set(stopwords.words('english'))
words = cleaned.split()

filtered = [w for w in words if w not in stop]

keywords1 = query.split()
keywords2 = ['searchsearch']
keywords = keywords1 + keywords2

count = Counter(filtered)
for keywd in keywords:
    del count[keywd]

for i in count.most_common(20):
    print(i[0], i[1])
