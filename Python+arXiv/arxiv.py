from PyPDF2 import PdfFileReader
from urllib import request
import re
from soupsieve import match

from tqdm import trange

from pathlib import Path

'''
pipeline: 输入文章标题任意格式, 得到标准模板样式
'''

class Information():
    def __init__(self, query_id=None, query_title=None) -> None:
        
        if query_id != None:
            self.query_url = f'http://export.arxiv.org/api/query?id_list={query_id}'
        elif query_title != None:
            query_title = query_title.replace(' ', '+')
            self.query_url = f'https://export.arxiv.org/api/query?search_query=all:{query_title}&max_results=1'

        self.strInf = request.urlopen(self.query_url).read().decode('utf-8')

        self._re_process()

    # 正则表达式解析
    def _re_process(self):

        Id = r'<id>http://arxiv.org/abs/(.*)</id>'
        Title = r'<title>([\s\S]*)</title>' # 有时候名字太长了，会换行
        Authors = r'<author>\s*<name>(.*)</name>\s*</author>'
        Year = r'<published>(\d{4}).*</published>'

        id_version = re.findall(Id, self.strInf)[0]
        id = id_version[0:-2]
        
        title = re.findall(Title, self.strInf)[0]
        title = re.sub(r'\n\s', '', title) # 去掉换行
        title_sub = re.sub(r'[^\w\s-]', '', title) # 去掉标点  

        authors = re.findall(Authors, self.strInf)

        year = re.findall(Year, self.strInf)[0]

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

    def _get_publish(self):

        # 读取 txt 预定义会议名称

        with open(r'conf_list.txt') as f:
            lines = [line.strip() for line in f]
        reg = '|'.join(lines)

        # obtain form arxiv comments
        Publish = f'<arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">[\s\S]*(({reg}).*?\d{{4}})[\s\S]*</arxiv:comment>'
        publish = re.findall(Publish, self.strInf)

        if publish != []:
            self.publish = publish[0][0]

            # todo 处理例如 CVPR2020 -> CVPR 2020
            # re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", text)

        else:
            # 未来对接整个互联网搜索
            self.publish = 'arXiv ' + self.year

    def _get_affiliation(self):

        # obtain from pdf file
        # 判断这个文件是否存在
        pdf_file = Path(f'{self.year}_{self.title_sub}.pdf')

        if pdf_file.exists():
            with pdf_file.open('rb') as f:
                pdf = PdfFileReader(f)

                first_page = pdf.getPage(0).extractText()
                first_page = first_page.split()
        
            authors1 = self.authors[0].replace(' ', '')
            self.affiliation = first_page[first_page.index(authors1) + 1]


    def write_notes(self):

        self._get_publish()
        self._get_affiliation()

        # 组合处理
        title_url = f'[{self.title}]({self.abs_url})  '
        authors = ', '.join(self.authors)
        authors = f'*{authors}*  '

        publish = f'**[`{self.publish}`] (`{self.affiliation}`)** '

        print(title_url)
        print(authors)
        print(publish)


    # download pdf from the web
    def download(self):
  
        request.urlretrieve(self.pdf_url, f'{self.year}_{self.title_sub}.pdf')


def verify_local_version(filename='11.pdf'):

    with open(filename, 'rb') as f:
        pdf = PdfFileReader(f)
        first_page = pdf.getPage(0).extractText()
        first_page = first_page.split()

    # 查到本地文件的版本 v-x
    id_version_local = first_page[-5][6:]
    id = id_version_local[:-2]

    information = Information(query_id=id)

    if information.id_version != id_version_local:

        print('>>>Downloading the latest version!!!')
        information.download()
        

if __name__ == "__main__":

    # query with title
    # input_title = 'Image-to-Image Translation with Conditional Adversarial Networks'
    # information = Information(query_title=input_title)
    # information.write_notes()

    # # query with id
    # id = '2103.13413'
    # information = Information(query_id=id)
    # information.write_notes()

    # # 
    # verify_local_version()
    while True:
        id = input("type id: ")

        # 先判断 id 是否有效，形如：2103.13413
        if re.match(id, r'\t'):
            pass


        information = Information(query_id=id)
        information.write_notes()
