\#\# 1. 节点关系

1.1. 父\(Parent\)

1.2. 子\(Children\)

1.3. 同胞\(Sibling\)

1.4. 先辈\(Ancestor\)

1.5. 后代\(Descendant\)

\#\# 2. 选取节点

\|表达式 \|    说明\|

\|----\|----\|

\|nodename\|     选取此节点的所有子节点。

\|/ \|     从根节点选取。

\|// \|     从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。

\|. \|    选取当前节点。

\|.. \|    选取当前节点的父节点。

\|@ \|    选取属性。\|

\#\# 3.  技巧

\#\#\# 3.1. XPATH如何选择不包含某一个属性的节点?

选择包含某一特定属性的节点，可以使用例如//tbody/tr\[@class\]来选择。那么不含某属性的节点如何用xpath取得呢？

例如排除一个属性的节点可以使用//tbody/tr\[not\(@class\)\]来写，排除一个或者两个属性可以使用//tbody/tr\[not\(@class or @id\)\]来选择。

\#\# 4. 例

\`\`\`

from lxml import etree

html = """

&lt;div&gt;

```
&lt;ul&gt;

     &lt;li class="item-0"&gt;&lt;a href="link1.html"&gt;first item&lt;/a&gt;&lt;/li&gt;

     &lt;li class="item-1"&gt;&lt;a href="link2.html"&gt;second item&lt;/a&gt;&lt;/li&gt;

     &lt;li class="item-inactive"&gt;&lt;a href="link3.html"&gt;&lt;span class="bold"&gt;third item&lt;/span&gt;&lt;/a&gt;&lt;/li&gt;

     &lt;li class="item-1"&gt;&lt;a href="link4.html"&gt;fourth item&lt;/a&gt;&lt;/li&gt;

     &lt;li class="item-0"&gt;&lt;a href="link5.html"&gt;fifth item&lt;/a&gt;

 &lt;/ul&gt;
```

&lt;/div&gt;

"""

\#利用 parse 方法来读取文件

f = open\("hello.html", "r"\)

html = f.read\(\)

root = etree.HTML\(html\)

\#报错可以尝试 etree.HTML\(html.decode\('utf-8'\)\)

\#网页获取

request.get\(url\).text

\#初始化

root = etree.HTML\(html\)

contents = etree.tostring\(root, pretty\_print=True\) \#

\#获取所有的 &lt;li&gt; 标签

tmp = root.xpath\("//li"\)

\#获取 &lt;li&gt; 标签的所有 class

tmp = root.xpath\("//li/@class"\)

\#获取 &lt;li&gt; 标签下 href 为 link1.html 的 &lt;a&gt; 标签

tmp = root.xpath\('//li/a\[@href="link1.html"\]'\)

\#获取 &lt;li&gt; 标签下的所有 &lt;span&gt; 标签,

\#因为 / 是用来获取子元素的，而 &lt;span&gt; 并不是 &lt;li&gt; 的子元素，所以，要用双斜杠

tmp = root.xpath\("//li//span"\)

\#获取 &lt;li&gt; 标签下的所有 class，不包括 &lt;li&gt;

tmp = root.xpath\('//li/a//@class'\)

\#获取最后一个 &lt;li&gt; 的 &lt;a&gt; 的 href

tmp = root.xpath\('//li\[last\(\)\]/a/@href'\)

\#获取倒数第二个元素的内容

tmp = root.xpath\('//li\[last\(\)-1\]/a'\)

\#获取 class 为 bold 的标签名

tmp = root.xpath\('//\*\[@class="bold"\]'\)

print\(tmp\)

\`\`\`

\`\`\`

from lxml import etree

html='''

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head lang="en"&gt;

```
&lt;meta charset="UTF-8"&gt;

&lt;title&gt;测试-常规用法&lt;/title&gt;
```

&lt;/head&gt;

&lt;body&gt;

&lt;div id="content"&gt;

```
&lt;ul id="useful"&gt;

    &lt;li&gt;这是第一条信息&lt;/li&gt;

    &lt;li&gt;这是第二条信息&lt;/li&gt;

    &lt;li&gt;这是第三条信息&lt;/li&gt;

&lt;/ul&gt;

&lt;ul id="useless"&gt;

    &lt;li&gt;1不需要的信息&lt;/li&gt;

    &lt;li&gt;2不需要的信息&lt;/li&gt;

    &lt;li&gt;3不需要的信息&lt;/li&gt;

&lt;/ul&gt;



&lt;div id="url"&gt;

    &lt;a href="属性1"&gt;这个不属于属性值&lt;/a&gt;

    &lt;a href="属性2" href2="属性3"&gt;这个也不是属性值&lt;/a&gt;

    &lt;a href3="attribute"&gt;3也不是属性值&lt;/a&gt;
