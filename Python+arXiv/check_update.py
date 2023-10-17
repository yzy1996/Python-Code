from urllib import request
from urllib.error import URLError, HTTPError
import re
from pathlib import Path
from pypdf import PdfReader
import feedparser
import os

class Information():
    def __init__(self, query_title) -> None:

        with open(query_title, 'rb') as f:

            pdf = PdfReader(f)
            first_page = pdf.pages[0]
            text_split = first_page.extract_text().split()


            for page in pdf.pages:
                if "/Annots" in page:
                    for annot in page["/Annots"]:
                        if annot.get_object()["/Subtype"] != "/Link":
                            self.flag_annot = True
                            break
                    else:
                        continue
                    break
            else:
                self.flag_annot = False


        str_id = text_split[-5]
        self.id_version_local = re.findall(r'\d{4}\.\d{5}v\d{1}', str_id)[0]
        query_url = f'http://export.arxiv.org/api/query?id_list={self.id_version_local[:-2]}'

        try:
            response = request.urlopen(query_url)
        except HTTPError as e:
            print('Error code: ', e.code)
        except URLError as e:
            print('Reason: ', e.reason)
        else:
            export_arxiv = response.read().decode('utf-8')

        feed = feedparser.parse(export_arxiv)

        self.query_title = query_title
        self.title = re.sub(r'[^\w\s-]', '', feed.entries[0].title).replace("\n", "").replace("  ", " ")
        self.year = feed.entries[0].published[:4]
        self.abs_url_version = feed.entries[0].id
        self.abs_url = self.abs_url_version[:-2]
        self.pdf_url = self.abs_url.replace('abs', 'pdf')
        self.id_version_server = self.abs_url_version[-12:]

    def check_update(self):
        if self.id_version_server != self.id_version_local:

            # 检查是否有笔记
            if not self.flag_annot:
                print(f'>>> Downloading from {self.id_version_local} to {self.id_version_server}')
                request.urlretrieve(information.pdf_url, f'{information.year}_{information.title}.pdf')
                os.remove(self.query_title)  

            else:
                print(f'>>> 请注意：{information.title} 存在更新版，但旧版本有笔记标注。')
                request.urlretrieve(information.pdf_url, f'{information.year}_{information.title} (1).pdf')

if __name__ == "__main__":

    root_dir = Path('./')
    pdf_list = sorted(root_dir.glob('*.pdf'))

    for file in list(pdf_list):
        try:
            information = Information(query_title=file)
            information.check_update()

        except Exception as ex:
            print('Error: ', ex)
            pass


