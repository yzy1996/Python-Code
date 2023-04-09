# Paper info into MarkDown

A tool to help you transfer arXiv information into markdown format.

<div align=center><img width="600" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/202303282243237.png"/></div>



## Support

- **id2md.py**: input arxiv id and then get the markdown format output.
- **file2md.py**: input foldername containing papers and then get the markdown format output.



## Usage

:laughing: now you can directly use such script anywhere after you install the specific package: 

```bash
pip install yzy

# dependency
pip install feedparser, PyPDF2

# then
python -m yzy.id2md
# or 
python -m yzy.file2md
```



---

1. run

```bash
python id2md.py
```

2. input `arxiv id` and get the result, for example:

<div align=center><img width="700" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/202303282218968.png"/></div>

3. copy the text and (shift) paste to your markdown file.

- [Lifting 2D StyleGAN for 3D-Aware Face Generation](https://arxiv.org/abs/2011.13126)  
  **[`CVPR 2021`]** *Yichun Shi, Divyansh Aggarwal, Anil K. Jain*

4. modify the information as you wish.

---



1. install `PyPDF2`
2. run

```bash
python file2md.py
```



## TODO

- [x] build pypi package

- [ ] add Internet conf search
- [ ] a website to use



## Related

https://github.com/MLNLP-World/SimBiber

https://github.com/yuchenlin/rebiber

https://github.com/j3soon/arxiv-utils



## 3rd-Party Usages

[arxiv_daily_tools](https://github.com/weihaox/arxiv_daily_tools)
