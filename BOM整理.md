## window

### 窗口位置

* screenLeft, screenTop, screenX, screenY

    chrome和firefox表示浏览器窗口左上角坐标，后俩和前俩值相同
    IE中后俩没啥意思，screenTop显示的是页面可见区域到屏幕顶部的距离

* moveTo(x, y)  moveBy(x, y) resizeTo(w, h) resizeBy(w, h)

    移动/收缩窗口，默认chrome和firefox禁用了这个东西，IE可用

### 窗口大小

* innerWidth innerHeight outerWidth outerHeight

    前两个指的是视口大小（viewport，页面可见区域大小，肉眼看到的空白网页大小）
    后两个是浏览器窗口大小（包含工具栏）
    IE8不支持这些东西

    在firefox和IE中，即使是全屏状态下，innerWidth和outerWidth也不相等

* document.documentElement.clientWidth document.documentElement.clientHeight
    
    clientWidth一般等于innerWidth，但当有纵向滚动条时，innerWidth - clientWidth = 17
    另一组类似
  
**特别注意：**
在移动设备chrome浏览器中，如果页面元素超过了设备宽度，如375屏幕，元素达到了600，则innerWidth等于600，innerHeight会按比例增大
此时clientWidth == outerWidth == 375, 高亦然

