# -*- coding: utf-8 -*-
import scrapy

"""需求：对百度翻译中指定词条的翻译结果进行获取"""


class PostdemoSpider(scrapy.Spider):
    name = 'postdemo'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        """
        该方法是父类中的一个方法，可以对start_urls列表中的元素进行get请求的发送
        :return:
        """
        # 发起post请求：
        # 1.将Request方法中method参数赋值为post
        # 2.FormRequest（）方发可以发起post请求
        print('start..')
        # post请求参数
        data = {'kw': 'dog'}
        # 发起post请求
        for url in self.start_urls:
            # formdata：post请求参数
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def parse(self, response):
        print(response.text)
