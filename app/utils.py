import urllib.request
import html2text
from string import punctuation
import re

def extract_text(url):
    response = urllib.request.urlopen(url)
    html = response.read()

    h = html2text.HTML2Text()
    h.ignore_links = True

    description = h.handle(html.decode('utf-8'))
    
    return description

def clean_text(description):
    description = description.lower()
    description = re.sub('[0-9]+\S+|\s\d+\s|\w+[0-9]+|\w+[\*]+.*|\s[\*]+\s|www\.[^\s]+', '', description)
    
    for p in punctuation:
        description = description.replace(p, '')
    
    description = re.sub('\n', '', description)
    
    return description