import requests
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from funLife.models import BookInfo
# Create your views here.


def funlife(request):
    return JsonResponse({"errcode": 00, "description": "Fun life coming!"})


def showtep(request):
    return render(request, 'funlife/muban.html')


def addapi(request):
    if request.method == "POST":
        bookInfo = BookInfo.objects.all().values()
        data = 'POST方法data'
        data1 = list(bookInfo)
        return render(request, 'funlife/addapi.html', {'data': data, 'data1': data1})
    else:
        data = 'other_data'
        data1 = 'other_data1'
        return render(request, 'funlife/addapi.html', {'data': data, 'data1': data1})


def index(request):
    if request.method == "POST":
        # # 测试请求数据：
        api_name = request.POST.get('api_name')
        api_url = request.POST.get('api_url')
        api_method = request.POST.get('api_method')
        api_headers = request.POST.get('api_headers')
        api_params = request.POST.get('api_params')

        # # 测试数据
        testdata = {'接口名称': api_name, '请求地址': api_url, '请求方式': api_method,
                    '请求头': api_headers, '请求参数': api_params}

        # 定义测试参数：
        # base_url = 'http://172.25.1.70:9606/admin'  # 开发
        base_url = 'http://172.25.1.242:33719/kcgw/admin'  # 测试
        service_name = 'PPPPPapigwservernamezf10uPPPPP'
        app_key = 'apptestkeyzf10u1'

        # 接口请求方式：
        def aapigw_url(method1, url1, params1, headers1):
            if method1 is 'post' or method1 is 'POST':
                post_r = requests.post(
                    base_url + url1, data=params1, headers=headers1)
                print("[POST] : " + url1 + "\n" + post_r.text + '\n' +
                      "--------------------------------------------")
            elif method1 is 'get' or method1 is 'GET':
                get_r = requests.get(
                    base_url + url1, params=params1, headers=headers1)
                print("[GET] : " + url1 + "\n" + get_r.text + '\n' +
                      "-------------------------------------------")
            else:
                print("方法错误！")

        print("####"*50)
        #  待测接口：
        # GET /ping
        aapigw_url('get', '/ping', {}, {})
        # /service/add 新增分组
        aapigw_url('post', '/service/add',
                   json.dumps({'service_path': service_name, 'service_id': 'service_id', 'secret': 'secretsecret'}), {})
        # /service/add 新增分组
        aapigw_url('post', '/service/add',
                   json.dumps({'service_path': service_name, 'service_id': 'service_id', 'secret': 'secretsecret'}), {})
        # GET  /service/all  获取所有的分组
        aapigw_url('get', '/service/list', {}, {})
        #  /api/add 添加一个新的api
        aapigw_url('post', '/api/add', json.dumps({"service_name": service_name,
                                                   "method": "GET",
                                                   "path": "/newapipath",
                                                   "backend_path": "/newapibackend_path",
                                                   "backend_method": "GET",
                                                   "backend_timeout": 20,
                                                   "backend_scheme": "http",
                                                   "balance_strategy": "rr",
                                                   "backend_host": [{"address": "www.baidu.com",
                                                                     "weight": 1}]}),
                   {})
        # GET  /api/list 获取分组下的所有apis
        aapigw_url('get', '/api/list', {'service_name': service_name}, {})
        # 获取 api_id    ******
        rrrr1 = requests.get(base_url+'/api/list',
                             params={'service_name': service_name})
        api_ids = rrrr1.json()['data'][0]['api_def']['id']  # 获取 api_id
        # /api/update  更新api
        aapigw_url('post', '/api/update', json.dumps({'api_id': api_ids,
                                                      'service_name': service_name,
                                                      'method': 'GET',
                                                      'path': '/newapipathaaa',
                                                      'backend_method': 'GET',
                                                      'balance_strategy': 'rr',
                                                      'backend_path': '/newapibackend_pathaaa',
                                                      'backend_timeout': 100,
                                                      'backend_scheme': 'http',
                                                      'backend_host': [{"address": "www.baiduaaa.com",
                                                                        "weight": 2}]}),
                   {})
        # /api/multi_add 批量创建api
        aapigw_url('post', '/api/multi_add', json.dumps({'apis_info': [{'api_id': 'apiids0000001',
                                                                        'service_name': service_name,
                                                                        'method': 'GET',
                                                                        'path': '/apiids0000001path',
                                                                        'backend_method': 'GET',
                                                                        'balance_strategy': 'rr',
                                                                        'backend_path': '/apiids0000001backend_path',
                                                                        'backend_timeout': 111,
                                                                        'backend_scheme': 'http',
                                                                        'backend_host': [{"address": "www.baiduaaaapi1.com",
                                                                                          "weight": 2}]},
                                                                       {'api_id': 'apiids0000001',
                                                                        'service_name': service_name,
                                                                        'method': 'GET',
                                                                        'path': '/apiids0000001path',
                                                                        'backend_method': 'GET',
                                                                        'balance_strategy': 'rr',
                                                                        'backend_path': '/apiids0000001backend_pathaaa',
                                                                        'backend_timeout': 111,
                                                                        'backend_scheme': 'http',
                                                                        'backend_host': [{"address": "www.baiduaaaapi1.comaaa",
                                                                                          "weight": 3}]},
                                                                       {'api_id': 'apiids0000002',
                                                                        'service_name': service_name,
                                                                        'method': 'GET',
                                                                        'path': '/apiids0000002path',
                                                                        'backend_method': 'GET',
                                                                        'balance_strategy': 'rr',
                                                                        'backend_path': '/apiids0000002backend_path',
                                                                        'backend_timeout': 222,
                                                                        'backend_scheme': 'http',
                                                                        'backend_host': [{"address": "www.baiduaaaap2.com",
                                                                                          "weight": 2}]}]}), {})
        # GET  /api/list 获取分组下的所有apis
        aapigw_url('get', '/api/list', {'service_name': service_name}, {})
        # GET  /app/list 获取所有App列表
        aapigw_url('get', '/app/list', {}, {})
        # /app/add 添加一个应用
        aapigw_url('post', '/app/add',  json.dumps({'app_key': app_key,
                                                    'auth_config': "{\"ak_sk_app_key\": \"ak_sk_app_key\",\"ak_sk_app_secret\": \"ak_sk_app_secret\"}",
                                                    'auth_type': 'aksk'}), {})
        # GET  /app/list 获取所有App列表
        aapigw_url('get', '/app/list', {}, {})
        # /app/update 更新应用/更新认证配置
        aapigw_url('post', '/app/update', json.dumps({'app_key': app_key,
                                                      'auth_config': "{\"ak_sk_app_key\": \"\",\"ak_sk_app_secret\": \"ak_sk_app_secretaaaaaa\"}",
                                                      'auth_type': 'aksk'}), {})
        # GET  /app/list 获取所有App列表
        aapigw_url('get', '/app/list', {}, {})
        # /subscribe/add 添加订阅关系
        aapigw_url('post', '/subscribe/add', json.dumps({'subscribe_list': {
                   'apiids0000001': ['apptestkeyzf10u1'], 'apiids0000002': ['apptestkeyzf10u1']}}), {})
        # /subscribe/del 删除订阅关系
        aapigw_url('post', '/subscribe/del', json.dumps({'subscribe_list': {
                   'apiids0000001': ['apptestkeyzf10u1'], 'apiids0000002': ['apptestkeyzf10u1']}}), {})

        # /app/del 删除应用
        aapigw_url('post', '/app/del', {'app_key': app_key}, {})
        # /api/del 删除api
        aapigw_url('post', '/api/del', json.dumps({'delete_list': {
                   'apigwservernamezf10u': ['apiids0000002', 'apiids0000001', 'apiids0000003', api_ids]}}), {})
        #    {'service_name': service_name, 'api_ids': api_ids}, {})
        # GET /service/del 删除服务
        aapigw_url('get', '/service/del',
                   {'service_name': service_name}, {})

        return render(request, 'funlife/index.html', {'testdata': testdata, 'result': 'result'})
    else:
        return render(request, 'funlife/index.html')

