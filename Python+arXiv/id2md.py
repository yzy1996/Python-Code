from urllib import request
import re
import feedparser
from pathlib import Path

p = Path(__file__)

with open(p.parents[0] / 'conf_list.txt', 'r') as f:
    data = f.read()
CONF = data.split('\n')
CONF = '|'.join(CONF)

class Information():
    '''
    extract information from arxiv api
    '''    
    
    def __init__(self, query_id) -> None:

        query_url = f'http://export.arxiv.org/api/query?id_list={query_id}'
        export_arxiv = request.urlopen(query_url).read().decode('utf-8')
        feed = feedparser.parse(export_arxiv)

        self.title = re.sub(r'[^\w\s-]', '', feed.entries[0].title)
        self.authors = [author.name for author in feed.entries[0].authors]
        self.abs_url_version = feed.entries[0].id
        self.abs_url = self.abs_url_version[:-2]
        self.pdf_url = self.abs_url.replace('abs', 'pdf')
        self.id_version = self.abs_url_version[-12:]
        self.year = feed.entries[0].published[:4]
        self.summary = feed.entries[0].summary

        try:
            self.comment = feed.entries[0].arxiv_comment
            publish = re.findall(rf'[\s\S]*(({CONF}).*?\d{{4}})[\s\S]*', self.comment)
            print(publish[0][0])
            self.publish = re.sub(r'\W*(\d{4})', r' \1', publish[0][0]) if publish else f'arXiv {self.year}'
        except:
            self.publish = f'arXiv {self.year}'

    def write_notes(self):
        '''
        define the markdown format and write notes
        '''

        title_url = f'[{self.title}]({self.abs_url})  '
        publish = f'**[`{self.publish}`]**'
        authors = ', '.join(self.authors)
        authors = f'*{authors}*'

        print('-', title_url)
        print(' ', publish, authors)

if __name__ == "__main__":

    while True:
        id = input("type id: ")

        # 2011.13126 2210.08823
        if re.findall(r'\d{4}\.\d{5}', id):

            information = Information(id)
            information.write_notes()
        
        # >>>
        # - [Lifting 2D StyleGAN for 3D-Aware Face Generation](http://arxiv.org/abs/2011.13126v2)  
        #   **[`CVPR 2021`]** *Yichun Shi, Divyansh Aggarwal, Anil K. Jain*