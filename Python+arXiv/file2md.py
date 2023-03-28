from urllib import request
import re
from pathlib import Path
from PyPDF2 import PdfReader

CONF = 'ICML|NIPS|NeurIPS|ICLR|CVPR|ICCV|ECCV|AAAI|IJCAI|3DV|UAI'


class Information():
    def __init__(self, query_title) -> None:

        query_id, _, _ = self.read_pdf(query_title)

        if re.findall(r'\d{4}.\d{5}', query_id):
            self.query_url = f'http://export.arxiv.org/api/query?id_list={query_id}'
            self.id = query_id

        else:
            # 预处理title去掉 - 等转义符号
            query_title1 = str(str(query_title)[:-4]).replace(' ', '+').replace('-', '+')
            self.query_url = f'https://export.arxiv.org/api/query?search_query=ti:{query_title1}&max_results=1'

        self.strInf = request.urlopen(self.query_url).read().decode('utf-8')

        self._update()

    def _update(self):

        if re.findall(r'<entry>[\s\S]*</entry>', self.strInf):  # 匹配到了内容

            Id = r'<id>http://arxiv.org/abs/(.*)</id>'
            Title = r'<title>([\s\S]*)</title>'  # 有时候名字太长了，会换行
            Authors = r'<author>\s*<name>(.*)</name>\s*</author>'
            Year = r'<published>(\d{4}).*</published>'

            id_version = re.findall(Id, self.strInf)[0]
            id = id_version[0:-2]

            title = re.findall(Title, self.strInf)[0]
            title = re.sub(r'\n\s', '', title)  # 去掉换行
            title_sub = re.sub(r'[^\w\s-]', '', title)  # 去掉标点

            authors = re.findall(Authors, self.strInf)
            year = re.findall(Year, self.strInf)[0]

            self.id_version = id_version
            self.id = id
            self.title = title
            self.title_sub = title_sub
            self.authors = authors
            self.year = year
            self.publish = ''

            self.abs_url = f'https://arxiv.org/abs/{self.id}'
            self.pdf_url = f'https://arxiv.org/pdf/{self.id}'

            self.write_notes()

        else:
            pass

    def _get_publish(self):

        # 读取 txt 预定义会议名称

        # with open(r'conf_list.txt') as f:
        #     lines = [line.strip() for line in f]
        # reg = '|'.join(lines)

        # obtain form arxiv comments
        Publish = f'<arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">[\s\S]*(({CONF}).*?\d{{4}})[\s\S]*</arxiv:comment>'
        publish = re.findall(Publish, self.strInf)

        if publish != []:
            self.publish = publish[0][0]

            # 处理例如 CVPR2020 -> CVPR 2020
            self.publish = re.sub(r'(\w)(\d{4})', r'\1 \2', self.publish)

        else:
            # 未来对接整个互联网搜索
            self.publish = 'arXiv ' + self.year

    def write_notes(self):

        self._get_publish()

        # 组合处理
        title_url = f'[{self.title}]({self.abs_url})  '

        publish = f'**[`{self.publish}`]**'

        authors = ', '.join(self.authors)
        authors = f'*{authors}*'

        print('-', title_url)
        print(' ', publish, authors, '\n')

    def read_pdf(self, filename):
        '''
        读取pdf文件，返回id, version, text
        '''

        with open(filename, 'rb') as f:

            pdf = PdfReader(f)

            first_page = pdf.pages[0]
            text = first_page.extract_text()
            text_split = text.split()
            id_version_local = text_split[-5]
            id_version = id_version_local.split(':')[-1]

            id = id_version[0:-2] if id_version else []
            version = id_version[-1] if id_version else []

        return id, version, text


if __name__ == "__main__":

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('*.pdf'))

    for file in list(pdf_list):
        try:
            Information(query_title=file)

        except:
            print('Error: ', file)
            pass
