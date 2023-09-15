# CSV



python 自带就有一个 csv 库

```python
import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```



```python
import csv
for row in csv.reader(['one,two,three']):
    print(row)
```



也可以借助 panda

```python
import pandas

df = pandas.read_csv('test.csv', encoding='utf-8')
print(df['Price'][0])
```

















