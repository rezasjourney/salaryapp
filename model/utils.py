from string import punctuation
import re

def clean(description):
    description = description.lower()
    description = re.sub('[0-9]+\S+|\s\d+\s|\w+[0-9]+|\w+[\*]+.*|\s[\*]+\s|www\.[^\s]+', '', description)
    
    for p in punctuation:
        description = description.replace(p, '')
    
    description = re.sub('\n', '', description)
    
    return description