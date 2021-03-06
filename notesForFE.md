笔记整理
==============
本文档是一些前端知识点的整理版本

# 目录
-------------

<details>
  <summary><b>点击打开目录</b></summary>

  - [前端基础](#前端基础)
  - [数据结构](#数据结构)
  - [网络](#计算机网络)

</details>

## 前端基础

-------------

1. CSS三栏布局方法 / 两栏左边固定右边自适应
* position: absolute定位，比较机械
* table/table-cell布局
* 浮动布局 双飞燕+圣杯，三层标签margin -100%等实现  
* flex布局（flex有哪些属性，怎么用的）
* grid布局（grid常用属性有哪些，怎么用的）

2. CSS垂直居中方法
* height & line-height
* position + translate方法
* table-cell / inline-block自动居中
* flex两种方法
* writing-mode方法

3. CSS双栏等高布局方法
* position + margin负值模拟
* table/table-cell布局
* flex布局

4. CSS权值  
#: 100
.: 10
tag: 1
继承: <1

4. Web语义化的理解
利于SEO，利于阅读网页信息，主要包含两部分：HTML语义化和CSS语义化
* HTML语义化包含让正确的标签做正确的事情、页面内容结构化、利于爬虫标记和SEO  
header, hgroup, footer, aside, nav, article, section等H5标签
* CSS语义化包含class和ID命名的语义，选择器名称是文档部件表达的意思或者在文中的位置，而不是样式相关。

5. 常见的14种HTML状态码

|状态码|标识|说明|
|:--:|:--:|:--:|
|200|OK|请求正常处理完毕|
|204|No Content|请求成功处理，没有实体的主体返回|
|206|Partial Content|GET范围请求已成功处理|
|301|Moved Permanently|永久重定向，资源已永久分配新URL|
|302|Found|临时重定向，资源已临时分配新URI|
|303|See Other|临时重定向，期望使用GET定向获取|
|304|Not Modified|配合If Modified Since 和 LastModify等使用的属性，和重定向没有半毛钱关系|
|307|Temporary Redirect|临时重定向，POST不会变成GET|
|400|Bad Request|请求报文语法错误或参数错误|
|401|Unauthorized|需要通过HTTP认证，或认证失败|
|404|Not Found|无法找到请求资源，服务器无理由拒绝|
|500|Internal Server Error|服务器故障或Web应用故障|
|502|Bad Gateway|为了完成请求访问下一个服务器，但该服务器返回了非法的应答|
|506|Service Unavailable|服务器超负载或停机维护|

6. HTML报文头部以及消息报头有哪些常见值？什么意思？
请求头：
```
GET https://www.baidu.com/img/baidu_jgylogo3.gif HTTP/1.1

Accept  */*
Accept-Encoding gzip, deflate, br
Accept-Language zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection  keep-alive
Cookie  _uab_collina=15299169869571128…1632033F343C206B460BFAA9D4C49
Host  g.alicdn.com
Referer https://login.taobao.com/membe…3060e4575e98eb5293fa4adf49af4c
User-Agent Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0
```
响应头：
```
HTTP/1.1 200 OK

access-control-allow-origin *
age 2583
cache-control max-age=2592000,s-maxage=3600
content-encoding  gzip
content-length  121629
content-md5 wXF/pQ0O55hPi21+qfDWYw==
content-type  application/javascript
date  Sun, 21 Oct 2018 13:17:02 GMT
server  Tengine
```

7. html cache类型有哪些？
* cache的优先级：`service worker`, `memory cache`, `disk cache`, network
* `memory cache`忽略html头中的设定，每次都会缓存，优先被命中，而且资源不返回状态码。  
Cache-Control: public, max-age=31536000可以使用memory cache  
保证相同的资源不会被加载两次  
* `Cache-control`: no-store是一个例外情况，`memory cache`及`disk cache`不会缓存任何内容，一般关闭页面Tab后memory和cache失效。
* `disk cache` 分为**强缓存**和**协商缓存**
* 强缓存：关键字为`Cache-control（HTTP1.1）`,`Expires` & `Pragma: no-cache (HTTP1.0)`, `Cache-control`的优先级较高
* `Cache-control` 有`max-age`(单位秒), `must-revalidate`, `no-cache`(缓存内容但是不使用), `no-store`(不缓存内容), `private`(默认值，客户端缓存，代理服务器不缓存), `public`(客户端和代理服务器都缓存)等选项。
* 协商缓存：强缓存失效之后使用的缓存机制，无法节约请求数量，如果服务器返回304状态码，则节省了数据量，效果不如强缓存。
两对值：
服务器：`Last-Modified` 客户端：`If-Modified-Since`
服务器：`Etag` 客户端：`If-None-Match` （这一组优先级较高）
* 缓存的应用：

  1. 对于长期不变的资源，可以设置`Cache-control: max-age=360000` 很大的数字；
  2. 对于经常变动的资源，比如微博文章等，可以设置`Cache-control: no-cache`，使用协商缓存；
  3. 注意不要使用类似`Cache-control: max-age=600 must-revalidate `的方式，这会导致客户端缓存时间混乱，出现各种问题。

8. keep-alive
* HTTP1.0头字段`Collection: keep-alive`
* HTTP1.1默认就有长连接
长连接可以复用TCP连接，从而节省了时间，但改变不了HTTP是半双工协议的特征。

9. Array方法列举，哪些改变了array哪些没有
* 改变Array的方法：`push pop unshift shift splice reverse sort`
* 不改变Array的方法：`slice concat (filter reduce map)`
* 其他方法：`indexOf lastIndexOf forEach...`

10. 实现简单的promise, New, function.bind, Object.create, require模块加载器

11. 验证邮箱的正则表达式
`/^([a-zA-Z0\-9.-_])+@([A-Za-z0-9])+\.[A-Za-z0-9\-._]{2,5}[A-Za-z0-9]$/`  

12. css动画animation、transition属性
* `animation: 'Bounce' 1000 ease-in 300 5 alternate`  
(name, time, time-func, delay, circle/infinite, reverse?/normal)
* `transition: 1000 swing 300`  
(property, time, time-func, delay)

13. 网页性能优化方法
* 宏观优化  
  1.**减少请求**(使用缓存、压缩资源、雪碧图、图片base64嵌入、图片懒加载等)  
  2.**js文件置于底部**
  ，防止阻塞其他元素的加载  
  3.**懒加载**，异步加载  
  4.将css内容放在顶部，**不使用@import**  
* Js优化  
  1.每次访问`HTMLCollection`元素都会重新获取一遍，可以将它转化为`Array`保存下来  
  2.`Reflow/Repaint`，频繁的Dom修改合并为一次操作  
  3.访问的作用域链越长，开销越大，对于操作次数非常多的情况，可以选择将作用域链较长的元素保存为局部变量  
  4.事件委托  

14. array-like Object有哪些？怎么转化成array？
* `arguments`函数参数, `arguments.callee`表示调用它的函数
* `HTMLCollectioin` 表示`Element node`的集合，通过`getElementsByName, getElementsByTagName, getElementsByClassName`获取，是动态的元素
* `NodeList`表示`node`集合，通过`.childNodes, querySelectorAll`等获取，是静态的元素。
* `NamedNodeMap`通过`Element.attributes`属性获取，包含所有的属性对象的集合

15. Array相关的问题
* 深拷贝数组的方法：
  1. 使用函数
  2. 使用JSON.parse(JSON.stringify(arr))
* 浅拷贝方法：
  1. [].slice.call(arr)
  2. [].concat.call(arr)
  3. b = [...a] 或 [...b] = a
* 数组同值
  1. Array(10).fill('a')
  2. Array.apply(null, {length: 10}).map(() => 'a')
* 数组转化:和浅拷贝类似
* 数组去重:
  1. for循环, forEach循环
  2. 利用Set [].from((new Set(arr)))
  3. 利用obj，类比桶排序
* obj类型检查：
  1. typeof
  2. instanceof 原型链相关
  3. constructor 需要原形和构造函数有联系
  4. {}.toString.call(obj) 返回 '[Object Object]'

16. cookie相关
* 读Cookie方法 `document.cookie`
* cookie的格式: `"xx=XX; yy=YY; ... ; zz=ZZ"`
* cookie最多4kB空间，保存用户的登录信息等
* cookie和session
  1. cookie存放在客户浏览器上，session存在服务器里
  2. 建议把登录信息等重要内容放在session，其他内容可以放在cookie
  3. cookie的形式是一个字符创，session是一个对象
  4. session不区分路径，访问一个网站的任意路径可访问相同的session；cookie有路径，不同路径中的cookie无法互相访问
* cookie的问题
  1. cookie空间太小
  2. 每次请求都要发送cookie，浪费带宽
  3. cookie无法跨域

17. localStorage和sessionStorage
* 大于5MB空间，可以存储较多信息
* webStorage是保存数据之用，sessionStorage在刷新/跳转到同源路径时不会消失，关闭浏览器或标签页才消失。
* 操作API(localStorage可换为sessionStorage)
```
localStorage.setItem(key, value);
localStorage.getItem(key);
localStorage.removeItem(key);
localStorage.clear();
localStorage.key(index);// 返回对应index的key值
```
注意：key和value全为字符串

18. 冒泡和捕获，事件流哪三个阶段？
* 事件：捕获阶段 -- 处理阶段 -- 冒泡阶段
* 事件委托利用了事件冒泡  
`var addEvent = addEventListener || attachEvent`  
`var target = e.target || e.srcElement;`

19. Css实现保持长宽比1:1
* 使用vw单位
* w30% + p-b100%
* grid网格随便搞

20. flex & grid重要的属性  
**Flex Base Styles**  
Container:  
`display: flex;`  
`flex-direction: column/row/column-reverse/row-reverse; `  
`justify-content: flex-end/flex-start/center/space-around/space-between/space-evenly`水平方向对齐  
align-items: flex-end...竖直方向对齐  
Item:  
`align-self: flex-end... `单个元素的垂直对齐方式  
**Normal Styles:**  
Container:  
`flex-wrap: wrap/wrap-reverse` 允许多行排布  
`align-content: space-evenly` 这个属性指的是有多列的flex子元素，怎么排列  
Item:  
`flex-grow: [Integer]` 这个属性指明拉伸(理解为)时元素拉伸多少倍，默认是1，设置为0时不会被拉伸，注意指的是拉伸比例而不是占据flex容器的多少  
`flex-shrink: 与flex-grow 相反`  
`flex-basis: [Num]px` 代替元素初始大小  
`flex: flex-grow flex-shrink flex-basis;` 简写形式  
**Grid Base Styles**  
Container:  
`grid-template-columns: 200px auto 200px;`  
`grid-template-rows: 100px 30px;`  
Item:  
`grid-column: 1 / 4;`  

21. 浏览器垃圾回收机制
* 引用计数，IE6-7应用的方法，容易内存泄漏
* 标记清除法，从根对象开始依次标记可达的对象，然后将其flag设为1，最后遍历所有元素，flag不为1的元素被删除

22. bootstrap中.row, .col-xs-5等的实现原理
* 响应式: `@media (min-width: 768/992/1200px)`依次写可以不写`max-width`之类的东西
* `.container`有两边15px的padding
* `.row`使用两边-15px的margin填充满container
* `.col-xs-5` 的实现：每种单元格类型均使用`float:left`，都是用左右`padding 15px`
针对n值的不同，设置width的百分比不同

23. 整理跨域相关的问题

**JSONP**  
页面中定义好方法，server中调用  
server中：
```
var qs = querystring.parse(req.url.split("?")[1]);
res.end(qs.callback + "(" + JSON.stringify(data) + ")");
```
应用格式：  
`<script src="http://127.0.0.1:3000/jsonp?callback=runMe"></script>`
* 只能使用GET方法
* 执行函数必须为全局函数

**CORS**
```
// 发送简易的ajax请求
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () {
  if (xmlhttp.readystate === 4 && xmlhttp.status === 200) {
    // do something
  }
}
// 最后一个参数为false则表示同步请求
xmlhttp.open('GET', 'http://127.0.0.1:80', true);
xmlhttp.setRequestHeader('Origin', 'localhost');
xmlhttp.send(null);
服务器端
res.writeHead(200, {
  contentType: 'text/javascript;charset=UTF-8',
  'Access-Control-Allow-Origin': '*'
})
```
**window.name**
基本思路:
1. 将远程页面的`window.name`设置为一个待传递的字符串;
2. 在需要跨域的页面中引入远程页面`(<iframe>)`, 然后在脚本中将这个iframe的src替换成本地的空页面;
3. 使用`this.contentWindow.name`读取到数据。
eg:
```
<iframe src="http://127.0.0.1:3000/domainB" frameborder="1"></iframe>
// in script
var iframe = document.querySelector(iframe)[0];
var flag = 0;
iframe.onload = function () {
  if (flag === 0) {
    iframe.src = "./vain.html";
    flag = 1;
  } else {
    console.log(this.contentWindow.name);
    // 加上这一句之后就可以，刷新页面也有效
    document.body.removeChild(this);
  }
}
```

**PostMessage**
用于和iframe的通信
* 发送方，iframe内嵌入发送方页面
```
var targetOrigin = "*";
iframe.contentWindow.postMessage(input.value, targetOrigin);
```
* 服务端
```
window.addEventListener('message', function (e) {
  receive.innerHTML = e.data;
}, false)
```

Jquery的ajax请求实例
```
// post
button.click = function () {
  $.ajax({
    type: 'GET',
    url: 'service.php?number'= + $("#bt").val(),
    dataType: 'json',
    data: {
      name: 'Jelly'
    },
    success: function (data) {
      ...
    },
    error: function (jqXHR) {
      console.log(jqXHR.status);
    }
  })
}
```

23. websocket相关知识

* HTML的限制：请求头很重、半双工、只能由客户端向服务器发送请求，如果要获取服务器状态则必须不断地轮询，浪费资源。  
* websocket的最大特点就是，服务器可以主动向客户端推送信息，客户端也可以主动向服务器发送信息，是真正的双向平等对话，属于服务器推送技术的一种。  
特点：建立在TCP协议之上，通过HTTP协议建立连接，无同源限制，可以发送文本和二进制数据。  
* 连接建立头字段：
`Upgrade: websocket` and `Connection: Upgrade`  
客户端返回
```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk= Sec-WebSocket-Protocol: chat
```
客户端API
```
var ws = new WebSocket('ws://localhost:8080');
webSocket.readyState -- CONNECTING/OPEN/CLOSING/CLOS
ws.onopen
ws.onclose
ws.onmessage 用于指定收到服务器数据后的回调函数
ws.send 用于向服务器发送数据
ws.onerror
webSocket.bufferedAmount 表示还有多少字节的二进制数据没有发送出去。它可以用来判断发送是否结束。
```

24. 整理DOM操作
节点类型：
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>A document</title>
  </head>
  <body>
    <!-- some comments -->
    <div>Document contents</div>
  </body>
</html>
```
* 节点都有`nodeType, nodeName, nodeValue, parentNode`等属性
* 常见的有：  

|node|nodeType|nodeName|nodeValue|parentNode|
|:--:|:--:|:--:|:--:|:--:|
|ELEMENT_NODE|1|`{tagName}`|null|父节点|
|ATTRIBUTE_NODE|2|`{name}`|`{value}`|null|
|TEXT_NODE|3|#test|`{value}`|父节点|
|COMMENT_NODE|8|#comment|`{value}`|父节点|
|DOCUMENT_NODE|9|#document|null|null|
|DOCUMENT_FRAGEMENT_NODE|11|#document-fragment|null|null|
|DOCUMENT_TYPE_NODE|10|doctype名|null|Document|

* 节点通常操作
属性：方便访问-同级的先后元素 / 子节点集合 / 第一个和最后一个子节点
`previousSibling / nextSibling
childNodes / firstChild / lastChild`

方法：
* 增：`appendChild(anode)`，注意如果anode已经存在，则相当于将其从原来的位置移动到新位置，返回anode
`insertBefore(insert_node, ref_node)`
* 删：`removeChild(anode)`
* 改：`replaceChild(new, old)`
* 复制：`cloneNode(BULL)`，BULL为true会复制所有子节点

* ELEMENT_NODE：
`className`属性
`attributes` Attr节点集合
`getAttribute(), setAttribute(), removeAttribute()`

* TEXT_NOD：
`document.createTextNode()`

26. 延迟加载脚本async & defer  
`<script async></script>`  
`<script defer></script>`  

27. 基本的快排
```
// 时间复杂度O(nlogn), 优化方式：1.三数字取中法优化主元；2.元素较少时使用插入排序作为替代
let arr = [];
for (let i = 0; i < 100; i++) {
  arr.push(Math.ceil(Math.random() * 2048));
}
quickSort(arr);
console.log(arr);

function quickSort(arr) {
  quick(arr, 0, arr.length-1);
}

function quick (arr, left, right) {
  // 注意边界条件判定
  if (left >= right) {
    return ;
  }
  
  // 直接将主元选择为最右端的元素
  let pivotIndex = right;
  let pivot = arr[pivotIndex];

  let i = left, j = right - 1;

  while (true) {
    while (arr[i] < pivot) {
      i++;
    }
    while (arr[j] > pivot) {
      j--;
    }
    if (i < j) {
      swap(i, j);
    } else {
      break;
    } 
  }

  swap(i, right);
  quick(arr, left, i - 1);
  quick(arr, i + 1, right);

  function swap (i, j) {
    // 同一元素则不用交换，节省资源
    if (i === j) {
      return ;
    }
    let tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
  }
}
```

28. list的方法

* entries
* every / some
* find / findIndex / indexOf / lastIndexOf
* flat / flatMap
* includes
* keys / values
* reduce / reduceRight / map / filter
* toSource / toString / toLocalString / 
* Others ...

29. window.fetch方法

Fetch是为取代XMLHttpRequest而生的
* fetch对返回404、500等情况也调用resolve，但是ok属性值为false
* 

-------------

## 数据结构

-------------
> 线性数据结构  
>> 1. 链表翻转  
设置三个指针，分别指向new, old, tmp, 将old.next = new  
>> 2. 后缀表达式  
逆波兰式子，本质是栈的问题，比如`3*(2+5)/(3-1)` => `3 2 5 + * 3 1 - /`  
>> 3. 栈、队列基本操作和存储结构  
进栈、出栈、入队、出队，可以用链表或者数组存储  
>
> 树  
>> 1. 遍历方法，递归和非递归实现方法  
先序 递归或者用栈  
中序 递归或者用栈  
后序 递归或者用栈，栈中需要加一个域，表明是否被访问过  
层序 使用队列  
>> 2. 二叉树翻转  
和层序遍历一样使用队列就能实现  
>> 3. 二叉搜索树相关操作  
增删改查  
>> 4. AVL树  
单左 / 单右  
左右 = 右右 + 左左  
>> 5. 堆的操作  
堆是一棵完全二叉树(Complete Binary Tree)  
堆的建立：共O(n)时间，从下向上调整，最底层最多调整一次，最上层最多调整log(n)次  
堆的插入：从下向上调整，O(log(n))  
堆的删除：删除根节点，然后从上到下，把最后一个元素与下一层左右节点大的元素对比，O(log(n))  
>> 6. 并查集和哈夫曼树  
哈夫曼树：用于编码，不能存在歧义，数据存在叶节点上  
并查集：非二叉树，使用数组存储，根节点parent值为-1  
>
> 图
>> 1. DFS和BFS  
DFS使用递归或者栈可以实现  
BFS(breadth-first-search)使用队列  
>> 2. dijkstra和floyd算法  
dijkstra 用于计算单源最短路径 O(V^2+E), 堆优化后O(Elog(V))  
floyd 用于计算所有节点互相的最短路径 O(V^3)  
>> 3. Prim算法，kruskal  
用于最小生成树，思想都是贪心算法  
Prim类似dijkstra O(V^2)  
kruskal每次选取剩余E中最小的 O(Elog(E))  
>
> 散列  
散列适合不需要求最大最小值的数据存储，选择合适的h(key)，查找期望是O(1)  
散列是空间换时间的方法  
>> 1. 散列函数  
线性取余、数字分析、折叠、平方取中  
前三字符移位法、移位法，从末位开始计算 \c * 32^i,加和后取余。  
>> 2. 冲突处理  
. 开放定址法：线性探测(+i)、平方探测(±i^2)、双散列(i * h2())、再散列  
TableSize为4n + 3的素数，则平方探测可以探测整个table  
双散列 h2(key) = p - (key mod p)，p是素数    
装填因子α大于0.5 - 0.85时，扩大table，重新计算元素位置  
. 分离链接法：关键字都保存在同一单链表中  
>> 3. 性能分析  
装填因子α在0.5以下时各种冲突处理方式的平均查找次数基本相同  
开放定址法使用数组存储，效率高，但有聚集现象
>
> 排序算法  
>> 冒泡 这种算法包含swap操作，适用于排序基本有序的序列  
>> 插排 这种算法适合简单的排序操作，不需要swap操作，较为稳定  
>> 希尔 希尔序列-插排的升级版(sedgewick序列可以优化至O(n^7/6))  
>> 选择（不稳定排序）  
>> 快排及优化 （三者取小、数目少时改用插排）快排无法应对大量数据，递归调用栈内存有限制，数据量大宜选用外排序  
>> 归并 非常理想的排序方法，递归次数是恒定的O(logn)，稳定而且最坏事件复杂度O(nlogn)，  
>> 堆排序 实现较为复杂，适用要获取最小/大n个元素的场景，最坏时间复杂度也是O(nlogn)  
>> 桶排序  
>> 基数 O(d(n+a)) d为趟数，a为桶数，需要额外的O(nd)空间  
  
-------------

## 计算机网络

-------------

### 大纲

> 重点概念
>> 拓扑  
>> OSI模型  
>> TCP/IP模型  
>
> 物理层
>> 带宽
>>> 数字带宽、物理带宽、噪声 (耐2B、香)  
>>
>> 设备 (电缆、卫星、hub、repeater、transceiver)  
>> 复用技术 (FDM, TDM, CDMA)  
>> 调制技术
>>> 基带(不归零逆转、曼彻斯特、4B/5B)  
>>> 通带(调相位)  
>
> 数据链路层
>> 成帧方法  
>> 纠错与检错 (循环冗余校验、互联网校验)  
>> 设备 (网卡、交换机，交换方式-存储转发、直接交换、无分片交换64B)  
>> 协议
>>> 基本协议 (无限制--+有限缓存--+噪声)  
>>> 滑窗协议  
>>> 错误处理 (回退n帧、选择性重传)  
>>
>> MAC子层
>>> ALOHA协议 (立即发送、随机延迟再发)  
>>> 分隙ALOHA协议 (在时隙开始时发送，S最大1/e)  
>>> CSMA协议 (非持续、1-持续、p-持续 保持侦听，空闲则以p概率发送)  
>>> CSMA/CD协议 (冲突发送jam && 听自己)  
>>
>> 以太网 (使用CSMA/CD协议和二进制指数后退算法)  
>> 帧结构 (62 + 2 + 6B源 + 6B + 2B数据长 + data + 4B校验和)
>>> 11 - 802.3  10 - eternet  
>>> eternet帧64字节  
>>
>> 二层交换 (一帧到达..泛洪. MAC表.. 时间戳..)  
>> 生成树协议 (单点故障.. 广播风暴.. 根网桥..根端口..指定端口..)  
>
> 网络层
>> 报头 (版本、报头长、数据长、分片和标识、生存时间、地址、校验和等)  
>> 路由表 (直连路由、静态路由、动态路由)  
>> 路由选择协议
>>> DV (适合小型网络)  
>>> RIP (15跳，路由环)  
>>> LS (发现、设置、构造、发送、计算)  
>>> OSPF (带宽度量、无路由环、选举DR)  
>>
>> IP相关技术
>>> 子网规划  
>>> CIDR (按地址块分)  
>>> NAT (私有--公有，端口)  
>>> ICMP  
>>> ARP (IP--MAC)  
>>
>> 拥塞控制
>>> 抑制分组 逐跳抑制分组 载荷脱落 随机早期检验  
>>> 流量整形：漏桶、令牌桶  
>
> 传输层
>> UDP
>>> 源 + 目的 + 总长 + 校验和 = 4B  
>>
>> TCP
>>> 源 + 目的 + ACK + SEQ + (..6) + 窗口 + 校验和 + Urgent + Options  
>>> RST URG SYN FIN ACK PSH  
>>> 三次握手  
>>> 四次挥手  
>>> 拥塞控制 (全双工、累计一定数量才发送/接送，慢启动)  
>>> TCP与UCP (可靠性、资源消耗、一对多、使用场景)
