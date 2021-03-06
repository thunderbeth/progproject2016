import urllib.request
import re
from bs4 import BeautifulSoup
import os
from os import path
import nltk
import json
homepage = urllib.request.urlopen('http://dolboeb.livejournal.com/2012/')
homepage_text = homepage.read().decode('utf-8')

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
def pauk_texts(link):
    for i in month:
        result = re.findall (link + i + '/[0-9]+', homepage_text)
        text_output = open(i + '.txt', 'w', encoding = 'utf-8')
        for j in result:
            postpage = urllib.request.urlopen(j)
            stringpostpage=postpage.read()
            soup = BeautifulSoup(stringpostpage, "lxml")
            texts = soup.findAll('td',class_ ='entry')
            for i in texts:
                cleantext = BeautifulSoup.get_text(i, separator=u' ')
                cleantext = re.sub('Tags:.*?Share','',cleantext)
                text_output.write(cleantext)
        text_output.close()
        
        
def ListToFreqDict(wordlist):
	wordfreq = [wordlist.count(p) for p in wordlist]
	freqmetric = [x  for x in wordfreq]
	perem = zip(wordlist,freqmetric)
	perem = list(set(perem))
	return perem
def sortFreqDict(freqdict):
	aux = sorted(freqdict,key=(lambda item: item[1]), reverse=True)
	#aux = sorted(aux,key=lambda item: item[0])
	return aux
def bigrammer(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.txt'):
            print(os.listdir(folder))
            print('Starting file parsing...')
            file_path = path.relpath(folder+'/'+filename)
            with open(file_path, encoding='utf-8') as f:
                content = f.read().lower()
                content = re.sub('[^а-яё\ \']+', " ", content)
                words = list(content.split())
                biwords = nltk.bigrams(words)
                bifreq = ListToFreqDict(list(biwords))
                bisortfreq = sortFreqDict(bifreq)[:1000]
                with open(filename+'data.json', 'w') as fp:
                    json.dump(bisortfreq, fp)
                #text_output2 = open(filename+'_bigramy.txt', 'w', encoding='utf-8')
                #for bisortfr in bisortfreq:
                #    text_output2.write(str(bisortfr) + '\n')
                #text_output2.close()
                #f.close()
                print('Bigrams ready')
                
#pauk_texts('http://dolboeb.livejournal.com/2012/')
bigrammer('un_N')
 # словарик второго файла, ищи что хочешь
# если будет пытаться ругаться то конвертируй item'ы в строки, - str() - должно перестать
# теперь скрещивай эти словарики двух файлов как тебе угодно и тащи что тебе угодно
#json_example(01.txtdata.json)