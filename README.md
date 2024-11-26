# 配置python环境
我使用的python版本是3.8，配置环境的话cd到文件夹所在位置运行 <br>
```
pip install -r requirements.txt
```
其中selenium需要配合chromedriver使用，可以在cmd中运行指令```chromedriver```查看自己电脑上的chromedriver是否安装好，但是有可能发生chromedriver与你当前电脑上的chrome版本不匹配的问题，需要重新安装一下chromedriver，可以参照这篇博客https://blog.csdn.net/weixin_52122271/article/details/130885214
# 将爬取主题对应的网页的信息并格式化储存到json文件中
运行spider.py，记得将代码中的url换成自己主题的url <br>
```url = "https://solutionportfolio.net.sap/bcm/industry/HEALTH"``` <br>
如果出现运行中断的情况，可能由两种原因造成：<br>
1. 网络不稳定（页面跳出来后网页并没有加载完全）- 这种情况下需要在shadowspider.py中将```sleep(2)```的时间调大一点，使得睡眠的时间足够网页加载完全。
2. 被限流 - 这种情况只需要重新运行一下spider.py就行了，重新运行会接着之前已经爬好的进度继续爬取。
<br>
总体用时 - 2h

# 调取谷歌翻译API并将翻译后的内容转成docx文档
运行json2docx.py，这里面将爬好的json文件分为几个部分保存在temp文件夹中，然后将每个temp.json转成temp.docx最后合并成一个完整的文档，这样做是为了避免中途谷歌翻译API限流卡死导致之前翻译的功亏一篑。如果发现终端长时间不打印新的翻译结果，可以停止运行，然后查看temp文件夹中生成到第几个docx了，
在代码<br>
```
num = split_json_to_files(json_file_path)
for i in range(0, num):
    subjson_file_path = f"temp/temp{i}.json"
    json_to_docx(i, subjson_file_path, f"temp/temp{i}.docx")
```
<br>
的for i in range(0, num):中将0改成下一个需要生成的docx文档的index即可。 <br>
<br>
总体用时 - 1h
<br>
<br>
最后的merged.docx就是我们需要的文档了，里面已经设好了一二三四级标题，自己在word里改一改样式就行了。
