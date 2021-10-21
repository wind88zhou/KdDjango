import requests
import json, jsonpath
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from .models import BookInfo
import base64
import time
import calendar
import random


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

        print("####" * 50)
        #  待测接口：
        # GET /ping
        aapigw_url('get', '/ping', {}, {})
        # /service/add 新增分组
        # aapigw_url('post', '/service/add',
        #            json.dumps({'service_path': service_name, 'service_id': 'service_id', 'secret': 'secretsecret'}), {})
        # # /service/add 新增分组
        # aapigw_url('post', '/service/add',
        #            json.dumps({'service_path': service_name, 'service_id': 'service_id', 'secret': 'secretsecret'}), {})
        # # GET  /service/all  获取所有的分组
        # aapigw_url('get', '/service/list', {}, {})
        # #  /api/add 添加一个新的api
        # aapigw_url('post', '/api/add', json.dumps({"service_name": service_name,
        #                                            "method": "GET",
        #                                            "path": "/newapipath",
        #                                            "backend_path": "/newapibackend_path",
        #                                            "backend_method": "GET",
        #                                            "backend_timeout": 20,
        #                                            "backend_scheme": "http",
        #                                            "balance_strategy": "rr",
        #                                            "backend_host": [{"address": "www.baidu.com",
        #                                                              "weight": 1}]}),
        #            {})
        # # GET  /api/list 获取分组下的所有apis
        # aapigw_url('get', '/api/list', {'service_name': service_name}, {})
        # # 获取 api_id    ******
        # rrrr1 = requests.get(base_url+'/api/list',
        #                      params={'service_name': service_name})
        # api_ids = rrrr1.json()['data'][0]['api_def']['id']  # 获取 api_id
        # # /api/update  更新api
        # aapigw_url('post', '/api/update', json.dumps({'api_id': api_ids,
        #                                               'service_name': service_name,
        #                                               'method': 'GET',
        #                                               'path': '/newapipathaaa',
        #                                               'backend_method': 'GET',
        #                                               'balance_strategy': 'rr',
        #                                               'backend_path': '/newapibackend_pathaaa',
        #                                               'backend_timeout': 100,
        #                                               'backend_scheme': 'http',
        #                                               'backend_host': [{"address": "www.baiduaaa.com",
        #                                                                 "weight": 2}]}),
        #            {})
        # # /api/multi_add 批量创建api
        # aapigw_url('post', '/api/multi_add', json.dumps({'apis_info': [{'api_id': 'apiids0000001',
        #                                                                 'service_name': service_name,
        #                                                                 'method': 'GET',
        #                                                                 'path': '/apiids0000001path',
        #                                                                 'backend_method': 'GET',
        #                                                                 'balance_strategy': 'rr',
        #                                                                 'backend_path': '/apiids0000001backend_path',
        #                                                                 'backend_timeout': 111,
        #                                                                 'backend_scheme': 'http',
        #                                                                 'backend_host': [{"address": "www.baiduaaaapi1.com",
        #                                                                                   "weight": 2}]},
        #                                                                {'api_id': 'apiids0000001',
        #                                                                 'service_name': service_name,
        #                                                                 'method': 'GET',
        #                                                                 'path': '/apiids0000001path',
        #                                                                 'backend_method': 'GET',
        #                                                                 'balance_strategy': 'rr',
        #                                                                 'backend_path': '/apiids0000001backend_pathaaa',
        #                                                                 'backend_timeout': 111,
        #                                                                 'backend_scheme': 'http',
        #                                                                 'backend_host': [{"address": "www.baiduaaaapi1.comaaa",
        #                                                                                   "weight": 3}]},
        #                                                                {'api_id': 'apiids0000002',
        #                                                                 'service_name': service_name,
        #                                                                 'method': 'GET',
        #                                                                 'path': '/apiids0000002path',
        #                                                                 'backend_method': 'GET',
        #                                                                 'balance_strategy': 'rr',
        #                                                                 'backend_path': '/apiids0000002backend_path',
        #                                                                 'backend_timeout': 222,
        #                                                                 'backend_scheme': 'http',
        #                                                                 'backend_host': [{"address": "www.baiduaaaap2.com",
        #                                                                                   "weight": 2}]}]}), {})
        # # GET  /api/list 获取分组下的所有apis
        # aapigw_url('get', '/api/list', {'service_name': service_name}, {})
        # # GET  /app/list 获取所有App列表
        # aapigw_url('get', '/app/list', {}, {})
        # # /app/add 添加一个应用
        # aapigw_url('post', '/app/add',  json.dumps({'app_key': app_key,
        #                                             'auth_config': "{\"ak_sk_app_key\": \"ak_sk_app_key\",\"ak_sk_app_secret\": \"ak_sk_app_secret\"}",
        #                                             'auth_type': 'aksk'}), {})
        # # GET  /app/list 获取所有App列表
        # aapigw_url('get', '/app/list', {}, {})
        # # /app/update 更新应用/更新认证配置
        # aapigw_url('post', '/app/update', json.dumps({'app_key': app_key,
        #                                               'auth_config': "{\"ak_sk_app_key\": \"\",\"ak_sk_app_secret\": \"ak_sk_app_secretaaaaaa\"}",
        #                                               'auth_type': 'aksk'}), {})
        # # GET  /app/list 获取所有App列表
        # aapigw_url('get', '/app/list', {}, {})
        # # /subscribe/add 添加订阅关系
        # aapigw_url('post', '/subscribe/add', json.dumps({'subscribe_list': {
        #            'apiids0000001': ['apptestkeyzf10u1'], 'apiids0000002': ['apptestkeyzf10u1']}}), {})
        # # /subscribe/del 删除订阅关系
        # aapigw_url('post', '/subscribe/del', json.dumps({'subscribe_list': {
        #            'apiids0000001': ['apptestkeyzf10u1'], 'apiids0000002': ['apptestkeyzf10u1']}}), {})

        # # /app/del 删除应用
        # aapigw_url('post', '/app/del', {'app_key': app_key}, {})
        # # /api/del 删除api
        # aapigw_url('post', '/api/del', json.dumps({'delete_list': {
        #            'apigwservernamezf10u': ['apiids0000002', 'apiids0000001', 'apiids0000003', api_ids]}}), {})
        # #    {'service_name': service_name, 'api_ids': api_ids}, {})
        # # GET /service/del 删除服务
        # aapigw_url('get', '/service/del',
        #            {'service_name': service_name}, {})

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

    if api_url == '' or api_method == '':
        return HttpResponse("参数错误！")
    else:
        # 接口请求方式：
        if api_method == 'post' or api_method == 'POST':
            post_r = requests.post(api_url, data=api_params, headers=api_headers)
            result = post_r.text
        elif api_method == 'get' or api_method == 'GET':
            if api_params == '':
                get_r = requests.get(api_url, params=api_params, headers=api_headers)  # params 为空，不做转换
                result = get_r.text
            else:
                get_r = requests.get(api_url, params=eval(api_params), headers=api_headers)  # params 需str转字典
                result = get_r.text
        else:
            return HttpResponse("参数错误！")

        return render(request, 'funlife/resultShow.html',
                      {'result': result, 'api_name': api_name, 'api_url': api_url, 'api_method': api_method,
                       'api_headers': api_headers, 'api_params': api_params})


