# coding=utf-8
from django.test import TestCase

# Create your tests here.
import requests,json,unittest
import time


par = {"client_id": "203986","client_secret": "fc6f18c45fa248b1e17f13d5797561c7"}

class apigwtest(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass

    #测试不同转发方式
    def test1_1(self):
        '''不同的转发方式-GET'''
        url="http://bj1-api.kingdee.com/zhuanfamethod/getmethod"
        r = requests.get(url, params=par)
        rjson = r.json()
        print(rjson)
        self.assertEqual(r.status_code,200)
        self.assertIn((rjson["data"])["enviroment"], "formal")
        self.assertEqual(rjson["errcode"], 0)
        self.assertEqual(rjson["method"], "GET")
        self.assertEqual(rjson["node"], "load balance")
        self.assertEqual(rjson["pathtype"], "absolute path")

    def test1_2(self):
        '''不同的转发方式-POST'''
        url="http://bj1-api.kingdee.com/zhuanfamethod/post"
        r = requests.post(url, params=par)
        rjson = r.json()
        print(rjson)
        self.assertEqual(r.status_code, 200)
        self.assertIn((rjson["data"])["enviroment"], "formal")
        self.assertEqual(rjson["errcode"], 0)
        self.assertEqual(rjson["method"], "POST")
        self.assertEqual(rjson["node"], "load balance")
        self.assertEqual(rjson["pathtype"], "absolute path")

    def test1_3(self):
        '''不同的转发方式-PUT'''
        url="http://bj1-api.kingdee.com/zhuanfamethod/put"
        r = requests.put(url, params=par)
        rjson = r.json()
        print(rjson)
        self.assertEqual(r.status_code, 200)
        self.assertIn((rjson["data"])["enviroment"], "formal")
        self.assertEqual(rjson["errcode"], 0)
        self.assertEqual(rjson["method"], "PUT")
        self.assertEqual(rjson["node"], "load balance")
        self.assertEqual(rjson["pathtype"], "absolute path")

    def test1_4(self):
        '''不同的转发方式-DELETE'''
        url="http://bj1-api.kingdee.com/zhuanfamethod/delete"
        r = requests.delete(url, params=par)
        rjson = r.json()
        print(rjson)
        self.assertEqual(r.status_code, 200)
        self.assertIn((rjson["data"])["enviroment"], "formal")
        self.assertEqual(rjson["errcode"], 0)
        self.assertEqual(rjson["method"], "DELETE")
        self.assertEqual(rjson["node"], "LoadBalance")
        self.assertEqual(rjson["pathtype"], "absolutePath")


if __name__ =="__main__":
    aa=unittest.main()
    print(aa)
