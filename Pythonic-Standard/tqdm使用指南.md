# tqdm 使用指南

https://tqdm.github.io/



先不说原理了，直接上无脑的使用过方法：

```python
from tqdm import tqdm

epoch = 0

while epoch < 10:
    epoch += 1
    with tqdm(train_loader, desc=f'Epoch {epoch}/10') as pbar:
        for i, (images, _) in enumerate(pbar):

            pbar.set_postfix(loss=i)
```



再来说一下我们的目标：

- 在哪一个epoch
- 每一个epoch里的迭代iteration
- 打印输出loss等log结果





需要设置好一些说明，以及更新策略



怎么简单怎么来



```
with tqdm(total=100) as pbar:
    for i in range(10):
        pbar.update(10)
```

意思是每隔10步更新一次，每次更新10，所以进度条就是10+10+10...



一种是 epoch 需要 tqdm，一种是每个 epoch 里的所有迭代循环

每多少个 iteration 打印一次 





range + len 出问题





root_dir = Path('./')
pdf_list = root_dir.glob('scan*.pdf')
a = list(pdf_list)

for file in tqdm(a):
    sleep(0.1)



搭配 enumerate 使用

for i, line in enumerate(tqdm(f)):





## 属性

```python
pbar 
```

