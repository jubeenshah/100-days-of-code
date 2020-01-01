import collections
import re

def mostCommonWord(paragraph, banned):
    paragraph = paragraph.lower()
    paragraph = re.sub(r'[^\w\s]',' ',paragraph)
    maxCounter = dict(collections.Counter(paragraph.split(" ")))
    maxCounter = sorted(maxCounter.items(), key= lambda lv : lv[1],reverse=True)
    for eachItem in maxCounter:
        if eachItem[0] in banned or eachItem[0]=="":
            continue
        else:
            return eachItem[0]
    

mostCommonWord("Bob. hIt, baLl", ["bob", "hit"])