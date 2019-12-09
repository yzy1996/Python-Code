<h1 align="center">For txt</h1>
<div align="center">



![python-version](https://img.shields.io/badge/python-3.7-blue) ![country](https://img.shields.io/badge/country-China-red)

</div>

## Usage

### Without Package

```python
with open('example.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

>>> 37 52 2
    49 49 4
    52 64 4
    20 26 1
    40 30 3
```



### With Package

`numpy.genfromtxt(fname, dtype=<class 'float'>, delimiter=None, encoding='bytes')`

`returns out: ndarray`



### Something Useful

1. `str.split(str="", num=string.count(str)) ` 

* str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
* num -- 分割次数。默认为 -1, 即分隔所有

`returns out: str`



2. `map(function, iterable)` 会根据提供的函数对指定序列做映射

可以用 `int` ，来将字符串变整数

## Example

You can see this example [txtfile](./example.txt)

`37 52 2`
`49 49 4`
`52 64 4`
`20 26 1`
`40 30 3`

```
import numpy as np

data = np.genfromtxt('example.txt')
>>> [[37. 52.  2.]
    [49. 49.  4.]
    [52. 64.  4.]
    [20. 26.  1.]
    [40. 30.  3.]] <class 'numpy.ndarray'>
    
print(data[0][0])
>>> 37.0 <class 'numpy.float64'>
```

Another example [txtfile](./example1.txt), but I really recommend you to use `csv` to store data with `,`

`37,52,2`
`49,49,4`
`52,64,4`
`20,26,1`
`40,30,3`

```python
import numpy as np

data = np.genfromtxt('example.txt')
>>> [nan nan nan nan nan]

data = np.genfromtxt('example.txt', dtype='unicode')
>>> ['37,52,2' '49,49,4' '52,64,4' '20,26,1' '40,30,3']


data = np.genfromtxt('example1.txt', dtype='unicode')
data1 = ()

for i in range(len(data)):
    data1 += tuple(map(int, data[i].split(',')))

data = np.reshape(data1, (5,3))
>>> [[37 52  2]
    [49 49  4]
    [52 64  4]
    [20 26  1]
    [40 30  3]] <class 'numpy.ndarray'>
```