#  接口测试入口页
def home(request):
    return render(request, 'funlife/home.html')

# 接口测试请求数据及结果展示
def resultShow(request):
    api_name = request.POST.get('api_name')
    api_url = request.POST.get('api_url')
    api_method = request.POST.get('api_method')
    api_headers = request.POST.get('api_headers')
    api_params = request.POST.get('api_params')
    
    if api_url == '' or api_method == ''   :
        return HttpResponse("参数错误！")
    else:
         # 接口请求方式：
        if api_method == 'post' or api_method == 'POST':
            post_r = requests.post(api_url, data=api_params, headers=api_headers)
            result = post_r.text
        elif api_method == 'get' or api_method == 'GET':
            if api_params=='':
                get_r = requests.get(api_url, params=api_params, headers=api_headers) # params 为空，不做转换
                result = get_r.text
            else:
                get_r = requests.get(api_url, params=eval(api_params), headers=api_headers) # params 需str转字典
                result = get_r.text
        else:
            return HttpResponse("参数错误！")

        return render(request, 'funlife/resultShow.html', {'result': result,'api_name': api_name, 'api_url': api_url, 'api_method': api_method,
                    'api_headers': api_headers, 'api_params': api_params})

def htmlstudy(request):
    return render(request,'funlife/htmlstudy.html')

def mainpage(request):
    usename = request.POST.get('usename')
    password = request.POST.get('password')
    gender = request.POST.get('gender')
    like = request.POST.get('like')
    site = request.POST.get('site')
    about = request.POST.get('about')

    if usename =='' or  password=='' or like=='' or site=='' or about =='':
        data = "参数传递不完整"
    else:

        data ={'usename':usename ,'password':password,'gender':gender,'like':like,'site':site,'about':about}
    return render(request,'funlife/mainpage.html',{'data':data})

def css_study(request):
    return render(request,'funlife/css_study.html')

def form_study(request):
    return render(request,'funlife/form_study.html')

def box_model_study(request):
    return render(request,'funlife/box_model_study.html')

def js_study(request):
    return render(request,'funlife/js_study.html')

def bootstrap_study(request):
    return render(request,'funlife/bootstrap_study.html')