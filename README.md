# -网络爬虫总结

>>主要是对这段时间碰到的爬虫方法的梳理后期逐步更近新的方法，在爬取数据的过程中，从最简单的静态网页的爬取到需要登录的动态网页的爬取<br>
网页爬虫的原理其实是对网页DOM对象中的各个标签元素进行有效的提取，相关的元素的如何选择根据不同工具的不同而有差异，但是一些基本的选择规范
如python perl的正则表达式，css选择器等等是其选择的基础，爬取动态页面需要了解js等前端页面的相关技术规范<br>
 
## 简单的入门爬虫工具Beautiful Soup
>>这个是一个可以从HTML或XML文件中提取数据的Python库，相关的使用请参考现有的文档[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#)<br>
这种数据爬取的方法可以整合到其他爬虫框架中，但此工具爬取效率相比其他方法不是很高，书写比较复杂<br>


## 模拟网页登陆
>>有的网页你要爬取相关信息的时候必须要登陆<br>模拟登陆界面的表单的填值点击操作（selenium PhantomJS模拟浏览器登录，spalsh等<br>通过HTTP的POST请求登录<br>直接加载cookies登录<br>
前面两种登陆的方式很容易碰到验证码问题，解决这种方法是利用某些第三方的打码平台或者图像识别的三方算法库（验证码不是图像模式就不好使了），参考链接[模拟登陆](https://blog.csdn.net/u014134180/article/details/55508229)<br>

## scrapy框架介绍
>>将爬取的数据格式，爬取后数据的处理，爬取数据等等其他的过程分离开来，具体的使用方法参考官方文档[scrapy](http://scrapy-chs.readthedocs.io/zh_CN/latest/intro/tutorial.html)<br>
工作原理可参考[原理介绍](http://python.jobbole.com/86405/)<br>


## splash介绍
>>此工具相当于一个轻量级的浏览器，功能很强大，主要是要爬取的页面进行一个渲染，去掉一些不必要的页面元素或者添加对页面进行一些预操作（当然是动态页面），加快提取效率<br>
参考官方文档[splash](http://splash.readthedocs.io/en/stable/scripting-ref.html#splash-jsfunc)<br>
