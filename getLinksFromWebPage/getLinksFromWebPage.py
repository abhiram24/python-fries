import requests
import re

fw = file('output_links.txt','wb')

#Put in your url list here
urlsList = ['http://www.techcrunch.com','http://www.qz.com']

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}

for url in urlsList:
    r = requests.get(url.strip(),headers=headers)
    html = r.text

    links = re.findall('"((http)s?://.*?)"', html)
    for j in links:
        result = j[0]
        param = url.split('www.')[1]
        if result.find(param) != -1:
            fw.write(result +'\n')
            print result

fw.close()

# Remove duplicate URLs from file
lines = open('output_links.txt', 'rb').readlines()
lines_set = set(lines)

out = open('output_links.txt', 'wb')

for line in lines_set:
    out.write(line)

out.close()