def htmlstudy(request):
    return render(request, 'funlife/htmlstudy.html')


def mainpage(request):
    usename = request.POST.get('usename')
    password = request.POST.get('password')
    gender = request.POST.get('gender')
    like = request.POST.get('like')
    site = request.POST.get('site')
    about = request.POST.get('about')

    if usename == '' or password == '' or like == '' or site == '' or about == '':
        data = "参数传递不完整"
    else:

        data = {'usename': usename, 'password': password, 'gender': gender, 'like': like, 'site': site, 'about': about}
    return render(request, 'funlife/mainpage.html', {'data': data})


def css_study(request):
    return render(request, 'funlife/css_study.html')


def form_study(request):
    return render(request, 'funlife/form_study.html')


def box_model_study(request):
    return render(request, 'funlife/box_model_study.html')


def js_study(request):
    return render(request, 'funlife/js_study.html')


def bootstrap_study(request):
    return render(request, 'funlife/bootstrap_study.html')


# 以下为慢慢过度写写代码艰难度日！
def homepage(request):
    bookInfo = BookInfo.objects.all().values()
    bookdata = list(bookInfo)

    data = ['hello', 'world', '!']
    data = json.dumps(data)  # data必须是一个list

    return render(request, 'funlife/homepage.html', locals())


def vuestudy(requset):
    data = [1, 2, 3, 4, 5, 6]
    return render(requset, 'funlife/vuestudy.html', locals())


