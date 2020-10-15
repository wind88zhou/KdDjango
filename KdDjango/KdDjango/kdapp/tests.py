# coding=utf-8(unittest.TestCase):
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


    def test1_5(self):
        r = requests.get(url ='http://paastest.kcssz.cloud.kingdee.com/omp_srv/paas/user/list',params ={"dev_id":"201367","page":"1","limit":"111","search":""})
        rjson = r.json()
        print(rjson)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(rjson["errcode"], 0)
        


#if __name__ =="__main__":
#    aa=unittest.main()
#    print(aa)
