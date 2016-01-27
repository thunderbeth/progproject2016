import urllib.request
import re
from lxml import etree

text_output = open('output.txt', 'w', encoding = 'utf-8')
homepage = urllib.request.urlopen('http://tema.livejournal.com/2015/')
homepage_text = homepage.read().decode('utf-8')

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']


for i in month:
    result = re.findall ('http://tema.livejournal.com/2015/'+ i + '/[0-9]+', homepage_text)
    for j in result:
        postpage = urllib.request.urlopen(j)
        stringpostpage=postpage.read()
        print(stringpostpage)
        tree = etree.HTML(stringpostpage)
        for i in tree.xpath('//*[@class="subject"]'):
            print (i)
        