def book_manage(request):
    user = "book_manager"
    return render(request, 'funlife/book_manage.html', locals())


def book_add(request):
    msg = "后端新增接口"
    return render(request, 'funlife/book_add.html', locals())


def book_del(request):
    msg = "后端删除接口"
    return render(request, 'funlife/book_del.html', locals())


def book_show(request):
    msg = "后端展示接口"
    return render(request, 'funlife/book_show.html', locals())


def pipeline_test(request):
    # 通用配置： 
    msg = "流水线接口测试！"
    base_url = 'http://paastest.kcssz.cloud.kingdee.com/pipeline-web/v2'  # 测试
    service_name = 'pipeline'
    Cookie = 'smecm=eyJ1aWQiOjYsIm5pY2tuYW1lIjoi5ZGo6ZSLIiwicGhvbmUiOiIxODcwNTA4MzIwOSIsImVtYWlsIjoiIiwiYXZhdGFyIjoiIiwiZG9tYWluIjoicGFhc3Rlc3Qua2Nzc3ouY2xvdWQua2luZ2RlZS5jb20iLCJhY2Nlc3NfdG9rZW4iOiIifQ==|1623720537129397999|8307f1e6dcf426b2ab3be423ebc4fb7ac5739823; uid=6; nickname=%E5%91%A8%E9%94%8B; project_id=10252; csid=csid162372052151afa27cc3ddebda66d4d662b9b1fdfa|1623750278|39'
    header_con = {'content-type': "application/json", 'Cookie': Cookie}

    pipeline_job_name = 'autopipeline' + str(calendar.timegm(time.gmtime()))

    # 接口请求方式：
    def pipeline_url(method, url, params, headers):
        if method is 'post' or method is 'POST':
            post_r = requests.post(base_url + url, data=params, headers=headers)
            print("====[POST] " + url + '=======errcode: ' + str(post_r.json()['errcode']))
            print(post_r.json())
            return post_r.json()
        elif method is 'get' or method is 'GET':
            get_r = requests.get(base_url + url, params=params, headers=headers)
            print("====[GET]" + url + '========errcode: ' + str(get_r.json()['errcode']))
            print(get_r.json())
            return get_r.json()
        else:
            print("方法错误！")

    # base64加密POST请求入参
    def base64_encode(encode_str):
        r_encode = base64.b64encode(encode_str.encode(encoding="utf-8"))
        result = str(r_encode)[2:-1]
        return result

    # base64解密方法
    def base64_decode(decode_str):
        return base64.b64decode(decode_str).decode()

    # 加密验证
    # print(base64_encode('{"page":1,"page_size":10}'))   # 加密结果 ： eyJwYWdlIjoxLCJwYWdlX3NpemUiOjEwfQ==
    # 解密验证
    # print(base64_decode('eyJwYWdlIjoxLCJwYWdlX3NpemUiOjEwfQ==')) # 解密结果 ： {"page":1,"page_size":10}

    print("*pipeline" + "*" * 60 + "Begin*")

    # 新建流水线
    pipeline_url('post', '/pipeline/create/pipeline', json.dumps(
        {'payload': base64_encode('{"name":pipeline_job_name1,"desc":"desc202106","tmpl_uuid":""}')}), header_con)
    # 获取流水线接口V2 ：
    pipeline_url('post', '/pipeline/list/pipelines',
                 json.dumps({'payload': base64_encode('{"page":1,"page_size":10}')}), header_con)
    # 获取流水线的job_uuid 给后续操作流水线使用
    get_jobuuid_data = pipeline_url('post', '/pipeline/list/pipelines',
                                    json.dumps({'payload': base64_encode('{"page":1,"page_size":10}')}), header_con)[
        'data']['jobs']
    for i in range(len(get_jobuuid_data)):
        if get_jobuuid_data[i]['name'] == "pipeline_job_name":
            # print(get_jobuuid_data[i]['job_uuid'] )
            jobs_uuid = get_jobuuid_data[i]['job_uuid']
            # 删除流水线
            pipeline_url('post', '/pipeline/delete/pipelines',
                         json.dumps({'payload': base64_encode("{'jobs_uuid': jobs_uuid}")}), header_con)
            # 再次获取流水线接口V2 ：
            pipeline_url('post', '/pipeline/list/pipelines',
                         json.dumps({'payload': base64_encode('{"page":1,"page_size":10}')}), header_con)
            # 获取流水线详情： # 待完善job_uuid的来源
            pipeline_url('get', '/pipeline/get/pipeline', {'job_uuid': jobs_uuid}, header_con)

    print("*pipeline" + "*" * 60 + "End*")

    # ide_r = requests.get('http://paasdev.kcssz.cloud.kingdee.com/kwide-web/ajax/workspace',
    #                      params={'name': '', 'cur_page': 1, 'page_num': 10},
    #                      headers={'content-type': "application/json",
    #                               'Cookie': 'Hm_lvt_dfe68e59e6c3b1f180d67c5f94adcaf3=1624327371,1624500209; gr_user_id=40956d5c-8de0-4079-8f5b-06bc211f423e; Hm_lvt_aff7fbe8fcb98b060541077cc76465f2=1625802415; smecm=eyJ1aWQiOjcsIm5pY2tuYW1lIjoi5ZGo6ZSLIiwicGhvbmUiOiIxODcwNTA4MzIwOSIsImVtYWlsIjoiIiwiYXZhdGFyIjoiIiwiZG9tYWluIjoicGFhc2Rldi5rY3Nzei5jbG91ZC5raW5nZGVlLmNvbSIsImFjY2Vzc190b2tlbiI6IiJ9|1626230025923085381|fef050405784ded86409677d3a0271fdacb14a0e; kwidesid=f%5E%D2%08%B8%27%A5%C0Ak%BDF%07+S%1B%A3%7D%A0%9C%CA%89%2C4%E0p%23%A4V%05%82%F9%82%5C%FA%D8K%B1%1A%B7%96T%7C%91i%A2%CEN; csid=csid1626230023c0b5bc1ef0f9b6ec5fd15ea96ddfad2c|1626259261|24'})

    result = get_jobuuid_data
    return render(request, 'funlife/pipeline_test.html', locals())


