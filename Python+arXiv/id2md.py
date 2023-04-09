from urllib import request
import re
import feedparser

CONF = 'ICML|NIPS|NeurIPS|ICLR|CVPR|ICCV|ECCV|AAAI|IJCAI|3DV|UAI|WACV|ICASSP|ICRA'


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
        self.abs_url = feed.entries[0].id
        self.pdf_url = self.abs_url.replace('abs', 'pdf')
        self.id_version = self.abs_url[-12:]
        self.year = feed.entries[0].published[:4]
        self.summary = feed.entries[0].summary

        try:
            self.comment = feed.entries[0].arxiv_comment
            publish = re.findall(rf'[\s\S]*(({CONF}).*?\d{{4}})[\s\S]*', self.comment)
            self.publish = re.sub(r'(\w)(\d{4})', r'\1 \2', publish[0][0]) if publish else f'arXiv {self.year}'
        except:
            self.publish = f'arXiv {self.year}'
            pass

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

        # 2011.13126
        if re.findall(r'\d{4}\.\d{5}', id):

            information = Information(id)
            information.write_notes()
