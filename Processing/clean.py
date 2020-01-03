import os
import re
from bs4 import BeautifulSoup

directory = './hasil/';
index = 0
for file in os.listdir(directory):
    with open(directory+file, 'r') as f:
        html = BeautifulSoup(f.read(), "lxml")
        html_text = html.find("div", {"id": "detikdetailtext"})

        if(not html_text):
            continue

        title = html.find("title").text
        desc = html.find("meta", {"name" : "description"})
        desc = desc["content"] if desc else "No Description"
        url = html.find("meta", {"property" : "og:url"})
        url = url["content"] if url else "/"

        trash = html_text.find('center')
        if(trash):
            trash.decompose()

        tags = html_text.find('div', {"class": "detail_tag"})
        if(tags):
            tags.decompose()

        clean_text = re.sub(r'\s+', ' ', html_text.text)
        index += 1

        print(index, title)
        with open('./clean/'+str(index)+'.txt', 'w') as out:
            out.write(title+'\n'+desc+'\n'+clean_text+'\n'+url)