```

&lt;/div&gt;

&lt;/div&gt;

&lt;/body&gt;

&lt;/html&gt;

'''

root = etree.HTML\(html\)

selector = root

\#提取文本信息

content=selector.xpath\('//ul\[@id="useful"\]/li/text\(\)'\)

content2 = selector.xpath\("//a/text\(\)"\)

content3 = selector.xpath\("//a\[@href\]/text\(\)"\) \#/text\(\)就像bs4里的string

\#提取属性

content4 = selector.xpath\("//a/@href"\)

content4 = selector.xpath\("//a/@href2"\)

content5=selector.xpath\('//a\[@href3="attribute"\]/text\(\)'\)

\#

print\(content5\)

\`\`\`

\`\`\`

from lxml import etree

import requests

url="[https://www.qiushibaike.com/](https://www.qiushibaike.com/)"

r=requests.get\(url\)

mytree=etree.HTML\(r.text\)

\`\`\`

\`\`\`

f = open\("color\_mapping\_file.html", "r"\)

html = f.read\(\)

root = etree.HTML\(html\)

tmp = root.xpath\('//li/a'\)\[0\]

print\(tmp.attrib\)

print\(tmp.text\)

print\(tmp.values\(\)\)

print\("+++++++++++++++++++++++++++"\)

tmp = root.xpath\('//li//a'\)

\#print\(tmp.attrib\)

print\("+++++++++++++++++++++++++++"\)

tmp = root.xpath\('//a\[@target="\_map"\]'\)

\`\`\`

\`\`\`

page='''

&lt;html&gt;

&lt;head&gt;

&lt;meta name="content-type" content="text/html; charset=utf-8" /&gt;

&lt;title&gt;友情链接查询 - 站长工具&lt;/title&gt;

&lt;!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc --&gt;

&lt;meta name="Keywords" content="友情链接查询" /&gt;

&lt;meta name="Description" content="友情链接查询" /&gt;

&lt;/head&gt;

&lt;body&gt;

&lt;h1 class="heading"&gt;Top News&lt;/h1&gt;

&lt;p style="font-size: 200%"&gt;World News only on this page&lt;/p&gt;

Ah, and here's some more text, by the way.

&lt;p&gt;... and this is a parsed fragment ...&lt;/p&gt;

&lt;a href="[http://www.cydf.org.cn/](http://www.cydf.org.cn/)" rel="nofollow" target="\_blank"&gt;青少年发展基金会&lt;/a&gt;

&lt;a href="[http://www.4399.com/flash/32979.htm](http://www.4399.com/flash/32979.htm)" target="\_blank"&gt;洛克王国&lt;/a&gt;

&lt;a href="[http://www.4399.com/flash/35538.htm](http://www.4399.com/flash/35538.htm)" target="\_blank"&gt;奥拉星&lt;/a&gt;

&lt;a href="[http://game.3533.com/game/](http://game.3533.com/game/)" target="\_blank"&gt;手机游戏&lt;/a&gt;

&lt;a href="[http://game.3533.com/tupian/](http://game.3533.com/tupian/)" target="\_blank"&gt;手机壁纸&lt;/a&gt;

&lt;a href="[http://www.4399.com/](http://www.4399.com/)" target="\_blank"&gt;4399小游戏&lt;/a&gt;

&lt;a href="[http://www.91wan.com/](http://www.91wan.com/)" target="\_blank"&gt;91wan游戏&lt;/a&gt;

&lt;/body&gt;

&lt;/html&gt;

'''

tag\_a = page.xpath\('/html/body/a'\)

print\(tag\_a\)

\# html 下的 body 下的所有 a

tag\_a = page.xpath\('/html/body//a'\)

print\(tag\_a\)

\# html 下的 body 下的所有 a

\`\`\`

\*\*“/”\*\*分隔上下级，最开始是文件本身（而不是html），文件下一级才是html;

\*\*/html/body//a\*\*

\*\*/html/body/a\*\*

\#\#\#　３.1. 获取节点（标签）属性

\`\`\`

tag\_a = page.xpath\('/html/body//a'\)

for a in tag\_a:

\#获取属性

```
print\(a.attrib\)
```

\#获取某一属性

```
print\(a.get\("href"\)\)

print\(a.text\)
```

\`\`\`

\#\#\# 3.2. 利用属性筛选标签

\`\`\`

\# 直接定位到&lt;h1 class="heading"&gt;Top News&lt;/h1&gt;

hs = page.xpath\('//h1\[@class="heading"\]'\)

hs = page.xpath\('/html/body/h1\[@class="heading"\]'\)

for h in hs:

```
print\(h.values\(\)\)

print\(h.text\)
```

\`\`\`

\#\#\# 3.3. 筛选任意标签

\`\`\`

ts = page.xpath\('/\*'\)

for t in ts:

```
print\(t.tag\)

\# 打印:html

\# html是文件的唯一下一级标签
```

ts = page.xpath\('/html/\*'\)

for t in ts:

```
print\(t.tag\)

\# 打印:body

\# body是html的唯一下一级标签
```

ts = page.xpath\('/html//\*'\)

for t in ts:

```
print\(t.tag\)

\# 打印：body、p、meta、title、meta、meta、h1、p等等
```

\`\`\`

\#\#\# 3.4.

preceding-sibling::前缀表示同一层的上一个节点。

following-sibling::前缀表示同一层的下一个节点。

\`\`\`

sbs = page.xpath\('//body//following-sibling::a'\)

for sb in sbs:

```
print\(sb.tag\)

\# 打印：a a a a a a ...
```

sbs = page.xpath\('//body/h1/following-sibling::\*'\)

for sb in sbs:

```
print\(sb.tag\)

\# h1 下，所有 h1 同级的子节点（标签）

\# 打印：p p a a a a ...
```

\`\`\`

\#\#\#

![](/assets/KEGG_object.jpg)

