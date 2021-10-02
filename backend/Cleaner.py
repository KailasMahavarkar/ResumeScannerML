import re
import string
import random

def NameGenerator(length: int = 6, extension: str = 'pdf') -> str:
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(length)]) + '.' + extension

def CleanResume(doc):
    #Remove newlines
    doc = re.sub('[\r\t\n]+', ' ', doc)
    #Remove URls
    doc = re.sub('http\S+\s*', ' ', doc)
    #Remove RT and cc
    doc = re.sub('RT|cc',' ',doc)
    #Remove hashtags
    doc = re.sub('#\S+',' ',doc)
    #Remove Mentions
    doc = re.sub('@\S+', ' ', doc)
    #Remove Punctuations
    doc = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ',doc)
    doc = re.sub(r'[^\x00-\x7f]',r' ', doc) 
    #remove white spaces
    doc = re.sub('\s+', ' ', doc)
    return doc.strip()