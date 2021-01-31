# YAML使用指南

> 配置文件



安装并使用包

```python
pip install pyyaml
import yaml
```



读取

```
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)
    
print(config)
```



## YAML文件规范

- 区分大小写；
- 使用缩进表示层级关系；
- 使用空格键缩进，而非Tab键缩进
- 缩进的空格数目不固定，只需要相同层级的元素左侧对齐；
- 文件中的字符串不需要使用引号标注，但若字符串包含有特殊字符则需用引号标注；
- 注释标识为#



- 对象：键值对的集合（简称 "映射或字典"）
- 键值对用冒号 “:” 结构表示，冒号与值之间需用空格分隔
- 数组：一组按序排列的值（简称 "序列或列表"）
- 数组前加有 “-” 符号，符号与值之间需用空格分隔
- 纯量(scalars)：单个的、不可再分的值（如：字符串、bool值、整数、浮点数、时间、日期、null等）
- None值可用null可 ~ 表示



## 几种类型

**(1) 字典**

```
usr: Jerry
psw: 123456
```

解析结果：

```
{'usr': 'Jerry', 'psw': 123456}
```



**(2) 数组**

```
- 1
- 2
- 3
```

解析结果：

```
[1, 2, 3]
```



**(3) 字典 嵌套 字典**

```
usr1:
  name: Tom
  psw: 123456
usr2:
  name: Jerry
  psw: 123456
```

解析结果：

```
{'usr1': {'name': 'Tom', 'psw': 123456}, 'usr2': {'name': 'Jerry', 'psw': 123456}}
```



**(4) 字典 嵌套 数组**

```
usr1:
  - 1
  - 2
usr2:
  - 1
  - 2
```

解析结果：

```
{'usr1': [1, 2], 'usr2': [1, 2]}
```



**(5) 数组 嵌套 字典**

```
- use1: Jerry
  psw: 123456
- use2: Tome
  psw: 123456
```

解析结果：

```
[{'use1': 'Jerry', 'psw': 123456}, {'use2': 'Tome', 'psw': 123456}]
```





## 基本数据类型

```
s_val: name             # 字符串：{'s_val': 'name'}
spec_s_val: "name\n"    # 特殊字符串：{'spec_s_val': 'name\n'
num_val: 31.14          # 数字：{'num_val': 31.14}
bol_val: true           # 布尔值：{'bol_val': True}
nul_val: null           # null值：{'nul_val': None}
nul_val1: ~             # null值：{'nul_val1': None}
time_val: 2018-03-01t11:33:22.55-06:00     # 时间值(iso8601格式)：{'time_val': datetime.datetime(2018, 3, 1, 17, 33, 22, 550000)}
date_val: 2019-01-10    # 日期值：{'date_val': datetime.date(2019, 1, 10)}
```



