# Paper info into MarkDown

A tool to help you transfer arXiv information into markdown format.

<div align=center><img width="600" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/202303282243237.png"/></div>

## Installation

You can directly use such script anywhere after you install the specific package: 

```bash
pip install -U yzy 
```

Or you can develop from the source code.

## Usage (v1.1)

- **id2md.py**: input arxiv id and then get the markdown format output.
- **file2md.py**: input foldername containing papers and then get the markdown format output.
- **checkv.py**: auto-update the pdf version.

```bash
python -m yzy.id2md

python -m yzy.file2md

python -m yzy.checkv
```

Then you can copy the text and (shift) paste to your markdown file and modify the information as you wish.

## Development

You can add more conferences in [this](./conf_list.txt).

## TODO

- [x] build pypi package
- [x] check and update the local pdf version
- [ ] add Internet conf search
- [ ] build a website to use

## 3rd-Party Usages

[arxiv_daily_tools](https://github.com/weihaox/arxiv_daily_tools)

## Contact

Please email im.crazyang@gmail.com or create Github issues here if you have any questions or suggestions. 

## Related

https://github.com/MLNLP-World/SimBiber

https://github.com/yuchenlin/rebiber

https://github.com/j3soon/arxiv-utils

https://github.com/vict0rsch/PaperMemory

https://www.mybib.com/#/projects/WZg97M/citations