def webide_test(request):
    tittle = 'WEBIDE 接口测试:'
    # 通用配置
    base_url = 'http://paasdev.kcssz.cloud.kingdee.com/kwide-console'
    # base_url = 'http://paasdev.kcssz.cloud.kingdee.com/kwide-web/ajax'  # 开发
    Cookie = 'gr_user_id=40956d5c-8de0-4079-8f5b-06bc211f423e; Hm_lvt_aff7fbe8fcb98b060541077cc76465f2=1625802415; kwsid=162683387566bffb72fbcc5fbeccf63faafe23ead9; kcsid=16268339658a9df9ddcae7bd6500ac19fba6cba91d; smecm=eyJ1aWQiOjcsIm5pY2tuYW1lIjoi5ZGo6ZSLIiwicGhvbmUiOiIxODcwNTA4MzIwOSIsImVtYWlsIjoiIiwiYXZhdGFyIjoiIiwiZG9tYWluIjoicGFhc2Rldi5rY3Nzei5jbG91ZC5raW5nZGVlLmNvbSIsImFjY2Vzc190b2tlbiI6IiJ9|1627032779731433142|7f84529fd500d7fbb3941746031906b7a634b268; Hm_lvt_dfe68e59e6c3b1f180d67c5f94adcaf3=1627034011; Hm_lpvt_dfe68e59e6c3b1f180d67c5f94adcaf3=1627034011; PPSESSION=2be1uukuqmhasfh1ru8odhp9v0; KERPSESSIONIDierp=1155861116253897728_e5aSm5D5pLyI77uFaLVb3k8EfzlUQBGDWRRSde3SW19k9bfuPdfCp5fS7V8Fk2QN8Vwrp6F6DmEVqkxAt71rZOQoOG1diC6bX33V; KERPSESSIONID=1155861116253897728_e5aSm5D5pLyI77uFaLVb3k8EfzlUQBGDWRRSde3SW19k9bfuPdfCp5fS7V8Fk2QN8Vwrp6F6DmEVqkxAt71rZOQoOG1diC6bX33V; kwidesid=2%02V%85l%BB%FA%A0%0BJx%BFG%1D%A6%94%04%EC3%D25%E7%5DI%F9%C1%D1%C4%0D%D3%3Fw%F6%0C%FAJ%D3%19%2C4%24z%D4LJ%03%90%B1; csid=csid1627032776ff85e6da4fa6ba8bb4971c0e51f1798b|1627277866|140'
    header_con = {'content-type': "application/json", 'Cookie': Cookie, 'Connection': 'close'}

    # 接口请求方式：
    def webide_url(method, url, params, headers):
        if method is 'post' or method is 'POST':
            post_r = requests.post(base_url + url, data=params, headers=headers)
            print("|====[POST] " + url + '====>>>>> ')
            print(post_r.text)
            return post_r.text
        elif method is 'get' or method is 'GET':
            get_r = requests.get(base_url + url, params=params, headers=headers)
            print("|====[GET]" + url + "====>>>>>")
            print(get_r.text)
            return get_r.text
        elif method is 'put' or method is 'PUT':
            put_r = requests.put(base_url + url, data=params, headers=headers)
            print("|====[PUT]" + url + "====>>>>>")
            print(put_r.text)
            return put_r.text
        elif method is 'delete' or method is 'DELETE':
            delete_r = requests.delete(base_url + url, data=params, headers=headers)
            print("|====[DELETE]" + url + "====>>>>>")
            print(delete_r.text)
            return delete_r.text
        else:
            print("方法错误 11！")

    # 获取所有工作空间列表 /workspace
    webide_url('get', '/workspace', {'name': '', 'cur_page': 1, 'page_num': 10}, header_con)
    # 修改工作空间 /workspace
    webide_url('put', '/workspace', json.dumps({'id': 272, 'name': 'updateworkplaceaname11aab1a'}), header_con)
    # 搜索修改后的工作空间 /workspace
    webide_url('get', '/workspace', {'name': 'updateworkplaceaname', 'cur_page': 1, 'page_num': 10}, header_con)

    # 获取所有代码仓库列表 /repository
    webide_url('get', '/repository', {'name': '', 'cur_page': 1, 'page_num': 10}, header_con)
    # 创建代码仓库 /repository
    webide_url('post', '/repository',
               json.dumps({'address': 'http://gitlab.paas.kdcloud.com/fusion/demo1.git',
                           'name': 'mygod_zf_test_rp' + str(random.randint(1, 999)),
                           'token': 'h8Y1jpbrocxh7JFC34Zn'}), header_con)
    # 搜索创建好的代码仓库 /repository
    webide_url('get', '/repository', {'name': 'mygod_zf_test_rp', 'cur_page': 1, 'page_num': 10}, header_con)
    # 获取待删除仓库的id
    to_del_repository_data = webide_url('get', '/repository',
                                        {'name': 'mygod_zf_test_rp', 'cur_page': 1, 'page_num': 10},
                                        header_con)
    to_del_repository_id = (jsonpath.jsonpath(json.loads(to_del_repository_data), '$..id'))[0]
    re_list = jsonpath.jsonpath(json.loads(to_del_repository_data), '$..list')[0]
    # 删除搜索的代码仓库 /repository
    webide_url('delete', '/repository', json.dumps({'id': to_del_repository_id}), header_con)

    # 获取资源地址信息 /resource
    webide_url('get', '/resource', '', header_con)
    # 编辑资源地址 /resource
    webide_url('post', '/resource', json.dumps(
        {'library_address': 'http://dev01-cosmic-devops.cosmic.cloudsz.kingdee.com/appstore/cosmic',
         'resource_address': 'http://dev01-cosmic-devops.cosmic.cloudsz.kingdee.com/appstore/cosmic'}),
               header_con)
    # 获取资源地址 /resource
    webide_url('get', '/resource', '', header_con)

    return render(request, 'funlife/webide_test.html', locals())
