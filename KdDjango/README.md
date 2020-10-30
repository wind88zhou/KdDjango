# KdDjango
这是锋哥玩儿的地盘！船新滴开始！

20201030
查询相关函数
get --  返回一条且只能有一条数据，返回值是一个对象，参数可以写查询条件。
all -- 返回模型类对应的所有数据，返回值是QuerySet
filter -- 返回满足条件的数据，返回值是QuerySet，参数可以写查询条件
exclude -- 返回不满足条件的数据，返回值是QuerySet，参数可以写查询条件
order_by -- 对查询结果进行排序，返回值是QuerySet，参数中写排序的字段

以下类需导入：  from django.db.models import F,Q,Sum,Count,Avg,Max.Min
F对象：用于类属性之间的比较
Q对象：用于条件之间的逻辑关系（与或非）

aggregate:进行聚合操作，返回值是个字典（字段_聚合方式: 结果）
count：返回结果集中数据的数目，返回值是一个数字

注意：
    对一个QuerySet实例对象，可以继续调用上面的所有函数

20201020
今天到体检啊  抽了5管血啊
试试新下载的代码管理工具gitkraken，下载地址：https://www.gitkraken.com/

20201014
新增admin.py

20201009
新买了3年的云服务器测试一下git及django
云服务器主机IP：81.71.139.152 

20200929
来回顾下，怕忘记git命令了
 git status
 git add +文件
 git commit -m “提交说明”
 git push origin master   

20200928
先去做工作了！

20200927 
通过腾讯云服务器上新一批新茶！
不错！不错！学会使用Git相关命令！表扬一下！nice！

20200731
新上一批好货！
