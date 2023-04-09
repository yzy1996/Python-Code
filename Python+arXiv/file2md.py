from urllib import request
import re
from pathlib import Path
from PyPDF2 import PdfReader
import feedparser

CONF = 'ICML|NIPS|NeurIPS|ICLR|CVPR|ICCV|ECCV|AAAI|IJCAI|3DV|UAI|WACV|ICASSP|ICRA'


class Information():
    def __init__(self, query_title) -> None:

        query_id = read_pdf(query_title)

        if re.findall(r'\d{4}.\d{5}', query_id):
            query_url = f'http://export.arxiv.org/api/query?id_list={query_id}'

        else:
            query_title1 = str(query_title)[:-4].replace(' ', '+').replace('-', '+')
            self.query_url = f'https://export.arxiv.org/api/query?search_query=ti:{query_title1}&max_results=1'

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

        title_url = f'[{self.title}]({self.abs_url})  '
        publish = f'**[`{self.publish}`]**'
        authors = ', '.join(self.authors)
        authors = f'*{authors}*'

        print('-', title_url)
        print(' ', publish, authors, '\n')


def read_pdf(filename, update=False):
    '''
    read pdf and return id
    '''

    with open(filename, 'rb') as f:

        pdf = PdfReader(f)

        first_page = pdf.pages[0]
        text_split = first_page.extract_text().split()
        str_id = text_split[-5]
        id_version_local = re.findall(r'\d{4}\.\d{5}v\d{1}', str_id)[0]
        id = id_version_local[:-2]

    return id


if __name__ == "__main__":

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('*.pdf'))

    for file in list(pdf_list):
        try:
            information = Information(query_title=file)
            information.write_notes()

        except Exception as ex:
            print('Error: ', ex)
            pass
