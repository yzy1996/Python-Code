import re
from urllib import request
from pathlib import Path
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

    def __init__(self, query_id=None, query_title=None) -> None:

        if query_id:
            query_url = f'http://export.arxiv.org/api/query?id_list={query_id}'
        elif query_title:
            query_title1 = str(query_title)[:-4].replace(' ', '+').replace('-', '+')
            query_url = f'https://export.arxiv.org/api/query?search_query=ti:{query_title1}&max_results=1'

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

        try: # try for no attribute 'arxiv_comment'
            self.comment = feed.entries[0].arxiv_comment
            self.conf = re.findall(rf'({CONF})', self.comment)[0]
            self.conf_year = re.findall(r'(\d{4})', self.comment)[0]
            self.publish = f'{self.conf} {self.conf_year}' if self.conf else f'arXiv {self.year}'
        except:
            self.publish = f'arXiv {self.year}'

        # self.project_urls = URLExtract().find_urls(self.summary) if self.comment else None

    # deprecated
    def _get_arxiv_info_regex(self):

        Id = r'<id>http://arxiv.org/abs/(.*)</id>'
        Title = r'<title>([\s\S]*)</title>'  # 有时候名字太长了，会换行
        Authors = r'<author>\s*<name>(.*)</name>\s*</author>'
        Year = r'<published>(\d{4}).*</published>'
        Publish = rf'<arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">[\s\S]*(({CONF}).*?\d{{4}})[\s\S]*</arxiv:comment>'

        id_version = re.findall(Id, self.export_arxiv)[0]
        id = id_version[0:-2]

        title = re.findall(Title, self.export_arxiv)[0]
        title = re.sub(r'\n\s', '', title)  # 去掉换行
        title_sub = re.sub(r'[^\w\s-]', '', title)  # 去掉标点

        authors = re.findall(Authors, self.export_arxiv)

        year = re.findall(Year, self.export_arxiv)[0]

        self.id_version = id_version
        self.id = id
        self.title = title
        self.title_sub = title_sub
        self.authors = authors
        self.year = year
        self.publish = ''
        self.affiliation = ''

        self.abs_url = f'https://arxiv.org/abs/{self.id}'
        self.pdf_url = f'https://arxiv.org/pdf/{self.id}'

        publish = re.findall(Publish, self.export_arxiv)

        if publish != []:
            self.publish = publish[0][0]
            self.publish = re.sub(r'(\w)(\d{4})', r'\1 \2',
                                  self.publish)  # CVPR2020 -> CVPR 2020

        else:
            # 未来对接整个互联网搜索
            self.publish = f'arXiv {self.year}'

    # unused
    def _get_affiliation(self):

        # obtain from pdf file
        pdf_file = Path(f'{self.year}_{self.title}.pdf')

        if pdf_file.exists():
            _, text_split = read_pdf(pdf_file)

            authors1 = self.authors[0].replace(' ', '')
            self.affiliation = text_split[text_split.index(authors1) + 1]

    def write_notes(self):
        '''
        define the markdown format and write notes
        '''

        # format is 'title, authors, and publication'
        title_url = f'[{self.title}]({self.abs_url})  '
        publish = f'**[`{self.publish}`]**'
        authors_str = ', '.join(self.authors)
        authors = f'*{authors_str}*  '

        print('-', title_url)
        print(' ', publish, authors, '\n')

def read_pdf(filename, update=False):
    '''
    read pdf and return id, text
    '''

    from PyPDF2 import PdfReader
    with open(filename, 'rb') as f:

        pdf = PdfReader(f)

        first_page = pdf.pages[0]
        text_split = first_page.extract_text().split()
        str_id = text_split[-5]
        id_version_local = re.findall(r'\d{4}\.\d{5}v\d{1}', str_id)[0]
        id = id_version_local[:-2]

        information = Information(query_id=id)
        if update and information.id_version != id_version_local:
            print(
                f'>>> Downloading from {id_version_local[-2:]} to {information.id_version[-2:]}'
            )
            request.urlretrieve(information.pdf_url, f'{information.year}_{information.title}_new.pdf')
            print(f'>>> Done')

    return id, text_split


def check_version():
    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('*.pdf'))

    for file in list(pdf_list):
        try:
            read_pdf(file, update=True)

        except Exception as ex:
            print('Error: ', ex)
            pass


def file2md():
    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('*.pdf'))

    for file in list(pdf_list):
        try:
            information = Information(query_title=file)
            information.write_notes()

        except Exception as ex:
            print('Error: ', ex)
            pass


def id2md():
    while True:
        id = input("type id: ")

        # 2011.13126
        if re.findall(r'\d{4}\.\d{5}', id):

            try:
                information = Information(id)
                information.write_notes()

            except Exception as ex:
                print('Error: ', ex)
                pass


if __name__ == '__main__':
    check_version()