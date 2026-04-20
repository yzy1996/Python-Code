from urllib import request
import re
from pathlib import Path
from pypdf import PdfReader
import feedparser

p = Path(__file__)

with open(p.parents[0] / 'conf_list.txt', 'r') as f:
    data = f.read()
CONF = data.split('\n')
CONF = '|'.join(CONF)

class Information():
    def __init__(self, query_title) -> None:

        query_id = read_pdf(query_title)

        if query_id and re.fullmatch(r'\d{4}\.\d{5}', query_id):
            query_url = f'http://export.arxiv.org/api/query?id_list={query_id}'
        else:
            query_title1 = Path(query_title).stem.replace(' ', '+').replace('-', '+')
            query_url = f'https://export.arxiv.org/api/query?search_query=ti:{query_title1}&max_results=1'

        self.query_url = query_url
        export_arxiv = request.urlopen(self.query_url).read().decode('utf-8')
        feed = feedparser.parse(export_arxiv)
        if not feed.entries:
            raise ValueError(f'No arXiv entry found for {query_title}')

        self.title = re.sub(r'[^\w\s-]', '', feed.entries[0].title)
        self.authors = [author.name for author in feed.entries[0].authors]
        self.abs_url_version = feed.entries[0].id
        self.abs_url = self.abs_url_version[:-2]
        self.pdf_url = self.abs_url.replace('abs', 'pdf')
        self.id_version = self.abs_url_version[-12:]
        self.year = feed.entries[0].published[:4]
        self.summary = feed.entries[0].summary

        try: # try for no attribute 'arxiv_comment'
            self.comment = feed.entries[0].arxiv_comment
            self.conf = re.findall(rf'({CONF})', self.comment)[0]
            self.conf_year = re.findall(r'(\d{4})', self.comment)[0]
            self.publish = f'{self.conf} {self.conf_year}' if self.conf else f'arXiv {self.year}'
        except (AttributeError, IndexError):
            self.publish = f'arXiv {self.year}'

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
        first_page_text = first_page.extract_text() or ''
        id_match = re.search(r'(\d{4}\.\d{5})(?:v\d+)?', first_page_text)
        if id_match:
            return id_match.group(1)

    return None


if __name__ == "__main__":

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('*.pdf'))

    for file in list(pdf_list):
        try:
            information = Information(query_title=file)
            information.write_notes()

        except Exception as ex:
            print(f'Error in file2md for {file}: {ex}')
