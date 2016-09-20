__author__ = 'hq'
# -*- coding:utf-8 -*-

import urllib2
import re
import cookielib


class Spider:

    def __init__(self):
        self.fout =  open('C:Users\Administrator\Desktop\outputC.html', 'w')
        self.count = 1;

    def getDetailPage(self, infoURL):
        def makeMyOpener(head={'accept-encoding': 'deflate, sdch','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'zh-CN,zh;q=0.8','cookie':'q_c1=1d76440165d54cee87f9a3d5f3d01bf4|1473232048000|1473232048000; d_c0="AHCAcO_xgAqPTgfsPC8mqg0AqXUVJitclCw=|1473232048"; _za=7c5cb4f0-d690-457f-8b22-ac97d3305804; l_cap_id="YzE4YjcxZDhhNzVkNDk1ZmE5YjJjZmIyNGM0YjIzOTM=|1473311767|0b30233791a7fa148320c1bde784824ea39f21de"; cap_id="OTkxYjBhMTNjZmViNGVhOTllNjAwNTNjZmY0ZjNlZDE=|1473311767|50e82be4263de5cf47f1798655cf24c7da2d4043"; _zap=fbdc3777-ea0b-4530-8d47-aea7453be9cb; login="Njg0OTM2MGMxOGRmNDQxYzhmZjBkZGI1ZmQ5YTBhMjY=|1473311796|6a40fce4d441fb89ac1fed6c322eb60eb195a286"; _xsrf=0feeb8963f1f4e66ef16491f0d3fb06a; __utmt=1; a_t="2.0ABCK1fRi6wgXAAAAcioDWAAQitX0YusIAHCAcO_xgAoXAAAAYQJVTTWB-FcArpcd-rMbFkxOB73P8iVOtLKaO3MlWYzwydvyONqiiJpXybSAL6PjSA=="; z_c0=Mi4wQUJDSzFmUmk2d2dBY0lCdzdfR0FDaGNBQUFCaEFsVk5OWUg0VndDdWx4MzZzeHNXVEU0SHZjX3lKVTYwc3BvN2N3|1474010482|7cdb95e16afe24a675b215a14ec6d0eb4f67ccb9; __utma=51854390.368633658.1474010384.1474010384.1474010384.1; __utmb=51854390.13.9.1474010384; __utmc=51854390; __utmz=51854390.1474010384.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/21479334; __utmv=51854390.100-1|2=registration_date=20151028=1^3=entry_date=20151028=1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}):
            cookie = cookielib.MozillaCookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
            header = []
            for key, value in head.items():
                elem = (key, value)
                header.append(elem)
            opener.addheaders = header
            return opener

        oper = makeMyOpener()
        uop = oper.open(infoURL)
        data = uop.read()
        #print data
        return data

    def getAllImgPageURL(self,page):
        #print page
        pattern = re.compile('<div class="zm-item-rich-text expandable js-collapse-body.*?data-entry-url="(.*?)">',re.S)
        items = re.findall(pattern, page)
        imgPageURL = []

        for item in items:
            imgPageURL.append(item)
            #print item

        return imgPageURL

    def getAllImgURL(self,imgPageURLs):
        imgURLs = []
        for url in imgPageURLs:
            #print url
            pageData = self.getDetailPage('https://www.zhihu.com/'+url)
            pattern = re.compile('<img .*?src="(.*?)".*?class="origin_image zh-lightbox-thumb lazy".*?>',
                                 re.S)
            items = re.findall(pattern, pageData)

            for item in items:
                imgURLs.append(item)
                #print item
        return imgURLs

    def writeData(self, contents,fout):

        self.fout.write("<html>")
        self.fout.write("<body>")

        for item in contents:
                self.count = self.count+1
                self.fout.write("<img src='%s'/>" % item)
        self.fout.write("</body>")
        self.fout.write("</html>")
        print self.count

    def start(self):

         for i in range(15,30):
             print i
             page = spider.getDetailPage('https://www.zhihu.com/collection/61913303?page=' + str(i))
             imgPageURL = self.getAllImgPageURL(page)
             imgurls = self.getAllImgURL(imgPageURL)
             self.writeData(imgurls,self.fout)

         self.fout.close()


spider = Spider()
spider.start()
