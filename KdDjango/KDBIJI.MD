windows下安装docker详细步骤:
https://blog.csdn.net/vitaair/article/details/80894890
安装在本地： C:\Program Files\Docker Toolbox
验证安装是否成功：CMD输入docker-machine出现版本等信息
关于Virtualbox打开出现e_fail (0x80004005) 组件machinewrap错误--解决方法:升级virtualbox/4.3.12
docker-machine -s "F:\docker" create --engine-registry-mirror=https://rf483vio.mirror.aliyuncs.com -d virtualbox default
docker教程：
https://www.runoob.com/docker/docker-tutorial.html
查看运行的容器 docker ps -a
载入镜像 docker pull 镜像名
查看容器内的标准输出 docker logs +id
后台运行docker   docker run -itd --name ubuntu-test ubuntu /bin/bash
启动容器  docker run -it 镜像名 /bin/bash
检查docker底层信息 docker inspect +镜像名
重启容器 docker restart <容器 ID>
进入容器 docker attach+id
 docker exec+id（推荐）
删除容器 docker rm
停止容器 docker stop +id
退出容器 exit
dockerfile相关：
https://www.cnblogs.com/ricklz/p/11855639.html

docke里面安装python并试着打印helloworld：
vim命令无法使用 ：
先安装apt-get update
apt-get install vim

virtualbox/4.3.12下载：
http://download.virtualbox.org/virtualbox/4.3.12/

linux命令相关：
查看linux机器安装的所有软件 rpm -qa
查看端口占用 lsof -i:端口号
解压文件 tar -xzvf  xxxx.tar.gz
查看运行的服务 systemctl | grep running
由第一行显示文件内容 cat
从最后一行显示文件内容 tac
一页一页显示文件内容 more
只看头几行内容 head 
只看尾巴几行 tail
centos7安装mysql:
https://www.cnblogs.com/lzhdonald/p/12511998.html
django报错：django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have0.9.3.    https://www.52pojie.cn/thread-921141-1-1.html
获取mysql是否监听端口 netstat -apn |grep 3306 
配置mysql文件位置 vim /etc/my.cnf
刷新mysql配置 flush privileges;
停止mysql服务systemctl stop  mysqld.service
启动mysql服务systemctl start mysqld.service
开启远程登录：grant all privileges on *.* to 'root'@'%' identified by '123123' with grant option;
Mysql 8.0以后的版本开启远程登录：
CREATE USER 'root'@'%' IDENTIFIED BY '你的密码'; 
GRANT ALL ON *.* TO 'root'@'%'; 
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '你的密码';
FLUSH PRIVILEGES;

win7登录mysql报错ERROR1045（28000）处理方法:
https://segmentfault.com/a/1190000020994966
需在mysql安装目录下的bin文件夹下运行
先停掉mysql服务：net stop mysql
运行 mysql --console --skip-grant-tables--shared-memory
另开窗口输入mysql
刷新权限  flush privileges
更改密码 alter user‘root’@‘localhost’ IDENIFIED BY ‘1234’
刷新权限  flush privileges
关闭窗口，启动服务  net start mysql
重新连接mysql： mysql -uroot -p1234

Django+Python:
CentOS7下部署Django项目详细操作步骤：
1.centos7+python3+django+SQlite3：https://pythonheidong.com/blog/article/513202/
2.sqltie3登出后失效运行：export LD_LIBRARY_PATH="/usr/local/lib" ，也可以写进~/.bashrc 或 ~/.bash_profile，再更新source ~/.bashrc 或~/.bash_profile
3.后台运行django：
3.1、安装工具：yum install screen
3.2、创建screen窗口 screen -S  +名称
3.3、退出保存 CTRL-A+D
3.4、恢复原来的工作状态 screen -r
3.5、停止  ，先查看 screen -ls，只有一个screen进程则 screen -r -d 进入后ctrl+C，如果多个screen进程，则screen -r -d +PID进入后ctrl+C
查看python3版本： python3 -V
       查看pip3版本：pip3 -V
查看sqlite3版本：sqlite3 --version
更新sqlite版本：export LD_LIBRARY_PATH="/usr/local/lib"
创建django项目：django-admin.py startproject 项目名
启动服务器：python  manage.py runserver 0.0.0.0:8000
创建APP： django-admin.py startapp 模型名
APP的变更：
python  manage.py migrate   # 创建表结构
python  manage.py makemigrations TestModel  # 让 Django 知道模型有一些变更
python  manage.py migrate TestModel   # 创建表结构
 报错Forbidden (CSRF cookie not set.):项目文件中的setting.py中将csrf语句注释掉
django之分页功能：https://www.cnblogs.com/kongzhagen/p/6640975.html
卸载自带PYTHON:
1.rpm -qa | grep python | xargs rpm -e --allmatches --nodeps //强制卸载自带的python以及相关联的程序
2.whereis python | xargs rm -rf //删除所有与python相关的残余文件
VMware安装Centos7超详细过程（图文）:
https://blog.csdn.net/babyxue/article/details/80970526
K8S相关:
业务节点抹掉配置 ：kubeadm reset
kubectl run 创建容器
kubectl get pods 查询资源列表
kubectl describe 获取资源想想信息
kubectl logs 获取容器日志
kubectl exec 在容器内执行一个命令


