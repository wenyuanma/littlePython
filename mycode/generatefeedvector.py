# -*- coding: utf-8 -*-
import feedparser
import re


def getwordcounts(url):
    print "%s" % url
    d = feedparser.parse(url)
    wordcount = {}
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wordcount.setdefault(word, 0)
            wordcount[word] += 1
    return url, wordcount


def getwords(html):
    txt = re.compile(r'<[^>]+>').sub("", html)
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    return [word.lower() for word in words if word != '']

apcount = {}
wordcounts = {}
feedlist = [line for line in file('feedlist.txt')]
for feedurl in feedlist:
    title, wc = getwordcounts(feedurl)
    wordcounts[title] = wc
    for word, count in wc.items():
        apcount.setdefault(word, 0)
        if count > 1:
                # 统计每个单词有多少个url有该单词
            apcount[word] += 1


# 要对单词进行筛选 出现在每个文档中的不要，出现在很少文档中的不要
wordlist = []
for w, bc in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.5:
        wordlist.append(w)
out = file('blogdata.txt', 'w')
# 写文件第一行
out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')
# 接下来，每一行代表一个blog的单词向量
for blog, wc in wordcounts.items():
    out.write(blog)
    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')
