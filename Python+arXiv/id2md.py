from urllib import request
import re

CONF = 'ICML|NIPS|NeurIPS|ICLR|CVPR|ICCV|ECCV|AAAI|IJCAI|3DV|UAI'

class Information():
    def __init__(self, query_id) -> None:

        self.query_url = f'http://export.arxiv.org/api/query?id_list={query_id}'

        self.strInf = request.urlopen(self.query_url).read().decode('utf-8')

        self._re_process()

    # 正则表达式解析
    def _re_process(self):

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
        print(' ', publish, authors)


if __name__ == "__main__":

    while True:
        id = input("type id: ")

        ## 先判断 id 是否有效，形如：2011.13126
        if re.findall(r'\d{4}\.\d{5}', id):

            information = Information(id)
            information.write_notes()
