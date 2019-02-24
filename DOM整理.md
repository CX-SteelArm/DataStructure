## DOM1级操作

* 节点类型：
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

### 通用属性

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

* 节点通常属性

    属性：方便访问-同级的先后元素 / 子节点集合 / 第一个和最后一个子节点  
    `previousSibling / nextSibling/childNodes / firstChild / lastChild`  
    **需要注意的是在childNodes属性中部分浏览器包含了文本节点**  

    使用另一组属性`firstElementChild` `lastElementChild` `childElementCount` `nextElementSibling` `previousElementSibling`忽略文本节点(IE9+)
    使用children属性返回所有非文本子节点

* 节点通常操作方法：

    增：`appendChild(anode)`，注意如果anode已经存在，则相当于将其从原来的位置移动到新位置，返回anode
    `insertBefore(insert_node, ref_node)`
    删：`removeChild(anode)`
    改：`replaceChild(new, old)`
    复制：`cloneNode(BULL)`，BULL为true会复制所有子节点

* Element_node
  
    公认属性，如id、align等可以直接div.id访问
    `attributes` Attr节点集合，返回一个**NamedNodeMap**对象
    `getAttribute(), setAttribute(), removeAttribute()`

* Text_node
    创建：`document.createTextNode()`
    操作：包含添加、删除、插入、替换等操作,如appendData, deleteData(offset,count), insertData(offset, text), replaceData(offset,count,text)等
    `ele.normalize()`可以将多个连续文本节点合成一个

* Attr_node

    不建议直接访问它，使用getAttribute()等操作更好

### dom操作

操作表格

    提供了大量的API，如：
    caption, tFoot, tHead属性对应索引
    tBodies, rows分别对应HTMLCollection
    insertRow(pos), insertCell(pos)创建行和单元格
    cells保存tr元素的所有单元格

使用动态DOM集合

    NodeList，HTMLCollection，NamedNodeMap都是动态的dom集合，特点是可以即时计算，转化为数组使用，可节省大量开销。

## DOM扩展操作

* context.querySelector()

    返回null, element或者报错（输入了不正确的选择器）

* context.querySelectorAll()

    返回一个NodeList对象

* ele.matchesSelector()

    返回布尔值

* className和classList

    className返回Array
    classList返回DOMTokenList，使用`add(value), contains(value), remove(value), toggle(value)`方法操作
    如果不是完全重写class，建议使用后者

* 焦点管理

    document.activeElement获取正在获得焦点的元素引用
    （元素获得焦点的方法：加载、输入、js调用focus方法）

* readyState

    文档的状态，只有两个值：`loading, complete`

* 自定义数据

    HTML5新增功能，可以直接`<div data-text="???"></div>`也可以在dom元素上用`dom.dataset.xxx = ''`

* innerHTML outerHTML innerText outerText

    前两个是官方标准，后两个不推荐使用了
    outerHTML = innerHTML + 容器标签
    innerText = outerText

* insertAdjacentHTML('flag', ele)
    
    将元素作为同辈插入，不同flag作用不同

* contains()

    验证节点包含的三种方法：1. parent.contains(child); 2. parent.compareDocumentPosition(child); 3. 从child的parent级别一直往上找
    compareDocumentPosition()这个函数的返回值说明了两个节点的位置关系，不是只有父子这么简单

* 滚动

    scrollIntoView(BOOL): 默认true头对齐，false则脚对齐
    其他还有scrollIntoViewIfNeeded(), scrollByLines(), scrollByPages()等方法

## 操作样式表

### 访问内连样式

    任何支持style特征的HTML元素都有一个style属性，这个style对象是CSSStyleDeclaration的实例，**只包含内连样式**，IE这个属性叫做styleFloat
    div.style.cssText以字符串格式返回css代码
    操作：getPropertyValue(name), setPropertyValue(name, value, priority), removeProperty(name)

### 计算样式

    document.defalutView.getComputedStyle(ele, '伪元素') => CSSStyleDeclaration的实例
    注意 style.border不会返回有效值，因为这个属性同时设置了四个值（`style.borderLeftWidth`）
    IE只支持dom.currentStyle属性


## 元素位置、大小

* offsetWidth offsetHeight clientWidth clientHeight
  
    前两个是元素的内在大小，即`border+padding+content`
    后两个是客户区大小，不包含`border`

* offsetTop offsetLeft offsetParent

    offsetParent是css上的作为包含的元素（定位元素）
    offsetLeft值等于定位元素左内边框（不包含padding-left）至元素的内在区域的距离，例如 `（父padding-left + 子margin-left）`

* scrollWidth scrollHeight 

    滚动部分的尺寸，某些情况等于clientWidth clientHeight

* scrollTop scrollLeft

    滚动距离  document.documentElement.scrollTop = xx  可以设置滚动距离

* getBoundingClientRect() => {left: xx, top: xx, right: xx, bottom: xx}
    
    这个属性针对的是元素内在盒子（b+p+c)
    chrome,firefox,IE9-11返回下列，IE8不返回width和height

      left: 34
      right: 250
      top: 81.20000457763672
      bottom: 197.20000457763672
      width: 216
      height: 116


