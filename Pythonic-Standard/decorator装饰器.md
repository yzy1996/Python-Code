# Decorator 装饰器用法

参考 https://www.zhihu.com/question/26930016





```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print('123')
        return func(*args, **kwargs)

    return wrapper

@decorator
def say_hello():
    print('同学你好')

# 相当于执行了 say_hello = decorator(say_hello)
    
say_hello()

>>> 123
	同学你好
```





```python
def info(value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(value)
            return func(*args, **kwargs)

        return wrapper

    return decorator

@info('456')
def say_hello():
    print('同学你好')

say_hello()

```

