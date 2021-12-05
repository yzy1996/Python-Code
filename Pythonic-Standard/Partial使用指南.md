# functools.partial (偏函数) 使用指南

```python
def add(*args):
    return sum(args)
```





partial() 被用作 “冻结” 函数的输入参数，同时返回一个新的具有原功能的函数。也就是提前输入了一部分参数，等效于最后一起输入。