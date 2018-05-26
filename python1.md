Python
==============
本文档是北京理工大学[python基础课程](https://www.icourse163.org/learn/BIT-268001)的笔记部分

# 目录
-------------

<details>
    <summary><b>点击打开目录</b></summary>

- [第二章](#第二章)
  * turtle库的使用
- [第三章](#第三章)
  * [time库的使用](#time库的使用)
  * [文本进度条代码示例](#文本进度条代码示例)

</details>

-------------

## 第二章
turtle库的使用，基本图形的绘制

-------------


## 第三章
基本数据类型及其操作

-------------

数字的操作：
* pow
* round(0.1 + 0.2, 1)这样就等于0.3了，不用考虑浮点数的问题

字符串表示方法：
* 单双引号
* 两个```之间夹的也是字符串

字符串基本操作：
* 切片[s:e:i], [::-1]表示将其反转
* x `+` y 字符串相接
* n `*` s 将字符串s重复n次
* x `in` s 返回x是否是s的字串

字符串处理函数：
* len() 返回长度
* str() 返回字符串形式
* hex() 或 oct() 返回16进制和8进制的字符串形式
* chr(u) / ord(c) unicode和字符的转化

str对象方法：
* str.lower() / str.upper()
* str.split()
* str.count()
* str.replace(old, new)
* str.center(width, [fillchar])
* str.strip("xxx") 删除str左右的xxx中的字符 " .str#.".strip(" .#") = "str"
* str.join(iterable)

格式化字符串：

    " {0} is {2} and {1} ".format(s1, s2, s3) // 槽机制，可以用序号表示插入位置

    : <填充> <对齐> <宽度> <,> <.精度> <进制>  

|填充|对齐|宽度|,|.精度|进制|
|:--:|:--:|:--:|:--:|:--:|:--:|
|用于填充的字符|<>^左右中对齐|输出宽度|千分分隔符|小数精度|b,c,d,o,x,X整数;e,E,f,%浮点数|

### time库的使用

-------------

|类别|函数|
|:---:|:---:|
|时间获取|time(), ctime(), gmtime()|
|时间格式化|strftime(), strptime()|
|程序计时|sleep(), perf_counter()|

时间获取：
* time() 获得时间戳
* ctime() 获取可读方式 time.ctime() -- 'Fri Jan 26 12:11:15 2018'
* gmtime() 获取计算机可处理的形式 time.ctime() -- time.struct_time(tm_year = 2018, ...)

时间格式化：
* strftime(tpl, ts) tpl为模板字符串，ts为计算机可以处理的时间，返回一个str
* strptime(str, tpl) 输入一个str和对应的模板字符串，返回ts

|格式化控制符|说明|
|:---:|:---:|
|%Y|年份|
|%m|月份|
|%B|月份名称|
|%b|月份名称缩写|
|%d|日期|
|%A|星期|
|%a|星期缩写|
|%H|小时24h制|
|%h|小时12h制|
|%M|分钟|
|%S|秒钟|

程序计时：
* sleep(x) 停止x秒
* pref_counter() 返回一个计数值，单位为秒

### 文本进度条代码示例

-------------
    涉及了较多知识点，如
    str.center(), str*int, time库使用, print end参数&\r回到行首刷新, 字符串格式化等
    注意：用idle执行不会产生预期效果，双击运行可以

```python
import time

scale = 50
print("start".center(scale // 2, '-'))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur),end="")
    time.sleep(0.1)
print("end".center(scale // 2, '-'))
```

计时方法在程序中是十分重要的，可以应用在：
* 比较算法执行时间
* 提高用户体验
* 人机纽带之一
* 在执行时间较长的程序中增加进度条
* 实际进度`≠`进度条展示 的操作（从用户心理出发？）

-------------

## 第四章
程序的控制

-------------

控制语句：
* 条件多分支 `if else elif...`
* 条件判断 `<exp1> if <statement> else <exp2>`简单写法，`不支持赋值过程`
* 语句逻辑关系 `and or not`分别表示`与或非`
* 异常处理 `try: <exp1> except: <exp2>` 或者 `try: <exp1> except <exptype>: <exp2>`只有发生`<exptype>(NameError, ValueError, et, al.)`类型错误时执行`<exp2>`语句
* 高级异常 `try: <exp1> except: <exp2> else: <exp3> finally: <exp4>` else是没有异常时执行的，finally不管有无异常都执行

循环结构：
* 遍历循环for `for <v> in <i> : <exp>` <i>常见的为`str`/`range()`/`[list]`/`[fi]`文件读取，每次读取一行 
* 无限循环while `while <statement>: <exp>` 
* 高级用法 `for in else...` `while else...` 如果循环没有被`break`语句终止退出，则执行`else`后面的内容

### random库的使用

-------------
使用梅森旋转算法生成的伪随机数，

|类别|函数|
|:---:|:---:|
|基本函数|seed(), random()|
|范围内随机数|randint(), getrandbits(), uniform(), randrange()|
|扩展随机函数|choice, shuffle()|

基本函数：
* seed(), 无参数默认以系统时间戳为准，有参数则生成固定伪随机序列
* random(), 生成[0.0, 1.0)范围内随机整数

范围内随机数：
* `randint(a, b)` [a, b]内随机整数
* randrange(m, n[, k]) [m, n)范围内以k为步长的随机整数
* getrandbits(k) 生成一个k比特长的随机整数
* uniform(a, b) 生成一个[a, b]之间的随机小数(可保留16位小数)

扩展随机函数：
* choice(seq) 从seq序列中随机选择一个元素
* shuffle(seq) 随机打乱seq序列的顺序

-------------
圆周率的计算：公式法和蒙特卡罗法
* 公式法：数学思维
* 蒙特卡罗法：计算思维，用计算机自动化求解

-------------

## 第五章
函数与代码复用

-------------

函数是一段代码的表示，表达特定的含义，两个作用：
* 降低编码难度
* 代码复用

```python
# function: simple IPO
def <name>():
    <exp>
    return ...
```

可选参数--只能放在非可选参数之后
可变参数

```python
def <name>(n, *b, **key):
    <exp>
    # b保存着传入的参数列表，key是传入的键值对
```

函数的返回值，多个返回值构成一个**元组**
在函数中使用`global`关键字可以声明为全局变量
`组合类型未在函数中创建，等同于全局变量`

```python
n, s = 1, 1
def f():
    # global s, without this s == 1, or s == 2
    s = 2
f()
print(n, s)
```

`lambda` 函数：当行内可定义，应用于一些特定的方法或函数的参数

函数和对象是代码复用的两种主要形式
模块化设计：具体包括主程序、子程序和子程序之间的关系（分为治之）
紧耦合和松耦合：两个部分交流的多少

### PyInstaller库

-------------

用于将.py文件打包成为一个可执行文件

|参数|作用|
|:---:|:---:|
|-h|帮助|
|--clean|清理打包临时文件|
|-D|生成一个文件目录dist|
|-F|生成一个可执行文件，位于dist目录中|
|-i <icon.ico>|制定打包的icon|

-------------

## 第六章
组合数据类型

-------------

集合类型-多个元素的**无序组合**，要求放入的**元素唯一**且类型是**不可变数据类型**: `整数、浮点数、字符串、元组等`
使用{}或set()建立`set("python") -- {'p', 'y', 't', 'h', 'o', 'n'}//以大括号和逗号表示`

|集合操作符|作用|
|:---:|:---:|
|`S\|T`|∪，S与T的并集|
|`S-T`|在S中但不在T中的|
|`S&T`|∩，S与T的交集|
|`S^T`|S和T的非相同元素|
|`S<=T` `S<T`|返回True或False，判断S和T子集关系|
同时还有`S\|=T, S-=T, S&=T, S^=T`等操作，会改变集合S

|集合方法|作用|
|:---:|:---:|
|`S.add(x)`|将x增加到S中|
|`S.discard(x)`|将x从S中移除，不报错|
|`S.remove(x)`|将x从S中移除，报错|
|`S.clear(x)`|清空S|
|`S.pop(x)`|随机返回S的元素一个，报错|
|`S.copy()`|返回S的副本|

    集合的应用：
    * 包含关系的比较
    * 数据去重

序列类型 **（包括字符串、元组、列表等）** 的基本操作：
* `x in s / x not in s`
* `s + t`连接
* `s * n`复制n次
* `s[i:j:k]`切片，不改变原序列
* `len(s)`
* `min(s)`
* `max(s)`
* `s.index(x) / s.index(x,i,j)`返回[i,j]之间第一次出现的索引
* `s.count(x)`

元组类型-----继承序列的操作，值不可更改

列表类型-----继承序列，值可以更改
列表的其他操作：
* `del s[i] / del s[i:j:k]`
* `s[i] = n`
* `s += t`
* `s *= n`

|列表方法|作用|
|:---:|:---:|
|`ls.append(x)`|将x增加到ls末尾|
|`ls.insert(x, n)`|将x添加到n位置|
|`ls.pop(i)`|弹出i位置的值|
|`ls.remove(x)`|删除第一次出现的x值|
|`ls.clear()`|清空|
|`ls.reverse()`|反转|
|`ls.copy()`|复制，生产新列表**注意tuple无copy方法**|
|`ls.sort(func, key, reverse)`|排序，key是一个回调，如`lambda x:x[1]`|

字典类型：键值对形式，以{}和dict()创建，以:分割键值，以,分割项
操作：
* `del d[k]`
* `k in d`键k是否在d的键列表中
* `d.keys()`返回`dict_keys([x, y, z])`
* `d.values()`返回`dict_values([a, b, c])`
* `d.items()`返回`dict_items([(x,a), (y,b), (z,c)])`

|字典方法|作用|
|:---:|:---:|
|`d.get(k[, default])`|返回key为k的值，没有则返回default|
|`d.pop(k[, default])`|弹出key为k的值，没有则返回default|
|`d.popitem()`|随机弹出一个item，以元组的形式|
|`d.clear()`|清空操作|

### jieba库

-------------

用处是分词：将中文词句分为一个个的部分

|函数|作用|
|:---:|:---:|
|`jieba.lcut(s)`|不存在冗余的分词，用得多|
|`jieba.lcut(s, cut_all=True)`|存在冗余的分词|
|`jieba.lcut_for_search(s)`|搜索引擎模式分词|
|`jieba.add_word(s)`|向库中加入词s|

-------------

## 第七章
文件的使用

-------------

文件是数据的抽象和集合
* 文件是存储在辅助存储器上的数据序列
* 文件是数据存储的一种格式
* 文件的展现形态有文本文件和二进制文件

    文本文件 vs 二进制文件
    * 本质上，它们均是二进制存储的
    * 展现方式上不同：文本文件由单一编码组成，如utf-8；二进制文件由0和1构成，没有特定的编码格式，例如.png、.avi文件等

文件的打开：f = open("xxx.txt", "r")

|文件打开模式|描述|
|:---:|:---:|
|r|只读模式，如果文件不存在返回FileNotFoundError|
|w|覆盖写模式，文件不存在则创建，存在则完全覆盖|
|x|创建写模式，创建文件并写入，如果文件存在返回FileExistsError|
|a|追加写模式，文件不存在则创建|
|b|二进制文件模式|
|t|文本模式，python默认的打开模式为rt|
|+|与rwxa结合使用，在原功能基础上增加同时读写功能|

    r+ 读+写，开始时文本指针位于头部
    w+ 覆盖写+读，开始时清空文本内容，文本指针位于头部
    a+ 追加写+读，开始时文本指针位于尾部

|读文件方法|描述|
|:---:|:---:|
|f.read(h=-1)|不给h则读取所有文本内容，返回一个字符串，给参数则读取前h个字符|
|f.readline(h=-1)|不给h读取一行，给h读取该行的前h个字符|
|f.readlines(h=-1)|读取前h行存入一个列表中并返回|

    若使用f.read()或f.readlines()一次性读取全部内容，可能需要花费较多成本，给这两个函数加上参数会好一些，或者使用for line in f:p ...，每次只会读取一行内容


|写文件方法|描述|
|:---:|:---:|
|f.write(s)|写入内容s|
|f.writelines(l)|写入列表l中是所有字符串|
|f.seek(offset)|改变文本指针位置 0开头 1当前 2结尾|

### wordcloud库

-------------

用于更直观地展现词语

`import wordcloud`
`w = wordcloud.WordCloud()`生成一个词云
`w.generate(txt)`向词云对象`w`中加入文本`txt`
`w.to_file(filename)`将词云输出为`.png/.jpg`格式文件

`w = wordcloud.WorldCloud()`的参数：

|参数|描述|
|:---:|:---:|
|width|指定宽度，默认400px|
|height|指定高度，默认200px|
|min_font_size|最小字号，默认4号|
|max_font_size|最大字号，默认值根据height变化|
|font_step|字号的步进间隔，默认1|
|font_path|字体文件，默认None|
|max_words|最大单词数量，默认200|
|stop_words|排除列表，以dict形式写入|
|mask|```from scipy.misc import imread / mk = imread("xxx") / w = wordcloud.WordCloud(mask=mk) ```|
|background_color|背景颜色，默认为黑色|

    mask是剪贴蒙版，是一章白色背景的图片